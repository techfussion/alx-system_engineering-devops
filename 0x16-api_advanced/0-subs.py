#!/usr/bin/python3
"""Fetch subreddit subs"""
import requests


def number_of_subscribers(subreddit):
    """Fetch reddit subs"""
    url = f'https://api.reddit.com/r/{subreddit}/about'
    headers = {'User-Agent': 'gritnec'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json() or {}
        return data.get('data', {}).get('subscribers', 0)
    return 0
