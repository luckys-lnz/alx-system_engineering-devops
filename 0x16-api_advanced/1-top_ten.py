#!/usr/bin/python3
"""Prints the titles of the first 10 post listed for a given subreddit."""

import requests
import sys


def top_ten(subreddit):
    """Return the top_ten hot post in a subbredit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    try:
        headers = {'User-Agent': 'my-reddit-app'}
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            print("success: {}\n".format(response.status_code))
            data = response.json()
            posts = data['data']['children']

            # iterate on the post to get the top 10 post in the subreddit
            for post in posts[:10]:
                print(post['data']['title'])
        else:
            print("chack your url or data you are trying to access")
            return 0

    except Exception as e:
        print("Exception: ".format(e))
        return 0
