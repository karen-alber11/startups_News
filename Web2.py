import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Web2:
    URL = "https://techfundingnews.com/category/ai/"

    def scrape_startup_news(self):
        response = requests.get(self.URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('div', class_='cs-entry__outer')

        today_date = datetime.now().date()  # Get today's date
        today_date_str = today_date.strftime('%B %d, %Y')  # Get today's date in format like 'November 6, 2024'
        # Strip leading zero from day if exists
        today_date_str = today_date_str.replace(' 0', ' ')  # Replace ' 0' with space to remove the leading zero

        articles_today = []

        for article in articles:
            # Extract the article date
            date_tag = article.find('div', class_='cs-entry__post-meta')
            if date_tag:
                article_date_str = date_tag.find('div', class_='cs-meta-date')
                if article_date_str:
                    article_date_str = article_date_str.text.strip()
                else:
                    continue  # Skip if no date is found
            else:
                continue  # Skip if no date is found

            # Compare the article date with today's adjusted date
            if article_date_str == today_date_str:
                # Extract the article details
                title_tag = article.find('h2', class_='cs-entry__title')
                title = title_tag.find('a').text.strip() if title_tag else 'No Title'
                description = article.find('div', class_='cs-entry__excerpt').text.strip() if article.find('div', class_='cs-entry__excerpt') else 'No Description'

                # Skip articles with "No Title" and "No Description"
                if title == 'No Title' and description == 'No Description':
                    continue

                # Append article details to the list
                articles_today.append({
                    'title': title,
                    'description': description,
                    'date': article_date_str
                })

        # Return an empty list if no articles are found
        return articles_today
