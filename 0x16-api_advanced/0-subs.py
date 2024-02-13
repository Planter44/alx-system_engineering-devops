#!/usr/bin/python3
"""Task 0"""


def number_of_subscribers(subreddit):
    """Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    subscriber = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subscriber.status_code >= 300:
        return 0

    return subscriber.json().get("data").get("subscribers")
