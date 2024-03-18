import requests


class Post:
    def __init__(self):
        self.URL="https://api.npoint.io/5808b1a3304a496f4c65"

    def posts_get(self):
        resources = requests.get(self.URL)
        resources.raise_for_status()

        all_posts = resources.json()
        return all_posts
