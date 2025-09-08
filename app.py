from shiny import App, ui, render, reactive, session
import pandas as pd
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# Reactive storage
items = reactive.Value([])  # store as list of dicts
edit_index = reactive.Value(None)

# ---------------------- UI ----------------------
app_ui = ui.page_navbar(
    ui.nav_panel(
        "Manage Items",
        ui.layout_columns(
            ui.card(
                ui.card_header("Add / Edit Items"),
                ui.input_text("code", "Product Code", ""),
                ui.input_select(
                    "desc", "Category",
                    {"Shirt": "Shirt", "Pants": "Pants", "T-Shirt": "T-Shirt", "Trouser": "Trouser"},
                ),
                ui.input_numeric("qty", "Quantity", 1, min=1),
                ui.input_numeric("price", "Price", 0.0, min=0.0, step=0.01),
                ui.input_slider("tax", "Tax (%)", 0, 20, 8, step=1),
                ui.layout_columns(
                    ui.input_action_button("add", "➕ Add Item", class_="btn btn-success btn-sm"),
                    ui.input_action_button("update", "📑 Update Item", class_="btn btn-warning btn-sm"),
                    ui.input_action_button("clear", "🆑 Clear All", class_="btn btn-danger btn-sm"),
                ),
                ui.download_button("download_pdf", "⬇️ Download Receipt (PDF)", class_="btn btn-secondary btn-sm"),
            ),
            ui.card(
                ui.card_header("Items Added"),
                ui.output_ui("items_table"),
            ),
        ),
    ),
    ui.nav_panel(
        "Receipt",
        ui.card(
            ui.card_header("Generated Receipt"),
            ui.output_ui("receipt"),
        )
    ),
    title="🧾 Receipt Generator",
    id="main_tabs",
    navbar_options=ui.navbar_options(
        bg="#036c5f",      # green navbar
        dark=True,         # white text
    ),
)

# Extra CSS
app_ui = ui.TagList(
    app_ui,
    ui.tags.style("""
        body { background: #036c5f !important; color: #f1f1f1 !important; }
        .navbar { background-color: #036c5f !important; }
        .nav-link, .navbar-brand { color: #ffffff !important; }
        .nav-link.active { background-color: #024d45 !important; }
        .card { background-color: #024d45 !important; color: #ffffff !important; border-radius: 10px; }
        .table { color: #ffffff !important; font-size: 13px; }
        .btn-success { background-color: #28a745 !important; border: none; }
        .btn-warning { background-color: #ffc107 !important; border: none; color: black !important; }
        .btn-danger { background-color: #dc3545 !important; border: none; }
        .btn-secondary { background-color: #17a2b8 !important; border: none; }
        .receipt-box { background: #024d45; padding: 10px; border-radius: 8px; }
    """)
)

# ---------------------- SERVER ----------------------
def server(input, output, session):
    @reactive.effect
    @reactive.event(input.add)
    def _add():
        data = items.get().copy()
        data.append({
            "code": input.code(),
            "desc": input.desc(),
            "qty": input.qty(),
            "price": input.price(),
            "tax": input.tax(),
        })
        items.set(data)

    @reactive.effect
    @reactive.event(input.update)
    def _update():
        idx = edit_index.get()
        if idx is not None:
            data = items.get().copy()
            if 0 <= idx < len(data):
                data[idx] = {
                    "code": input.code(),
                    "desc": input.desc(),
                    "qty": input.qty(),
                    "price": input.price(),
                    "tax": input.tax(),
                }
                items.set(data)
                edit_index.set(None)

    @reactive.effect
    @reactive.event(input.clear)
    def _clear():
        items.set([])

    # Items table
    @output
    @render.ui
    def items_table():
        data = items.get()
        if not data:
            return ui.p("No items yet.")

        rows_html = []
        for i, r in enumerate(data):
            rows_html.append(
                f"""
                <tr>
                  <td style="white-space:nowrap;">
                    <button class="btn btn-sm btn-light"
                      onclick="Shiny.setInputValue('edit_index', {i}, {{priority:'event'}})">✏️</button>
                    <button class="btn btn-sm btn-danger"
                      onclick="Shiny.setInputValue('remove_index', {i}, {{priority:'event'}})">❌</button>
                  </td>
                  <td>{r['code']}</td>
                  <td>{r['desc']}</td>
                  <td>{r['qty']}</td>
                  <td>{r['price']:.2f}</td>
                  <td>{r['tax']}%</td>
                </tr>
                """
            )

        return ui.HTML(
            """
            <table class="table table-sm table-bordered">
              <thead>
                <tr><th>Actions</th><th>Code</th><th>Category</th><th>Qty</th><th>Price</th><th>Tax</th></tr>
              </thead>
              <tbody>
            """ + "\n".join(rows_html) + """
              </tbody>
            </table>
            """
        )

    # Receipt preview
    @output
    @render.ui
    def receipt():
        data = items.get()
        if not data:
            return ui.p("No receipt yet.")

        rows = "".join(
            f"""
            <tr>
                <td>{i+1}</td>
                <td>{r['code']}</td>
                <td>{r['desc']}</td>
                <td>{r['qty']}</td>
                <td>{r['price']:.2f}</td>
                <td>{r['tax']}%</td>
                <td>{r['qty'] * r['price'] * (1 + r['tax']/100):.2f}</td>
            </tr>
            """
            for i, r in enumerate(data)
        )
        total = sum(r['qty'] * r['price'] * (1 + r['tax']/100) for r in data)
        now = datetime.datetime.now()

        return ui.HTML(f"""
        <div class="receipt-box">
            <h5 style="text-align:center;">🧾 Receipt Preview</h5>
            <table class="table table-sm table-bordered">
                <thead>
                    <tr><th>#</th><th>Code</th><th>Category</th>
                        <th>Qty</th><th>Price</th><th>Tax</th><th>Total</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
            <hr>
            <h6>Grand Total: ₹{total:.2f}</h6>
            <p>Date: {now.strftime('%d/%m/%Y')} | Time: {now.strftime('%I:%M %p')}</p>
        </div>
        """)

    # PDF download
    @session.download(filename=lambda: f"receipt_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
    def download_pdf():
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        elements = []

        data = items.get()
        if not data:
            buffer.seek(0)
            return buffer

        # Header
        now = datetime.datetime.now()
        elements.append(Paragraph("<b>🧾 PARZi GLOBAL</b>", styles["Title"]))
        elements.append(Paragraph(f"Date: {now.strftime('%d/%m/%Y')} Time: {now.strftime('%I:%M %p')}", styles["Normal"]))
        elements.append(Spacer(1, 12))

        # Items
        table_data = [["#", "Code", "Category", "Qty", "Price", "Tax %", "Total"]]
        total = 0
        for i, r in enumerate(data):
            line_total = r["qty"] * r["price"] * (1 + r["tax"]/100)
            total += line_total
            table_data.append([i+1, r["code"], r["desc"], r["qty"], f"{r['price']:.2f}", f"{r['tax']}%", f"{line_total:.2f}"])

        table = Table(table_data, colWidths=[20, 50, 70, 30, 50, 40, 60])
        table.setStyle(TableStyle([
            ("GRID", (0,0), (-1,-1), 0.5, colors.black),
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
            ("ALIGN", (3,1), (-1,-1), "CENTER"),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 12))

        # Totals
        elements.append(Paragraph(f"<b>Grand Total: ₹{total:.2f}</b>", styles["Normal"]))

        doc.build(elements)
        buffer.seek(0)
        return buffer

    # Remove / Edit events
    @reactive.effect
    @reactive.event(input.remove_index)
    def _remove():
        idx = int(input.remove_index())
        data = items.get().copy()
        if 0 <= idx < len(data):
            data.pop(idx)
            items.set(data)

    @reactive.effect
    @reactive.event(input.edit_index)
    def _edit():
        idx = int(input.edit_index())
        data = items.get()
        if 0 <= idx < len(data):
            row = data[idx]
            session.send_input_message("code", {"value": row["code"]})
            session.send_input_message("desc", {"value": row["desc"]})
            session.send_input_message("qty", {"value": row["qty"]})
            session.send_input_message("price", {"value": row["price"]})
            session.send_input_message("tax", {"value": row["tax"]})
            edit_index.set(idx)


app = App(app_ui, server)
