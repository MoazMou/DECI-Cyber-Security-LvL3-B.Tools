import socket
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title("Python File Transfer (Reciever) DEMO")
root.geometry("400x420")
root.iconbitmap(r'img\\icon.ico')

img = PhotoImage(file="img\\background.png")
recieve_logo = PhotoImage(file="img\\receive.png")
app_background = Label(root, image=img, width=450, height=250).pack(side=TOP)

def receive_files():
    receiver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver.connect((f"{entry_IP.get()}", 7777))

    with open(f"Receiver\\{entry_path.get()}", 'wb') as file:
        while True:
            file_data = receiver.recv(1024)
            if not file_data:
                break
            file.write(file_data)
        messagebox.showinfo("File Transfer", "File has received!")

entry_data = StringVar()
entry_IP_data = StringVar()
label = Label(root, text="Connect to an IP:", font=("arila",15,"bold")).place(x=20, y=260)
entry_IP = ttk.Entry(root, width=15, textvariable=entry_IP_data, font=15)
entry_IP.place(x=200, y=260)
label = Label(root, text="Filename with extension:", font=("arila",15,"bold")).place(x=20, y=310)
entry_path = ttk.Entry(root, width=13, textvariable=entry_data, font=15)
entry_path.place(x=270, y=310)
recieve_btn = Button(root, text="   Receive files", image=recieve_logo, width=280, height=50, compound=LEFT, command=receive_files, font=("arila",15,"bold")).place(x=55, y=350)

root.mainloop()