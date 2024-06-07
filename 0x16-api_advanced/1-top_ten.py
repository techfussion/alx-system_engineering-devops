#!/usr/bin/python3
"""a Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "CustomUserAgent/1.0"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(chi.get("data").get("title")) for chi in results.get("children")]
