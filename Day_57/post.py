import requests


class Post:
    def __init__(self):
        self.URL="https://api.npoint.io/c790b4d5cab58020d391"

    def posts_get(self):
        resources = requests.get(self.URL)
        resources.raise_for_status()

        all_posts = resources.json()
        return all_posts
