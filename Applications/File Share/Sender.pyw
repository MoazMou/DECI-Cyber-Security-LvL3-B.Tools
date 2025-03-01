import socket
from tkinter import *
from tkinter import ttk, filedialog, messagebox

root = Tk()
root.title("Python File Transfer (Sender) DEMO")
root.geometry('400x430')
root.iconbitmap(r'img\\icon.ico')

img = PhotoImage(file="img\\background.png")
send_logo = PhotoImage(file="img\\send.png")
share_logo = PhotoImage(file="img\\share.png")
app_background = Label(root, image=img, width=450, height=250).pack(side=TOP)

def open_files():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_data.set(file_path)

def start_stream():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 7777))
    server.listen(1)

    conn, addr = server.accept()

    with open(f"{entry_data.get()}", "rb") as file:
        while True:
            file_data = file.read(1024)
            if not file_data:
                break
            conn.send(file_data)
        messagebox.showinfo("File Transfer", "File has sent!")

entry_data = StringVar()
entry_path = ttk.Entry(root, width=50, textvariable=entry_data, font=10).pack(side=TOP, pady=8)
get_btn = Button(root, text="    Open files", image=send_logo, width=280, height=50, compound=LEFT, command=open_files, font=("arila",15,"bold")).pack(side=TOP, pady=5)
send_btn = Button(root, text="   Send files", image=share_logo, width=280, height=50, compound=LEFT, command=start_stream, font=("arila",15,"bold")).pack(side=TOP)

root.mainloop()