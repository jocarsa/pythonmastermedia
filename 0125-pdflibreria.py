from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("basesdatos.pdf")
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Add a password to the new PDF
writer.encrypt("mastermedia")

# Save the new PDF to a file
with open("basesdatos2.pdf", "wb") as f:
    writer.write(f)
