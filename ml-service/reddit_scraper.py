import requests
import json
from datetime import datetime, timezone

def scrape_reddit(ticker: str, limit: int = 25) -> list[dict]:
    headers = {"User-Agent": "sentient-dev/0.1"}
    url = f"https://www.reddit.com/r/stocks+investing+wallstreetbets+StockMarket+SecurityAnalysis/search.json"
    params = {
        "q": ticker,
        "sort": "new",
        "limit": limit,
        "type": "link",
        "restrict_sr": "true"
    }
    
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    
    posts = []
    for post in data["data"]["children"]:
        p = post["data"]
        posts.append({
            "id": p["id"],
            "title": p["title"],
            "text": p.get("selftext", ""),
            "score": p["score"],
            "subreddit": p["subreddit"],
            "created_at": datetime.fromtimestamp(p["created_utc"], tz=timezone.utc).isoformat(),
            "url": p["url"],
            "ticker": ticker.upper()
        })
    
    return posts

if __name__ == "__main__":
    ticker = input("Enter a ticker symbol (e.g. AAPL): ")
    print(f"\nFetching Reddit posts about {ticker}...\n")
    posts = scrape_reddit(ticker)
    print(f"Found {len(posts)} posts:\n")
    for p in posts:
        print(f"[{p['subreddit']}] {p['title']}")
        print(f"  Score: {p['score']} | {p['created_at']}\n")

    filename = f"{ticker.upper()}_posts.json"
    with open(filename, "w") as f:
        json.dump(posts, f, indent=2)
    print(f"\nSaved to {filename}")
