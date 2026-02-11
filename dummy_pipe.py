# A dummy pipeline to load and encrypt/decrypt data

import pandas as pd
from cryptography.fernet import Fernet

def read_data(filename='dummy_data.csv'):
    try:
        df = pd.read_csv(filename)
        print("Data loaded successfully:")
        print(df)
        return df
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None

def encrypt_employee_column(df):
    """Encrypt the Employee column values."""
    # Generate a key for encryption
    key = Fernet.generate_key()
    cipher = Fernet(key)
    
    # Create a copy of the dataframe
    df_encrypted = df.copy()
    
    # Encrypt each Employee value
    df_encrypted['Employee'] = df_encrypted['Employee'].apply(
        lambda x: cipher.encrypt(str(x).encode()).decode()
    )
    
    print("\nEncrypted DataFrame:")
    print(df_encrypted)
    
    return df_encrypted, key

def decrypt_employee_column(df_encrypted, key):
    """Decrypt the Employee column values."""
    cipher = Fernet(key)
    
    # Create a copy of the dataframe
    df_decrypted = df_encrypted.copy()
    
    # Decrypt each Employee value
    df_decrypted['Employee'] = df_decrypted['Employee'].apply(
        lambda x: int(cipher.decrypt(x.encode()).decode())
    )
    
    print("\nDecrypted DataFrame:")
    print(df_decrypted)
    
    return df_decrypted

if __name__ == "__main__":
    df = read_data()
    if df is not None:
        encrypted_df, encryption_key = encrypt_employee_column(df)
        print(f"\nEncryption key (save this to decrypt later): {encryption_key.decode()}")
        
        # Demonstrate decryption
        decrypted_df = decrypt_employee_column(encrypted_df, encryption_key)

