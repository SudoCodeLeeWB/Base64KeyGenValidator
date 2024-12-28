# RSA Key Generator and Validator

## Description
This project generates RSA private and public keys, encodes them in PEM and Base64 formats, and validates their integrity. It also provides utilities for signing and verifying test data using the generated keys.

## Prerequisites
Ensure you have Python 3.7+ installed. Install the required dependencies using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## File Structure
```
.
├── Base64Encoder.py         # Handles Base64 encoding
├── PrivateKeyGenerator.py   # Generates private keys
├── PublicKeyGenerator.py    # Generates public keys
├── Validation.py            # Validates keys and Base64 encoding
├── main.py                  # Main script for key generation and validation
├── PemFiles/                # Directory for storing generated keys
├── requirements.txt         # Dependency management
└── README.md                # Project instructions
```

## Usage
1. Run the `main.py` script to generate keys, encode them in Base64, and validate them:

```bash
python main.py
```

2. The generated files will be saved in the `PemFiles/` directory:
   - `private_key.pem`: Private key in PEM format
   - `public_key.pem`: Public key in PEM format
   - `private_key_base64.txt`: Private key encoded in Base64
   - `public_key_base64.txt`: Public key encoded in Base64

## Validation
The project automatically validates:
- The integrity of the private and public keys using a signing and verification process.
- The accuracy of Base64 encoding and decoding by comparing the decoded content with the original.

## Contributions
Feel free to fork this repository and submit pull requests for improvements.


---
This README and the project structure were generated with the help of OpenAI's GPT model for quick and efficient setup.
