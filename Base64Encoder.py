# Base64Encoder.py
import base64

class Base64Encoder:
    @staticmethod
    def encode_base64(data):
        return base64.b64encode(data).decode('utf-8')
