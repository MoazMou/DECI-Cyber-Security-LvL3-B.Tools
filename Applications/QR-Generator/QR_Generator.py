import qrcode 
def main():
    while True:
        data = input("  [*] Enter URl of Message: ")
        img = qrcode.make(f"{data}")
        img.save("image.png")
        qr = qrcode.QRCode()
        qr.add_data(f"{data}")
        qr.print_ascii()
main()