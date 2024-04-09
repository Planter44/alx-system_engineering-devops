#!/usr/bin/python3
"""Task  2 """

def recurse(subreddit, hot_list=[], count=0, after=None):
    """reddit API and returns all hot posts
    of the subreddit"""
    import requests

    subscriber = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if subscriber.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in subscriber.json()
                        .get("data")
                        .get("children")]

    information = subscriber.json()
    if not information.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, information.get("data").get("count"),
                   information.get("data").get("after"))
