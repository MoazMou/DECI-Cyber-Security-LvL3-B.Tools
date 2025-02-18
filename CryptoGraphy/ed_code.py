from cryptography.fernet import Fernet
import subprocess
import colorama
import time

class bcolors():
    RED = colorama.Fore.RED
    BLUE = colorama.Fore.BLUE
    GREEN = colorama.Fore.GREEN
    WHITE = colorama.Fore.WHITE
    YELLOW = colorama.Fore.YELLOW

def encrypt_option(plain_text):
    try:
        subprocess.run("cls", shell=True)
        key_data = Fernet.generate_key()
        key = Fernet(key_data)

        with open("key.key", "w") as file:
            file.write(key_data.decode())
            
        encryption = key.encrypt(plain_text)
        print(f"\n[{bcolors.BLUE}+{bcolors.WHITE}] Plain text: {plain_text}")
        print(f"\n[{bcolors.GREEN}${bcolors.WHITE}] Encryption text: {encryption.decode()}")
        print(f"\n[{bcolors.BLUE}>>>{bcolors.WHITE}] File saved as: encrypted_file.ENC")

        with open("encrypted_file.ENC", "w") as file2:
            file2.write(encryption.decode())

        time.sleep(5)
        start_main()
    except:
        print(f"\n[{bcolors.RED}X{bcolors.WHITE}] Encryption Error. Check Your Key!")

def decrypt_option(encrypted_text):
    try:
        subprocess.run("cls", shell=True)
        with open("key.key", "r") as file:
            key_data = file.read()
        key = Fernet(key_data)

        decryption = key.decrypt(encrypted_text)
        print(f"\n[{bcolors.BLUE}+{bcolors.WHITE}] Encrypted text: {encrypted_text}")
        print(f"\n[{bcolors.GREEN}${bcolors.WHITE}] Decrypted text: {decryption.decode()}")
        print(f"\n[{bcolors.BLUE}>>>{bcolors.WHITE}] File saved as: decrypted_file.DEC")

        with open("decrypted_file.DEC", "w") as file3:
            file3.write(decryption.decode())

        time.sleep(5)
        start_main()
    except:
        print(f"\n[{bcolors.RED}X{bcolors.WHITE}] Decryption Error. Check Your Key!")

def select_files():
    global file_path, filename
    subprocess.run("cls", shell=True)
    while True:
        try:
            filename = input(f"[{bcolors.BLUE}>>>{bcolors.WHITE}] Enter file path: ")

            with open(filename, "r") as file:
                file_path = file.read()
            start_main()

        except KeyboardInterrupt:
            subprocess.run("cls", shell=True)
            break
        except:
            print(f"\n[{bcolors.YELLOW}!{bcolors.WHITE}] File Not Found")

def start_main():
    try:
        subprocess.run("cls", shell=True)
        while True:
            print(f"""   
    ------- M.SMY.CryptoGraphy -------
                  
        [{bcolors.RED}1{bcolors.WHITE}] Encrypt files
        [{bcolors.RED}2{bcolors.WHITE}] Decrypt files
        [{bcolors.RED}3{bcolors.WHITE}] Select files
        [{bcolors.RED}Exit{bcolors.WHITE}] Ctrl + C  
                  
    [{bcolors.GREEN}@{bcolors.WHITE}] Selected File: {filename}

    [{bcolors.GREEN}#{bcolors.WHITE}] File Data: {file_path}

    # {bcolors.YELLOW}Created by Moaaz Mourad Cyber Security LvL3 {bcolors.WHITE}#      
""")
            cmd = int(input(f"(@{bcolors.BLUE}moaz{bcolors.WHITE}~{bcolors.BLUE}crypto{bcolors.WHITE})> "))
            if cmd == 1:
                encrypt_option(file_path.encode())
            elif cmd == 2:
                decrypt_option(file_path.encode())
            elif cmd == 3:
                select_files()
            else:
                print(f"\n[{bcolors.YELLOW}!{bcolors.WHITE}] Command Error. Type again")
    except ValueError:
        print(f"\n[{bcolors.RED}X{bcolors.WHITE}] Value Error. Input Should Be An Integer")
    except KeyboardInterrupt:
        exit()

select_files()