from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Create a new PDF document
pdf_file = "example.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)


# Add some text to the PDF
c.drawString(100, 700, "Hello, world!")


# Save the PDF
c.save()


print("PDF created!")