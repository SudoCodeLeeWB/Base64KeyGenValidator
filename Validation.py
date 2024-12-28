# Validation.py
import base64
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

def validate_key(private_key_pem, public_key_pem):
    # Test string to sign
    test_string = b"This is a test string for validation."

    # Load private key
    private_key = serialization.load_pem_private_key(
        private_key_pem,
        password=None,
    )

    # Create a signature
    signature = private_key.sign(
        test_string,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    # Load public key
    public_key = serialization.load_pem_public_key(
        public_key_pem,
    )

    # Verify the signature
    try:
        public_key.verify(
            signature,
            test_string,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Validation failed: {e}")
        return False

def validate_base64_encode(base64_encoded_data, original_data):
    # Decode Base64 data
    decoded_data = base64.b64decode(base64_encoded_data)

    # Compare with original data
    return decoded_data == original_data
