#!/usr/bin/python3
""" Task  1"""

def top_ten(subreddit):
    """Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    subscriber = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subscriber.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in subscriber.json().get("data").get("children")]
