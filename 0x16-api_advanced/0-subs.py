#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests,
ensure you’re setting a custom User-Agent.

Requirements:

Prototype: def number_of_subscribers(subreddit)
If not a valid subreddit, return 0.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a subreddit
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "An API Client"
            }
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code != 200:
        return 0
    else:
        subscribers = data['data']['subscribers']
    return subscribers
