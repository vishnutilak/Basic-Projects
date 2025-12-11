import json, base64, hmac, hashlib
from time import time

def _b64u(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()

def _b64ud(s: str) -> bytes:
    padding = '=' * (-len(s) % 4)
    return base64.urlsafe_b64decode(s + padding)

def jwt_encode(payload: dict, secret: str, alg='HS256', exp_seconds=900):
    header = {"alg": alg, "typ": "JWT"}
    payload = payload.copy()
    payload['iat'] = int(time())
    payload['exp'] = payload['iat'] + exp_seconds
    s = _b64u(json.dumps(header, separators=(',',':')).encode()) + "." + _b64u(json.dumps(payload, separators=(',',':')).encode())
    sig = hmac.new(secret.encode(), s.encode(), hashlib.sha256).digest()
    return s + "." + _b64u(sig)

def jwt_decode(token: str, secret: str):
    header_b64, payload_b64, sig_b64 = token.split('.')
    s = header_b64 + "." + payload_b64
    expected = _b64u(hmac.new(secret.encode(), s.encode(), hashlib.sha256).digest())
    if not hmac.compare_digest(expected, sig_b64):
        raise ValueError("Invalid signature")
    payload = json.loads(_b64ud(payload_b64))
    if payload.get('exp',0) < int(time()):
        raise ValueError("Token expired")
    return payload

# example:
# t = jwt_encode({"user":1}, "s3cr3t"); print(jwt_decode(t,"s3cr3t"))
