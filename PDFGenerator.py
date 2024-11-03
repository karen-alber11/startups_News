from fpdf import FPDF

class PDFGenerator:
    def __init__(self, filename="tech_news.pdf"):
        self.filename = filename

    def create_pdf(self, news):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Daily Tech Startup News", ln=True, align='C')
        pdf.ln(10)

        for article in news:
            pdf.multi_cell(0, 10, txt=article)
            pdf.ln(5)  # Add a little space between articles

        pdf.output(self.filename)
