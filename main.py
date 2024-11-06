from PDFGenerator import PDFGenerator
from EmailSender import EmailSender
from Web1 import Web1
from Web2 import Web2
from termcolor import colored  # Import termcolor for colored output

# Main Function to Orchestrate the Process
def main():
    url1 = "https://economictimes.indiatimes.com/tech/startups"
    url2 = "https://techfundingnews.com/category/ai/"

    # Create scraper instances for Web1 and Web2
    scraper1 = Web1()
    articles1 = scraper1.scrape_startup_news()

    scraper2 = Web2()
    articles2 = scraper2.scrape_startup_news()

    # Print the URLs in blue
    print(colored(f"URL1: {url1}", "blue"))
    print(colored(f"URL2: {url2}", "blue"))

    # Print the articles to debug
    print("Web1 Articles:", articles1)
    print("Web2 Articles:", articles2)

    # Prepare a list of articles with title and description for Web1 and Web2
    news_array1 = [{'title': article['title'], 'description': article['description']} for article in articles1]
    news_array2 = [{'title': article['title'], 'description': article['description']} for article in articles2]

    # Create the PDF
    pdf_filename = "tech_news.pdf"  # Define PDF filename
    pdf_gen = PDFGenerator(filename=pdf_filename)

    # Generate PDF with the URL added as text and articles below it
    combined = []
    if articles1:
        combined.append({'title': url1, 'description': 'Startup News from the Economic Times'})
        combined.extend(news_array1)
    if articles2:
        combined.append({'title': url2, 'description': 'Startup News from Tech Funding News'})
        combined.extend(news_array2)

    # Create PDF with the combined articles
    pdf_gen.create_pdf(combined)

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
