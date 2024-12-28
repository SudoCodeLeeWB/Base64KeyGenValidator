# main.py
import os
from PrivateKeyGenerator import PrivateKeyGenerator
from PublicKeyGenerator import PublicKeyGenerator
from Base64Encoder import Base64Encoder
from Validation import validate_key, validate_base64_encode

def save_to_file(filename, data):
    # Ensure the PemFiles directory exists
    os.makedirs("PemFiles", exist_ok=True)
    file_path = os.path.join("PemFiles", filename)
    with open(file_path, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    # Generate private key
    private_key = PrivateKeyGenerator.generate_private_key()
    private_pem = PrivateKeyGenerator.serialize_private_key(private_key)

    # Generate public key
    public_key = PublicKeyGenerator.generate_public_key(private_key)
    public_pem = PublicKeyGenerator.serialize_public_key(public_key)

    # Encode keys in Base64
    private_base64 = Base64Encoder.encode_base64(private_pem)
    public_base64 = Base64Encoder.encode_base64(public_pem)

    # Save keys to files
    save_to_file("private_key.pem", private_pem.decode('utf-8'))
    save_to_file("public_key.pem", public_pem.decode('utf-8'))
    save_to_file("private_key_base64.txt", private_base64)
    save_to_file("public_key_base64.txt", public_base64)

    # Validate keys
    print("Validating keys...")
    if validate_key(private_pem, public_pem):
        print("Key validation successful.")
    else:
        print("Key validation failed.")

    # Validate Base64 encoding
    print("Validating Base64 encoding...")
    if validate_base64_encode(private_base64, private_pem):
        print("Private key Base64 validation successful.")
    else:
        print("Private key Base64 validation failed.")

    if validate_base64_encode(public_base64, public_pem):
        print("Public key Base64 validation successful.")
    else:
        print("Public key Base64 validation failed.")

    print("Keys generated and saved:")
    print("Private Key (PEM): PemFiles/private_key.pem")
    print("Public Key (PEM): PemFiles/public_key.pem")
    print("Private Key (Base64): PemFiles/private_key_base64.txt")
    print("Public Key (Base64): PemFiles/public_key_base64.txt")
