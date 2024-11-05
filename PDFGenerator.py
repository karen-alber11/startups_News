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
            # Print the title in bold
            pdf.set_font("Arial", 'B', size=12)  # Bold font
            pdf.cell(0, 10, txt=self.sanitize_text(article['title']), ln=True)
            pdf.set_font("Arial", size=12)  # Regular font
            pdf.multi_cell(0, 10, txt=self.sanitize_text(article['description']))  # Description in regular font

            # Print a dashed line
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())  # Draw a line at the current Y position
            pdf.ln(5)  # Add a little space after the line

        pdf.output(self.filename)

    def sanitize_text(self, text):
        """Replace or remove special characters from text."""
        # Example replacements (you can add more as needed)
        replacements = {
            "\u2019": "'",  # Replace right single quote with apostrophe
            "\u2018": "'",  # Replace left single quote with apostrophe
            "\u201c": '"',  # Replace left double quote with "
            "\u201d": '"',  # Replace right double quote with "
            # Add more replacements if necessary
        }

        # Apply replacements
        for old, new in replacements.items():
            text = text.replace(old, new)

        return text
