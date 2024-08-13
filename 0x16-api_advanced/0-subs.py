#!/usr/bin/python3
"""A script that gets the subscribers of a subreddit."""

import requests
import sys


def number_of_subscribers(subreddit):
    """Return the total number_of_subscribers of a subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        headers = {'User-Agent': 'my-reddit-app'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            print("status: {}".format(response.status_code))
            data = response.json()
            return data['data']['subscribers']
        else:
            print("Please check the Url")
            return 0

    except Exception as e:
        print("Exception: {}".format(e))
        return 0
