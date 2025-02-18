import subprocess
from tkinter import *
from tkinter import messagebox, filedialog

root = Tk()
root.title("RFP Locker | version 2.0")
root.geometry('360x600')
try:
    root.iconbitmap(r"img/icon.ico")
except:
    root.configure(bg="black")

def lock_file():
    try:
        path = filedialog.askdirectory()
        if not path:
            return
        subprocess.run(f"attrib \"{path}\" +r +h +s", shell=True, check=True)
        subprocess.run(f"cacls \"{path}\" /e /p everyone:n", shell=True, check=True)
        messagebox.showinfo(title="RFP Locker", message="Folder has been locked!")
    except subprocess.CalledProcessError as msg:
        messagebox.showinfo(title="RFP Locker", message="Folder has been locked!")

def support():
    messagebox.showinfo(title="RFP Locker | Tech Support", message="Call the creator: Moaaz Mourad\n\nPhone: +20 1155633000")

def unlock_file():
    root = Tk()
    root.title("RFP Locker | File Unlock")
    root.geometry('400x130')
    root.configure(bg="black")
    try:
        root.iconbitmap(r"img/icon.ico")
    except:
        root.configure(bg="black")

    def root_unlocker():
        try:
            path = path_entry.get()
            if not path:
                messagebox.showwarning(title="RFP Locker | Warning", message="Folder path not found!")
                return

            subprocess.run(f"cacls \"{path}\" /T /E /P everyone:f", shell=True, check=True)
            subprocess.run(f"attrib \"{path}\" -r -h -s", shell=True, check=True)
            messagebox.showinfo(title="RFP Locker", message="Folder has been unlocked!")
        except subprocess.CalledProcessError as msg:
            messagebox.showerror(title="RFP Locker | Error", message=f"Process Error:\n\n {msg}")
    
    Label(root, text="Enter your folder path: ", width=20, bg="black", fg="white", font=10).pack(side=TOP, padx=10, pady=5)
    path_entry = Entry(root, width=50, font=15)
    path_entry.pack(side=TOP, padx=10, pady=5)
    Button(root, text="File Unlock", width=13, height=1, bg="black", fg="white", command=root_unlocker, font=("arila",15,"bold")).pack(side=TOP, padx=10, pady=5)
    root.mainloop()

try:
    image = PhotoImage(file="img\\bg.png")
    bg_lable = Label(root, width=500, height=600, image=image).pack()
except:
    root.configure(bg="black")

Button(root, text="File Lock", width=13, height=1, bg="black", fg="white", command=lock_file, font=("arila",15,"bold")).place(x=95, y=410)
Button(root, text="File Unlock", width=13, height=1, bg="black", fg="white", command=unlock_file, font=("arila",15,"bold")).place(x=95, y=470)
Button(root, text="Tech support", width=13, height=1, bg="black", fg="white", command=support, font=("arila",15,"bold")).place(x=95, y=530)
root.mainloop()