import os
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session


load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
user_id = os.getenv("USER_ID")



api_url = "https://openapi.tidal.com/v2"

client = BackendApplicationClient(client_id=client_id)

oauth = OAuth2Session(client=client)

token = oauth.fetch_token(token_url='https://auth.tidal.com/v1/oauth2/token', client_id=client_id,
        client_secret=client_secret)

print(token)

resp = oauth.get(f"{api_url}/users/{user_id}/relationships/publicProfile")
print(resp)