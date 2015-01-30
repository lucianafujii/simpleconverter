import base64
import hmac, hashlib
from .config import policy_document, s3_secret_key

def policy():
    return base64.b64encode(str(policy_document))

def signature():
    policy = base64.b64encode(str(policy_document))
    return base64.b64encode(hmac.new(
        s3_secret_key,
        policy,
        hashlib.sha1).digest())

