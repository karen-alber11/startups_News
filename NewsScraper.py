import requests
from bs4 import BeautifulSoup
from fpdf import FPDF


class NewsScraper:
    def __init__(self, url="https://economictimes.indiatimes.com/tech/startups"):
        self.url = url

    def get_startup_news(self):
        # Request and parse the webpage
        try:
            req = requests.get(self.url)
            req.raise_for_status()  # Raise an error for bad responses

            soup = BeautifulSoup(req.text, "html.parser")

            # List to store articles
            articles = []

            # Adjusted selectors based on the actual HTML structure
            for article in soup.find_all('div', class_='some-actual-class-name'):  # Replace with actual class name
                title = article.find('h3').text.strip() if article.find('h3') else "No title"
                content = article.find('p').text.strip() if article.find('p') else "No content available"
                url = article.find('a')['href'] if article.find('a') else "No URL"
                time_posted = "Time not available"  # You can adjust this if time data is available

                # Append the article to the list
                articles.append({
                    "title": title,
                    "content": content,
                    "url": url,
                    "time_posted": time_posted
                })

                print(f"Title: {title}\nContent: {content}\nURL: {url}\nPosted: {time_posted}\n")  # Debug print

            return articles

        except requests.RequestException as e:
            print(f"Error fetching the news: {e}")
            return []

    def save_to_pdf(self, articles):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for news in articles:
            pdf.cell(0, 10, f"Title: {news['title']}", ln=True)
            pdf.cell(0, 10, f"URL: {news['url']}", ln=True)
            pdf.multi_cell(0, 10, f"Summary: {news['content']}")
            pdf.cell(0, 10, f"Posted: {news['time_posted']}", ln=True)
            pdf.cell(0, 10, '', ln=True)  # Add a blank line between articles

        pdf_file_path = "startup_news.pdf"
        pdf.output(pdf_file_path)
        print(f"Articles saved to {pdf_file_path}")


# Example usage
if __name__ == "__main__":
    scraper = NewsScraper()
    startup_news = scraper.get_startup_news()
    if startup_news:
        scraper.save_to_pdf(startup_news)
