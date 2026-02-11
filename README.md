# Encrypt Pipe

A Python data pipeline demonstrating encryption and decryption of sensitive numerical data in CSV files using Fernet symmetric encryption.

## Overview

This repository contains a simple data pipeline that:
1. Generates dummy CSV data with dates, employee IDs, and costs
2. Loads the data into a pandas DataFrame
3. Encrypts the Employee column using cryptographic methods
4. Decrypts the data back to its original form

## Encryption Details

### Fernet Symmetric Encryption

This project uses **Fernet** encryption from the `cryptography` library, which provides:

- **Algorithm**: AES (Advanced Encryption Standard) in CBC mode with a 128-bit key
- **Authentication**: HMAC (Hash-based Message Authentication Code) using SHA256 for message integrity
- **Key Size**: 256-bit URL-safe base64-encoded keys
- **Security Features**:
  - Authenticated encryption (encrypt-then-MAC)
  - Timestamp verification to prevent replay attacks
  - Built-in key derivation using PBKDF2
  - Cryptographically secure random number generation

### How It Works

1. **Key Generation**: A unique 256-bit encryption key is generated using `Fernet.generate_key()`
2. **Encryption Process**: 
   - Each Employee ID is converted to a string and encoded to bytes
   - Fernet encrypts the bytes using AES-128-CBC
   - An HMAC signature is added for authentication
   - The result is base64-encoded for safe storage/transmission
3. **Decryption Process**:
   - The encrypted string is decoded from base64
   - HMAC signature is verified to ensure data integrity
   - Data is decrypted using the same key
   - Result is converted back to the original integer format

### Security Considerations

- **Symmetric Encryption**: The same key is used for both encryption and decryption, so the key must be kept secure
- **Key Storage**: In production, keys should be stored securely (e.g., environment variables, key management services)
- **Key Rotation**: For enhanced security, keys should be rotated periodically
- **Data at Rest**: This implementation encrypts specific columns while keeping others in plaintext

## Files

- **`generate_data.py`**: Generates dummy CSV data with 10 rows
- **`dummy_pipe.py`**: Main pipeline with encryption/decryption functions
- **`dummy_data.csv`**: Sample data file (generated)
- **`requirements.txt`**: Python dependencies

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Generate Dummy Data
```bash
python generate_data.py
```

### Run the Encryption Pipeline
```bash
python dummy_pipe.py
```

This will:
1. Load the CSV data
2. Display the original DataFrame
3. Encrypt the Employee column
4. Display the encrypted DataFrame
5. Show the encryption key
6. Decrypt the data back to original form
7. Display the decrypted DataFrame

## Dependencies

- **pandas**: Data manipulation and CSV handling
- **cryptography**: Fernet encryption implementation

## Example Output

**Original Data:**
```
         Date  Employee    Cost
0  2025-01-16     10003  520.30
1  2025-09-15     10004  879.70
```

**Encrypted Data:**
```
         Date                                           Employee    Cost
0  2025-01-16  gAAAAABpjFYUKwtphWwquz7486lH9qEUg7-1KaqnxoffIl...  520.30
1  2025-09-15  gAAAAABpjFYUh7PWAFKaxi73XeWhZ07wNwbFuqX7WHjw2U...  879.70
```

**Decrypted Data:**
```
         Date  Employee    Cost
0  2025-01-16     10003  520.30
1  2025-09-15     10004  879.70
```

## License

This is a demonstration project for educational purposes.
