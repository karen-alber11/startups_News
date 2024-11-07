import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Web6:
    URL = "https://venturebeat.com/category/ai/"  # Replace with the actual URL

    def scrape_startup_news(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='ArticleListing')

        # Get today's date in the compatible format for comparison
        today_date = datetime.now().strftime("%B %d, %Y")
        print(f"Today's date: {today_date}")  # Debug print to check today's date

        articles_today = []

        for article in articles:
            # Extract the title and ensure it exists
            title_tag = article.find('h2', class_='ArticleListing__title')
            title = title_tag.find('a').text.strip() if title_tag and title_tag.find('a') else 'No Title'

            # Extract the article's date
            time_tag = article.find('time', class_='ArticleListing__time')
            article_date_str = time_tag.text.strip() if time_tag else None

            if article_date_str:
                # Convert the article's date to the desired format
                article_date = datetime.strptime(article_date_str, "%B %d, %Y %I:%M %p").strftime("%B %d, %Y")
                print(f"Article date: {article_date}")  # Debug print to check article date

                # Check if the article date matches today's date
                if article_date == today_date:
                    # Append article details to the list
                    articles_today.append({
                        'title': title,
                        'date': article_date_str
                    })

        # Return today's articles or an empty list if none match
        return articles_today
