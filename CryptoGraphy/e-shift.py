def encrypt_messages():
    text = input("[*] Enter your message> ")
    shift = int(input("[*] Enter shift> "))

    if shift > 0:
        key = (shift - 2 + 3 + 5 - 1)
    else:
        key = (shift + 2 - 3 - 5 + 1)

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_text = ' '

    for i in text.lower():
        if i == ' ':
            encrypted_text += i
        else:
            index = alphabet.find(i)
            new_index = (index + key) % len(alphabet)
            encrypted_text += alphabet[new_index]

    print(f"\n[*] Shift: {shift}")
    print(f"[*] Normal: {text}")
    print(f"[*] Encrypted: {encrypted_text} ({shift})")

encrypt_messages()