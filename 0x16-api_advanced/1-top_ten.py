#!/usr/bin/python3

"""
function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit.
If an invalid subreddit is given, the function should print None.
"""

import requests


def top_ten(subreddit):
    """
    return first 10 hot posts of a subreddit
    ex:
    reddit = top_ten('redditdev')
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    req = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
    )

    if req.status_code == 200:
        for post in req.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)
