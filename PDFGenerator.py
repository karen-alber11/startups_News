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

        current_url = None

        for article in news:
            # Check if we need to start a new section with a URL
            if article.get('url') and article['url'] != current_url:
                current_url = article['url']

                # Add the URL as a clickable link in blue
                pdf.set_text_color(0, 0, 255)  # Blue color for URL
                pdf.cell(0, 10, txt=current_url, ln=True, link=current_url)

                # Add a short hashed separator line after the URL
                pdf.set_text_color(0, 0, 0)  # Reset color to black
                pdf.cell(0, 5, txt="--------------------------------", ln=True)
                pdf.ln(2)

            # Print the title in bold
            pdf.set_font("Arial", 'B', size=12)  # Bold font for title
            pdf.cell(0, 10, txt=self.sanitize_text(article['title']), ln=True)

            # Print the description
            if 'description' in article and article['description']:
                pdf.set_font("Arial", size=12)  # Regular font for description
                pdf.multi_cell(0, 10, txt=self.sanitize_text(article['description']))

            # Add a long bolded line after each article
            y = pdf.get_y()
            pdf.set_font("Arial", 'B', size=12)
            pdf.line(10, y, 200, y)  # First bold line
            pdf.ln(5)

            # Check if the next article has a different URL or if we're at the last article
            if (news.index(article) == len(news) - 1) or (news[news.index(article) + 1].get('url') != current_url):
                # Add two long bolded lines if it's the last article in the current URL section
                y = pdf.get_y()
                pdf.line(10, y, 200, y)  # First long bold line
                pdf.line(10, y + 2, 200, y + 2)  # Second long bold line
                pdf.ln(8)  # Add some space for the next section

        pdf.output(self.filename)

    def sanitize_text(self, text):
        """Replace or remove special characters from text."""
        replacements = {
            "\u2019": "'",  # Replace right single quote with apostrophe
            "\u2018": "'",  # Replace left single quote with apostrophe
            "\u201c": '"',  # Replace left double quote with "
            "\u201d": '"',  # Replace right double quote with "
        }

        # Apply replacements
        for old, new in replacements.items():
            text = text.replace(old, new)

        return text
