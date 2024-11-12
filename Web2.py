import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Web2:
    URL = "https://techfundingnews.com/category/ai/"

    def scrape_startup_news(self):
        response = requests.get(self.URL)
        if response.status_code != 200:
            return []  # No need to print an error, just return empty list if failure

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='cs-entry__outer')

        today_date = datetime.now()
        today_date_str = today_date.strftime('%B %d, %Y').replace(" 0", " ")

        articles_today = []

        for article in articles:
            # Extract the article date if available
            date_tag = article.find('div', class_='cs-entry__post-meta')
            if date_tag:
                date_element = date_tag.find('div', class_='cs-meta-date')
                article_date_str = date_element.text.strip() if date_element else None
            else:
                article_date_str = None

            # Only proceed if article date matches today's date
            if article_date_str == today_date_str:
                # Extract title
                title_tag = article.find('h6', class_='cs-entry__title')
                title = title_tag.find('a').text.strip() if title_tag and title_tag.find('a') else None

                # Extract description if available
                description_tag = article.find('div', class_='cs-entry__excerpt')
                description = description_tag.text.strip() if description_tag else None

                # Only add articles to the list if title is present
                if title:
                    articles_today.append({
                        'title': title,
                        'description': description,
                        'date': article_date_str
                    })

        return articles_today
