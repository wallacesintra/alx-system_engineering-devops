#!/usr/bin/python3

"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""


import requests


def number_of_subscribers(subreddit):
    """
    return the number of subscribers
    ex:
    reddit = number_of_subscribers('redditdev')
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77\
               Safari/537.36"}
    req = requests.get(
        url,
        headers=headers,
        allow_redirects=False
    )

    if req.status_code != 200:
        return 0

    data = req.json()['data']
    return data['subreddit_subscribers']
