from shiny import App, ui, render, reactive
import pandas as pd
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import tempfile, os

# Reactive storage
items = reactive.Value(pd.DataFrame(columns=["Product_Code", "Qty", "Category", "Price"]))
edit_index = reactive.Value(None)

app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.input_text("code", "Product_Code", ""),
        ui.input_select(
            "desc", "Category",
            {"Shirt": "Shirt", "Pants": "Pants", "T-Shirt": "T-Shirt", "Trouser": "Trouser"},
        ),
        ui.input_numeric("qty", "Quantity", 1, min=1),
        ui.input_numeric("price", "Price", 0.0, min=0.0, step=0.01),
        ui.input_slider("tax_rate", "Tax (%)", 0, 20, 8, step=1),
        ui.layout_columns(
            ui.input_action_button("add", "Add Item", class_="btn btn-primary btn-sm"),
            ui.input_action_button("update", "Update Item", class_="btn btn-success btn-sm"),
            ui.input_action_button("clear", "Clear All", class_="btn btn-danger btn-sm"),
        ),
        ui.download_button("download_pdf", "Download Receipt (PDF)", class_="btn btn-secondary btn-sm"),
        open="always",
    ),
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
        idx = edit_index.get()
        if idx is not None:
            df = items.get().copy()
            if 0 <= idx < len(df):
                df.loc[idx] = {
                    "Product_Code": input.code(),
                    "Qty": input.qty(),
                    "Category": input.desc(),
                    "Price": input.price(),
                }
                items.set(df)
                edit_index.set(None)

    @reactive.effect
    @reactive.event(input.clear)
    def _clear():
        items.set(pd.DataFrame(columns=["Product_Code", "Qty", "Category", "Price"]))

    @reactive.effect
    @reactive.event(input.remove_index)
    def _remove():
        idx = int(input.remove_index())
        df = items.get().copy()
        if 0 <= idx < len(df):
            items.set(df.drop(idx).reset_index(drop=True))

    @reactive.effect
    @reactive.event(input.edit_index)
    def _edit():
        idx = int(input.edit_index())
        df = items.get().copy()
        if 0 <= idx < len(df):
            row = df.iloc[idx]
            session.send_input_message("code", {"value": str(row["Product_Code"])})
            session.send_input_message("desc", {"value": str(row["Category"])})
            session.send_input_message("qty", {"value": float(row["Qty"])})
            session.send_input_message("price", {"value": float(row["Price"])})
            edit_index.set(idx)

    @output
    @render.ui
    def items_table():
        df = items.get()
        if df.empty:
            return ui.p("No items yet.")

        rows_html = []
        for i, r in df.iterrows():
            rows_html.append(
                f"""
                <tr>
                  <td style="white-space:nowrap;">
                    <button class="btn btn-sm btn-warning"
                      onclick="Shiny.setInputValue('edit_index', {i}, {{priority:'event'}})">✏️ Edit</button>
                    <button class="btn btn-sm btn-danger"
                      onclick="Shiny.setInputValue('remove_index', {i}, {{priority:'event'}})">❎ Delete</button>
                  </td>
                  <td>{r['Product_Code']}</td>
                  <td>{r['Qty']}</td>
                  <td>{r['Category']}</td>
                  <td>{r['Price']:.2f}</td>
                </tr>
                """
            )

        return ui.HTML(
            """
            <table class="table table-sm" style="font-size:13px; border-collapse:collapse;">
              <thead>
                <tr><th style="width:140px;">Actions</th><th>Product_Code</th><th>Qty</th><th>Item</th><th>Price</th></tr>
              </thead>
              <tbody>
            """ + "\n".join(rows_html) + """
              </tbody>
            </table>
            """
        )

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
        <div style="border:1px solid #000; padding:10px; width:280px; font-family:monospace; font-size:13px">
          <h4 style="text-align:center; margin:0;">RECEIPT 🧾</h4>
          <p style="margin:2px 0;">Nr.: 69 </p>
          <hr style="margin:4px 0;">
          <table style="width:100%; font-size:12px; border-collapse:collapse;">
            <tr><th>Product_Code</th><th>Qty</th><th>Item</th><th>Price</th></tr>
            {lines}
          </table>
          <hr style="margin:4px 0;">
          <p style="margin:2px 0;">Subtotal: {subtotal:.2f}</p>
          <p style="margin:2px 0;">Tax ({input.tax_rate()}%): {tax:.2f}</p>
          <p style="margin:2px 0;"><b>Total: {total:.2f}</b></p>
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

        from io import BytesIO
        buffer = BytesIO()

        RECEIPT_WIDTH = 220  # ~80mm
        RECEIPT_HEIGHT = 600
        receipt_page = (RECEIPT_WIDTH, RECEIPT_HEIGHT)

        doc = SimpleDocTemplate(
            buffer,
            pagesize=receipt_page,
            leftMargin=10, rightMargin=10, topMargin=10, bottomMargin=10
        )
        styles = getSampleStyleSheet()
        elements = []

        # ---- Shop name / Header ----
        elements.append(Paragraph("<b>PARZi GLOBAL</b>", styles["Title"]))
        elements.append(Paragraph(f"Nr.: {now.strftime('%Y%m%d%H%M%S')}", styles["Normal"]))
        elements.append(Spacer(1, 8))

        # Items Table
        data = [["Product_Code", "Qty", "Item", "Price"]]
        for row in df.itertuples():
            data.append([row.Product_Code, row.Qty, row.Category, f"{row.Price:.2f}"])
        table = Table(data, colWidths=[40, 30, 70, 50])
        table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("FONTNAME", (0, 0), (-1, -1), "Courier"),
            ("FONTSIZE", (0, 0), (-1, -1), 8),
            ("ALIGN", (1, 1), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 8))

        # Totals
        elements.append(Paragraph(f"Subtotal: {subtotal:.2f}", styles["Normal"]))
        elements.append(Paragraph(f"Tax ({input.tax_rate()}%): {tax:.2f}", styles["Normal"]))
        elements.append(Paragraph(f"<b>Total: {total:.2f}</b>", styles["Normal"]))
        elements.append(Spacer(1, 8))

        # Date/Time
        elements.append(Paragraph(f"Date: {now.strftime('%d/%m/%Y')}", styles["Normal"]))
        elements.append(Paragraph(f"Time: {now.strftime('%I:%M %p')}", styles["Normal"]))

        doc.build(elements)

        buffer.seek(0)
        yield buffer.read()


app = App(app_ui, server)
