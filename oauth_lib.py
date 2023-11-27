import requests
from requests_oauthlib import OAuth2Session
import config

# Set your OAuth2 client ID and client secret
client_id = config.CLIENT_ID
client_secret = config.CLIENT_SECRET
authorization_base_url = 'https://public-api.wordpress.com/oauth2/authorize'
token_url = 'https://moonytunes.com/wp-json/oauth2/token'

# Create OAuth2 session
oauth = OAuth2Session(client_id, redirect_uri='https://your-redirect-uri.com')

# Redirect user for authorization
authorization_url, state = oauth.authorization_url(authorization_base_url)

# Get authorization response (assuming it's redirected to your redirect_uri)
redirect_response = input('Paste the full redirect URL here: ')
token = oauth.fetch_token(token_url, authorization_response=redirect_response, client_secret=client_secret)

# Use the obtained token for API requests
api_url = 'moonytunes.com/wp-json/wp/v2/posts'
headers = {'Authorization': 'Bearer ' + token['access_token']}
response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Process data here
    print(data)
else:
    print('Error:', response.status_code, response.text)
