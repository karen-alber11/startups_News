import tweepy
from datetime import datetime

class Jawlah:
    def __init__(self, api_key, api_key_secret, access_token, access_token_secret):
        # Authenticate
        self.auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)
        self.today = datetime.now().date()

    def fetch_today_posts(self, username):
        try:
            tweets = self.api.user_timeline(screen_name=username, tweet_mode="extended", count=100)
            today_posts = [tweet.full_text for tweet in tweets if tweet.created_at.date() == self.today]
            return today_posts
        except tweepy.errors.Unauthorized:
            print("Error: Unauthorized. Please check your API credentials.")
            return []
        except tweepy.errors.Forbidden:
            print("Error: Forbidden. You may not have permission to access this resource.")
            return []
        except tweepy.TweepyException as e:
            print(f"Error fetching tweets: {e}")
            return []
