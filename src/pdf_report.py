from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO


def generate_pdf_report(total_units, total_revenue, lowest_stock, best_product):
    buffer = BytesIO()

    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(50, height - 50, "AI Inventory Forecast Report")

    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, height - 90, "Executive Summary")

    pdf.drawString(50, height - 130, f"Total Units Sold: {total_units}")
    pdf.drawString(50, height - 155, f"Total Revenue: ${total_revenue:,.0f}")
    pdf.drawString(50, height - 180, f"Lowest Stock: {lowest_stock}")
    pdf.drawString(50, height - 205, f"Best Seller: {best_product}")

    pdf.drawString(50, height - 250, "AI Recommendation:")
    pdf.drawString(50, height - 275, "Review low-stock products and reorder high-demand items.")

    pdf.save()
    buffer.seek(0)

    return buffer