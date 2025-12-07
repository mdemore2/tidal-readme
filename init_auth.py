import tidalapi

session = tidalapi.Session()
login, future = session.login_oauth()
print(login.verification_uri_complete)

future.result()

token_type = session.token_type
access_token = session.access_token
# Not needed if you don't care about refreshing
refresh_token = session.refresh_token
expiry_time = session.expiry_time

print("TOKEN_TYPE=", token_type)
print("ACCESS_TOKEN=", access_token)
print("REFRESH_TOKEN=", refresh_token)
print("EXPIRY_TIME=", expiry_time)

with open(".env", "w") as f:
    f.write(f"TOKEN_TYPE={token_type}\n")
    f.write(f"ACCESS_TOKEN={access_token}\n")
    f.write(f"REFRESH_TOKEN={refresh_token}\n")
    f.write(f"EXPIRY_TIME={expiry_time}\n")
