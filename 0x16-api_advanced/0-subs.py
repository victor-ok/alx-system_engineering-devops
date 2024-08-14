# #!/usr/bin/python3
# """Function to query subscribers on a given Reddit subreddit."""
# import requests


# def number_of_subscribers(subreddit):
#     """Return the total number of subscribers on a given subreddit."""
#     url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
#     headers = {
#         "User-Agent": "my bot 0.1"
#     }
#     response = requests.get(url, headers=headers, allow_redirects=False)
#     if response.status_code == 404:
#         return 0
#     results = response.json().get("data")
#     return results.get("subscribers")

#!/usr/bin/python3
"""
module for number of subscribers for subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers for subreddit
    """
    results = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={'User-agent': 'my bot 0.1'})

    if results.status_code == 200:
        response_data = results.json()
        subscribers = response_data['data']['subscribers']
        return subscribers
    else:
        return 0
 