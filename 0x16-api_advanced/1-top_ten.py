#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.

Requirements:

Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
            "User-Agent": "My Reddit API Client"
            }
    response = requests.get(url, headers=headers)
    data = response.json()
    if response.status_code != 200:
        print('None')
    else:
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
