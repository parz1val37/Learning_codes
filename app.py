from shiny import App, ui, render, reactive
import pandas as pd
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import uuid
from io import BytesIO

# Reactive storage
items = reactive.Value(pd.DataFrame(columns=["id", "Product_Code", "Qty", "Category", "Price"]))
edit_uuid = reactive.Value(None)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_text("code", "Product_Code", ""),
        ui.input_select(
            "desc", "Category",
            {"Shirt": "Shirt", "Pants": "Pants", "T-Shirt": "T-Shirt", "Trouser": "Trouser"},
        ),
        ui.input_numeric("qty", "Quantity", 1, min=1),
        ui.input_numeric("price", "Price", 0, min=0.0, step=0.01),
        ui.input_slider("tax_rate", "Tax (%)", 0, 20, 8, step=1),
        ui.layout_columns(
            ui.column(
                3,
                ui.input_action_button(
                    "add", "➕ Add Item",
                    class_="btn btn-sm",
                    style=(
                        "background-color:#028a7e; color:white; border: 1px solid rgba(255, 255, 255, 0.4); border-radius: 12px; backdrop-filter: blur(8px); font-weight:bold; "
                        "padding:6px 0; height:75px; width:69px;"
                    )
                )
            ),
            ui.column(
                4,
                ui.input_action_button(
                    "update", "✏️ Update Item",
                    class_="btn btn-sm",
                    style=(
                        "background-color:#f0ad4e; color:white; border: 1px solid rgba(255, 255, 255, 0.4); border-radius: 12px; backdrop-filter: blur(8px); font-weight:bold; "
                        "padding:8px 0; height:75px; width:70px;"
                    )
                )
            ),
            ui.column(
                5,
                ui.input_action_button(
                    "clear", "🗑️ Clear All",
                    class_="btn btn-sm",
                    style=(
                        "background-color:#d9534f; color:white; border: 1px solid rgba(255, 255, 255, 0.4); border-radius: 12px; backdrop-filter: blur(8px); font-weight:bold; "
                        "padding:8px 0; height:75px; width:69px;"
                    )
                )
            ),
        ),
        ui.download_button(
            "download_pdf", "🧾 Download Receipt",
            class_="btn btn-sm",
            style="background-color:#6c757d; color:white; border:none; font-weight:bold; width:100%;"
        ),
    ),
    ui.tags.style("""body { background: #036c5f !important; }"""),
    ui.layout_columns(
        ui.card(
            ui.card_header("Items Added"),
            ui.output_ui("items_table"),
        ),
        ui.card(
            ui.card_header("Generated Receipt"),
            ui.output_ui("receipt"),
        ),
    ),
)

def server(input, output, session):
    @reactive.effect
    @reactive.event(input.add)
    def _add():
        df = items.get().copy()
        df = pd.concat(
            [df, pd.DataFrame([{
                "id": uuid.uuid4().hex,
                "Product_Code": input.code(),
                "Qty": input.qty(),
                "Category": input.desc(),
                "Price": input.price(),
            }])],
            ignore_index=True,
        )
        items.set(df)

    @reactive.effect
    @reactive.event(input.update)
    def _update():
        uid = edit_uuid.get()
        if uid is not None:
            df = items.get().copy()
            idx = df.index[df["id"] == uid].tolist()
            if idx:
                df.loc[idx[0]] = {
                    "id": uid,
                    "Product_Code": input.code(),
                    "Qty": input.qty(),
                    "Category": input.desc(),
                    "Price": input.price(),
                }
                items.set(df)
                edit_uuid.set(None)

    @reactive.effect
    @reactive.event(input.clear)
    def _clear():
        items.set(pd.DataFrame(columns=["id", "Product_Code", "Qty", "Category", "Price"]))

    @reactive.effect
    @reactive.event(input.remove_id)
    def _remove():
        uid = input.remove_id()
        df = items.get().copy()
        idx = df.index[df["id"] == uid].tolist()
        if idx:
            df = df.drop(idx[0]).reset_index(drop=True)
            items.set(df)

    @reactive.effect
    @reactive.event(input.edit_id)
    def _edit():
        uid = input.edit_id()
        df = items.get().copy()
        idx = df.index[df["id"] == uid].tolist()
        if idx:
            row = df.iloc[idx[0]]
            session.send_input_message("code", {"value": str(row["Product_Code"])})
            session.send_input_message("desc", {"value": str(row["Category"])})
            session.send_input_message("qty", {"value": float(row["Qty"])})
            session.send_input_message("price", {"value": float(row["Price"])})
            edit_uuid.set(uid)

    @output
    @render.ui
    def items_table():
        df = items.get()
        if df.empty:
            return ui.p("No items yet.")

        rows_html = []
        for r in df.itertuples():
            rows_html.append(f"""
                <tr>
                  <td style="white-space:nowrap;">
                    <button class="btn btn-sm btn-warning"
                        onclick="Shiny.setInputValue('edit_id', '{r.id}', {{priority:'event'}})">✏️ Edit</button>
                    <button class="btn btn-sm btn-danger"
                        onclick="Shiny.setInputValue('remove_id', '{r.id}', {{priority:'event'}})">❎ Delete</button>
                  </td>
                  <td>{r.Product_Code}</td>
                  <td>{r.Qty}</td>
                  <td>{r.Category}</td>
                  <td>{r.Price:.2f}</td>
                </tr>
            """)

        return ui.HTML(f"""
            <table class="table table-sm" style="font-size:13px; border-collapse:collapse;">
              <thead>
                <tr><th style="width:140px;">Actions</th><th>Product_Code</th><th>Qty</th><th>Item</th><th>Price</th></tr>
              </thead>
              <tbody>
                {''.join(rows_html)}
              </tbody>
            </table>
        """)

    @output
    @render.ui
    def receipt():
        df = items.get()
        if df.empty:
            return ui.p("No items yet.")

        subtotal = float((df["Qty"] * df["Price"]).sum())
        tax_rate = input.tax_rate() / 100.0
        tax = round(subtotal * tax_rate, 2)
        total = round(subtotal + tax, 2)
        now = datetime.datetime.now()

        lines = "".join(
            f"<tr><td>{row.Product_Code}</td><td>{row.Qty}</td><td>{row.Category}</td><td>{row.Price:.2f}</td></tr>"
            for row in df.itertuples()
        )

        return ui.HTML(f"""
        <div style="border-radius:10px; background-color:#f7f7f7; padding:10px; width:300px; font-family:Arial, sans-serif; font-size:13px">
          <h4 style="text-align:center; margin:0; color:#028a7e;">RECEIPT 🧾</h4>
          <hr style="margin:4px 0; border-color:#028a7e;">
          <table style="width:100%; font-size:12px; border-collapse:collapse;">
            <tr style="background-color:#028a7e; color:white;">
                <th>Product_Code</th><th>Qty</th><th>Item</th><th>Price</th>
            </tr>
            {lines}
          </table>
          <hr style="margin:4px 0;">
          <p style="margin:2px 0;">Subtotal: {subtotal:.2f}</p>
          <p style="margin:2px 0;">Tax ({input.tax_rate()}%): {tax:.2f}</p>
          <p style="margin:2px 0; font-weight:bold;">Total: {total:.2f}</p>
          <hr style="margin:4px 0;">
          <p style="margin:2px 0;">Date: {now.strftime('%d/%m/%Y')}</p>
          <p style="margin:2px 0;">Time: {now.strftime('%I:%M %p')}</p>
        </div>
        """)

    @render.download(filename=lambda: f"receipt_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
    def download_pdf():
        df = items.get()
        if df.empty:
            yield b""
            return

        subtotal = float((df["Qty"] * df["Price"]).sum())
        tax_rate = input.tax_rate() / 100.0
        tax = round(subtotal * tax_rate, 2)
        total = round(subtotal + tax, 2)
        now = datetime.datetime.now()

        buffer = BytesIO()
        RECEIPT_WIDTH, RECEIPT_HEIGHT = 250, 600
        doc = SimpleDocTemplate(buffer, pagesize=(RECEIPT_WIDTH, RECEIPT_HEIGHT),
                                leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10)
        styles = getSampleStyleSheet()
        elements = []

        # Custom header style
        header_style = ParagraphStyle('header', fontSize=14, textColor=colors.HexColor("#028a7e"), alignment=1, spaceAfter=6)
        normal_style = ParagraphStyle('normal', fontSize=10)
        bold_style = ParagraphStyle('bold', fontSize=10, leading=12, spaceAfter=2, fontName="Helvetica-Bold")

        # Header
        elements.append(Paragraph("PARZi GLOBAL", header_style))
        elements.append(Paragraph(f"Receipt No.: {now.strftime('%Y%m%d%H%M%S')}", normal_style))
        elements.append(Spacer(1, 8))

        # Table data
        data = [["Product_Code", "Qty", "Item", "Price"]]
        for row in df.itertuples():
            data.append([row.Product_Code, row.Qty, row.Category, f"{row.Price:.2f}"])
        table = Table(data, colWidths=[60, 30, 80, 50])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#028a7e")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 9),
            ("ALIGN", (1, 1), (-1, -1), "CENTER"),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 8))

        # Totals
        elements.append(Paragraph(f"Subtotal: {subtotal:.2f}", normal_style))
        elements.append(Paragraph(f"Tax ({input.tax_rate()}%): {tax:.2f}", normal_style))
        elements.append(Paragraph(f"Total: {total:.2f}", bold_style))
        elements.append(Spacer(1, 8))

        # Date/Time
        elements.append(Paragraph(f"Date: {now.strftime('%d/%m/%Y')}", normal_style))
        elements.append(Paragraph(f"Time: {now.strftime('%I:%M %p')}", normal_style))

        doc.build(elements)
        buffer.seek(0)
        yield buffer.read()

app = App(app_ui, server)
