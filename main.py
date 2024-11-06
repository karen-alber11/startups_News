from termcolor import colored
from PDFGenerator import PDFGenerator
from EmailSender import EmailSender
from Web1 import Web1
from Web2 import Web2
from Web3 import Web3
from Web4 import Web4

# Function to sanitize text by replacing problematic characters
def sanitize_text(text):
    # Replace ellipsis with three dots
    return text.replace('…', '...')

# Main Function to Orchestrate the Process
def main():
    url1 = "https://economictimes.indiatimes.com/tech/startups"
    url2 = "https://techfundingnews.com/category/ai/"
    url3 = "https://techcrunch.com/category/startups/"
    url4 = "https://disruptafrica.com/category/startups/"

    # Create scraper instances for Web1, Web2, Web3, and Web4
    scraper1 = Web1()
    articles1 = scraper1.scrape_startup_news()

    scraper2 = Web2()
    articles2 = scraper2.scrape_startup_news()

    scraper3 = Web3()
    articles3 = scraper3.scrape_startup_news()

    scraper4 = Web4()
    articles4 = scraper4.scrape_startup_news()

    # Print the URLs in blue (for debugging purposes)
    print(colored(f"URL1: {url1}", "blue"))
    print(colored(f"URL2: {url2}", "blue"))
    print(colored(f"URL3: {url3}", "blue"))
    print(colored(f"URL4: {url4}", "blue"))

    # Prepare articles for each web source and sanitize the text
    news_array1 = [{'title': sanitize_text(article['title']), 'description': sanitize_text(article['description']), 'url': url1} for article in articles1]
    news_array2 = [{'title': sanitize_text(article['title']), 'description': sanitize_text(article['description']), 'url': url2} for article in articles2]
    news_array3 = [{'title': sanitize_text(article['title']), 'url': url3} for article in articles3]
    news_array4 = [{'title': sanitize_text(article['title']), 'description': sanitize_text(article['description']), 'url': url4} for article in articles4]

    # Combine all articles
    combined_articles = news_array1 + news_array2 + news_array3 + news_array4

    # Create the PDF
    pdf_filename = "tech_news.pdf"  # Define PDF filename
    pdf_gen = PDFGenerator(filename=pdf_filename)

    # Generate PDF with the URL added as text and articles below it
    pdf_gen.create_pdf(combined_articles)

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
