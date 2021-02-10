from django.conf import settings
import jwt
import datetime

def access_token(user):
    token_payload={
                'username':user.username,
                'exp':datetime.datetime.utcnow() + datetime.timedelta(days=0,minutes=15),
                'iat':datetime.datetime.utcnow(),
            }
    access_token=jwt.encode(token_payload,settings.SECRET_KEY,algorithm='HS256')
    return access_token
def refresh_token(user):
    token_payload={
                'username':user.username,
                'exp':datetime.datetime.utcnow() + datetime.timedelta(days=0,minutes=20),
                'iat':datetime.datetime.utcnow(),
            }
    refresh_token=jwt.encode(token_payload,settings.JWT_REFRESH_KEY,algorithm='HS256')
    return refresh_token
