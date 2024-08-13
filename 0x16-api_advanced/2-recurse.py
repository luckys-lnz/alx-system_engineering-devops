#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and
returns the list of hot articles for a given subreddit.
"""

import requests
import sys
import time


def recurse(subreddit, hot_list=[]):
    """Recursively fetch all hot articles and their titles from a subreddit."""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'my_reddit_app'}

    try:
        # Fixed URL and parameter name
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            # Added code to properly extend hot_list with titles
            for post in posts:
                hot_list.append(post['data']['title'])

            # Check for 'after' to handle pagination
            after = data['data'].get('after')

            if after:
                # Recursive call with updated hot_list
                return recurse(subreddit, hot_list)
            else:
                # No more pages, return the hot_list
                return hot_list

        elif response.status_code == 404:
            # Handle invalid subreddit
            print("Invalid subreddit.")
            return None

        elif response.status_code == 429:
            # Handle rate limiting
            print("Rate limit exceeded. Retrying after 60 seconds.")
            time.sleep(60)  # Wait 60 seconds before retrying
            return recurse(subreddit, hot_list)

        else:
            # Handle other HTTP errors
            print("Error: HTTP status code {}".format(response.status_code))
            return None

    except Exception as e:
        # Handle exceptions and print errors
        print("Exception: {}".format(e))
        return None
