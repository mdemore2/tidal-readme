import tidalapi

session = tidalapi.Session()
login, future = session.login_oauth()
print(login.verification_uri_complete)

future.result()

token_type = session.token_type
access_token = session.access_token
refresh_token = session.refresh_token # Not needed if you don't care about refreshing
expiry_time = session.expiry_time

print("TOKEN_TYPE=", token_type)
print("ACCESS_TOKEN=", access_token)
print("REFRESH_TOKEN=", refresh_token)
print("EXPIRY_TIME:=", expiry_time)
