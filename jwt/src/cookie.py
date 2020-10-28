import jwt

def generate_jwt(payload, key):
    return jwt.encode(payload, key=key, algorithm="HS256").decode()

def verify_jwt(mtext, key):
    return jwt.decode(mtext, key=key, algorithm="HS256")
