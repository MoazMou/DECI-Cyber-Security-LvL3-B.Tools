import hashlib

def create_a_password():
    while True:
        your_password = input("[*] Create a password: ").encode()
        confirm_your_password = input("[*] Confirm your password: ").encode()
    
        if your_password == confirm_your_password:
            hash_your_password = hashlib.sha256(your_password).hexdigest()
            with open("password.rfp", "w") as file:
                file.write(hash_your_password)
            print("\n[:)] Password has been created!")
            login()
            break
        else:
            print("\n[:(] Error, please check your password")

def login():
    with open("password.rfp", "r") as file:
        stored_password = file.read().strip()

    while True:
        value = input("[*] Enter your password: ").encode()
        if hashlib.sha256(value).hexdigest() == stored_password:
            print("\n[:)] Login successful!")
            break
        else:
            print("\n[:(] Incorrect password. Try again.")

create_a_password()