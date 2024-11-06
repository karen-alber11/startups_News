# Web5 = https://inc42.com/buzz/
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Web5:
    URL = "https://technode.com/"  # Replace with the actual URL

    def scrape_startup_news(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='entry-wrapper')

        # Get today's date in the compatible format for comparison
        today_date = datetime.now().strftime("%b %d, %Y").replace(" 0", " ")
        # print(f"Today's date (formatted): {today_date}")  # Debug print

        articles_today = []

        for article in articles:
            # Extract the title (x) and ensure it exists
            title_tag = article.find('h3', class_='entry-title')
            title = title_tag.find('a').text.strip() if title_tag and title_tag.find('a') else 'No Title'

            # Extract the article's date
            time_tag = article.find('time', class_='entry-date published')
            article_date_str = time_tag.text.strip() if time_tag else None

            if article_date_str:
                # Format article date to match today's date format for comparison
                article_date = datetime.strptime(article_date_str, "%b %d, %Y").strftime("%b %d, %Y").replace(" 0", " ")
                # print(f"Article date (formatted): {article_date}")  # Debug print

                # Check if the article date matches today's date
                if article_date == today_date:
                    # Append article details to the list
                    articles_today.append({
                        'title': title,
                        'date': article_date_str
                    })

        # Return today's articles or an empty list if none match
        return articles_today

