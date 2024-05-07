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

    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "custom"},
    )

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
