import snscrape.modules.twitter as sntwitter
import pandas as pd
import json
from pathlib import Path

def scrape_tweets(query, limit=100):
    """
    Scrape tweets for bias analysis using SNScrape
    """
    tweets = []
    try:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
            if i >= limit:
                break
            tweets.append({
                "date": tweet.date.isoformat(),
                "content": tweet.content,
                "url": tweet.url
            })
        return tweets
    except Exception as e:
        print(f"Error scraping tweets: {e}")
        return []

def save_tweets(tweets, filename):
    """Save tweets to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(tweets, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    # Example queries for bias analysis
    queries = [
        "2008 financial crisis",
        "vaccine conspiracy",
        "political polarization"
    ]
    
    data_dir = Path("data/social")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    for query in queries:
        print(f"Scraping tweets for: {query}")
        tweets = scrape_tweets(query, limit=50)
        filename = data_dir / f"{query.replace(' ', '_')}_tweets.json"
        save_tweets(tweets, filename)
        print(f"Saved {len(tweets)} tweets to {filename}")
