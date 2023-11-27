import json
import base64
import requests
from requests.auth import HTTPBasicAuth
from config import WP_KEY

WP_USER = 'Tom-admin'
WP_URL = 'https://theoryofeverything.info'

class WP():
    def __init__(self, user, url, posts_postfix):
        self.url = url
        self.posts_postfix = posts_postfix
        wp_connection = user + ':' + WP_KEY
        token = base64.b64encode(wp_connection.encode())
        self.auth = HTTPBasicAuth(user, WP_KEY)
        self.headers = {
            'Authorization': 'Basic ' + token.decode('utf-8')
            }

    def get_posts(self):
        api_url = self.url + self.posts_postfix
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def update_post_categories(self, post_id, categories):
        if isinstance(categories,list):
            categories = ','.join(categories)
        r = requests.post(
            self.url + self.posts_postfix + str(post_id),
            headers=self.headers,
            json={'categories': categories})
        return r.json()
