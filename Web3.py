# Web3 = https://techcrunch.com/category/startups/
import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Web3:
    URL = "https://techcrunch.com/category/startups/"  # Replace with the actual URL

    def scrape_startup_news(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='loop-card__content')

        # Get today's date in the compatible format for comparison
        today_date = datetime.now().date()
        # print(f"Today's date: {today_date}")  # Debug print to check today's date

        articles_today = []

        for article in articles:
            # Extract the category (y) and ensure it exists
            category_tag = article.find('div', class_='loop-card__cat-group')
            category = category_tag.find('a').text.strip() if category_tag and category_tag.find('a') else None

            # Continue only if the category matches "Startups"
            if category != "Startups":
                continue

            # Extract the article's date in ISO format
            time_tag = article.find('time', class_='loop-card__meta-item loop-card__time wp-block-tc23-post-time-ago')
            article_date_str = time_tag['datetime'] if time_tag else None

            if article_date_str:
                # Convert the article's date to a date object
                article_date = datetime.fromisoformat(article_date_str).date()
                # print(f"Article date: {article_date}")  # Debug print to check each article date

                # Check if the article date matches today's date
                if article_date == today_date:
                    # Extract title and link
                    title_tag = article.find('h3', class_='loop-card__title')
                    title = title_tag.find('a').text.strip() if title_tag and title_tag.find('a') else 'No Title'
                    link = title_tag.find('a')['href'] if title_tag and title_tag.find('a') else None

                    # Append article details to the list
                    articles_today.append({
                        'title': title,
                        'link': link,
                        'category': category,
                        'date': article_date_str
                    })

        # Return today's articles or an empty list if none match
        return articles_today
