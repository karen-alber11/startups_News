# from NewsScraper import NewsScraper
from PDFGenerator import PDFGenerator
from EmailSender import EmailSender
from Scheduler import Scheduler

# Main Function to Orchestrate the Process
def main():
    # Initialize the scraper
    # scraper = NewsScraper()

    # Fetch news articles
    # news_array = scraper.get_startup_news()
    news_array = ["Hello Karen!"]

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
