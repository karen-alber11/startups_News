from PDFGenerator import PDFGenerator
from EmailSender import EmailSender
from Web1 import Web1  # Ensure this imports the Web1 class

# Main Function to Orchestrate the Process
def main():
    scraper = Web1()  # Create an instance of the Web1 class
    articles = scraper.scrape_startup_news()  # Fetch the articles from the Web1 class

    # Prepare a list of articles with title and description
    news_array = [{'title': article['title'], 'description': article['description']} for article in articles]

    # Generate PDF with the news
    pdf_filename = "tech_news.pdf"  # Define PDF filename
    pdf_gen = PDFGenerator(filename=pdf_filename)
    pdf_gen.create_pdf(news_array)

    # Send email with the generated PDF
    email_sender = EmailSender(
        from_email="karenalber11@gmail.com",
        password="ygwg oajl xwqu hfeo",  # Use your generated app password
        to_email="karenalber.work@gmail.com",
        smtp_server="smtp.gmail.com",
        port=587
    )
    email_sender.send_email(
        subject="Daily Tech Startup News",
        body="Please find attached the latest news on tech startups.",
        pdf_filename=pdf_filename
    )

if __name__ == "__main__":
    main()