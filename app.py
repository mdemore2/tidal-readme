import os
import base64
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests
import tidalapi
from datetime import date, timedelta
from tidalapi.page import PageItem, PageLink
from tidalapi.mix import Mix

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")

token_type = os.getenv("TOKEN_TYPE")
access_token = os.getenv("ACCESS_TOKEN")
refresh_token = os.getenv("REFRESH_TOKEN")
expiry_time = os.getenv("EXPIRY_TIME")

session = tidalapi.Session()
session.load_oauth_session(token_type,access_token,refresh_token,expiry_time)

home = session.home()
#home.categories.extend(session.explore().categories)
#home.categories.extend(session.videos().categories)

prev = date.today().replace(day=1) - timedelta(days=1)
print(prev.year)
print(prev.month)

for category in home.categories:
    print(category.title)
    if category.title == "Your listening history":
        print("in match")
        for item in category.items:
            if isinstance(item, Mix):
                print(item.title)





#api_url = "https://openapi.tidal.com/v2"
#
#client = BackendApplicationClient(client_id=client_id)
#oauth = OAuth2Session(client=client)
#
#token = oauth.fetch_token(token_url='https://auth.tidal.com/v1/oauth2/token', client_id=client_id,
#        client_secret=client_secret)
##print(token)
#
#
#resp = oauth.get("https://openapi.tidal.com/v2/albums/370954635?countryCode=US")
#print(resp)
#
#
#sess = tidalapi.Session()
#login, future = sess.login_oauth()
#print(login.verification_uri_complete)
#time.sleep(60)
#
#
#resp = oauth.get("https://openapi.tidal.com/v2/users/37227871")
#print(resp.content)
#
#resp = oauth.get("https://openapi.tidal.com/v2/users/37227871/relationships/publicProfile?locale=en-US")
#print(resp.content)
