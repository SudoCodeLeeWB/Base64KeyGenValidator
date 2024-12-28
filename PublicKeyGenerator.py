# PublicKeyGenerator.py
from cryptography.hazmat.primitives import serialization

class PublicKeyGenerator:
    @staticmethod
    def generate_public_key(private_key):
        return private_key.public_key()

    @staticmethod
    def serialize_public_key(public_key):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
