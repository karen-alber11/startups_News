import requests
from bs4 import BeautifulSoup
from datetime import datetime


class Web4:
    # Set the Web4 URL
    URL = "https://disruptafrica.com/category/startups/"

    def scrape_startup_news(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(self.URL, headers=headers)

        # Check if the page loads successfully
        if response.status_code != 200:
            print(f"Failed to retrieve page. Status code: {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = soup.find_all('article', class_='l-post list-post list-post-on-sm m-pos-left')

        today_date = datetime.now().date()  # Get today's date in yyyy-mm-dd format
        # print(f"Today's Date (yyyy-mm-dd): {today_date}")  # Print today's date

        articles_today = []

        for article in articles:
            # Extract title from <h2 class="is-title post-title"><a> x </a></h2>
            title_tag = article.find('h2', class_='is-title post-title')
            title = title_tag.find('a').text if title_tag else 'No title'
            link = title_tag.find('a')['href'] if title_tag else '#'

            # Extract description from <div class="excerpt"><p> y </p></div>
            description_tag = article.find('div', class_='excerpt')
            description = description_tag.find('p').text if description_tag else 'No description'

            # Extract the date from href URL in the <a href="https://disruptafrica.com/yyyy/mm/dd/title/"> link
            date_str = link.split('/')[3:6]  # Extract date as [yyyy, mm, dd]
            article_date = datetime.strptime("/".join(date_str), '%Y/%m/%d').date()  # Convert to date object

            # print(f"Extracted article date (yyyy-mm-dd): {article_date}")  # Print the extracted article date

            # Compare the article date with today's date
            if article_date == today_date:
                articles_today.append({
                    'title': title,
                    'link': link,
                    'description': description,
                    'date': article_date
                })

        # Print the articles found for today
        # print("Today's Articles:", articles_today)
        return articles_today

