# Web1 = https://economictimes.indiatimes.com/tech/startups
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Web1:
    URL = "https://economictimes.indiatimes.com/tech/startups"

    def scrape_startup_news(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='story-box clearfix')

        today_date = datetime.now().date()  # Get today's date
        articles_today = []

        for story_box in articles:
            # Extract the article date
            article_date_str = story_box.find('time', class_='date-format')['data-time']
            article_date = datetime.strptime(article_date_str, '%b %d, %Y, %I:%M %p IST').date()

            # Check if the article date matches today's date
            if article_date == today_date:
                title = story_box.find('h4').text
                link = story_box.find('a')['href']
                description = story_box.find('p').text
                # Append article details as a dictionary to the list
                articles_today.append({
                    'title': title,
                    'link': link,
                    'description': description,
                    'date': article_date_str
                })

        return articles_today
