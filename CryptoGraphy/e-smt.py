from cryptography.fernet import Fernet

def encrypt_data():
    global encrypt_text, key
    key = Fernet.generate_key()
    cipher = Fernet(key)

    message = input("\n[+] Enter your message: ")
    encrypt_text = cipher.encrypt(message.encode())

    print(f"\n[*] Key: {key.decode()}") 
    print(f"[*] Encrypted Data: {encrypt_text.decode()}")
    decrypt_data()

def decrypt_data():
    global encrypt_text, key
    key_input = input("\n[+] Enter the key: ").encode()
    
    try:
        cipher = Fernet(key_input)
        decrypt_text = cipher.decrypt(encrypt_text).decode()  
        print(f"\n[*] Decrypted Data: {decrypt_text}")
        encrypt_data
    except Exception as e:
        print("\n[X] Wrong key or decryption error!")
        decrypt_data()

encrypt_data()