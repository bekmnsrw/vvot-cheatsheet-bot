from base64 import b64encode

def encode_to_base64(bytes):
    return b64encode(bytes).decode("utf-8")