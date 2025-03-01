from tkinter import *
from tkinter import ttk, messagebox, filedialog

root = Tk()
root.title("-PyDataBase v0.5-")
root.geometry('600x550')
root.iconbitmap(r'img\\icon.ico')
root.configure(bg="white")

def help_option():
    window = Tk()
    window.title("-Help-")
    window.iconbitmap(r'img\\icon.ico')
    window.geometry('740x360')

    default_text = """
                                    
                                                [Welcome to Python Database!]

 This application allows you to create, edit, and save text files with ease. Below are the main features:

 1. **Open a File**: Load an existing text file into the editor by selecting 'Open' from the 'File' menu.
 2. **Save Your Work**: Save your current text to a file by choosing 'Save' in the 'File' menu.
 3. **Clear the Editor**: Use 'Clear' to remove all text from the editor.
 4. **Exit the Application**: Select 'Exit' from the 'File' menu to close the editor.

 Instructions:
 - Use the menu options at the top of the window to perform actions.
 - Type your text freely in the editor below.
 - Remember to save your work before exiting!

 Enjoy using this simple text editor!
"""
    text_area = Text(window, width=500, height=20, font=("arila",13))
    text_area.pack(side=TOP)
    text_area.insert("1.0", default_text)


    window.mainloop()

def clear_tree():
    for item in tree.get_children():
        tree.delete(item)

def create_data():
    filename = filedialog.asksaveasfile(filetypes=[("Text file", "*.pydb")])
    if not filename:
        return

def open_data():
    global path
    try:
        clear_tree()
        
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
        
        path = filedialog.askopenfilename(filetypes=[("Text file", "*.pydb")])
        print(path)
        if not path:
            return
        get_data()
    except Exception as msg:
        print(f"Error: {msg}")
        messagebox.showerror(title="PyDataBase", message="File not found!")

def get_data():
    with open(f'{path}', 'r') as file:
        rows = file.readlines()
        for index, line in enumerate(rows):
            values = line.strip().split(",")
            tree.insert(parent="" , index="end", iid=index, values=values)

def add_data():
    try:
        id = id_entry.get()
        username = name_entry.get()
        email_address = email_entry.get()
        password = password_entry.get()

        if not id or not username or not email_address or not password:
            messagebox.showwarning(title="PyDatabse", message="Empty input found!")
        else:
            with open(f"{path}", "a") as add_data:
                add_data.write(f"\n{id},{username},{email_address},{password}")
            print(f"Added client: {id}, {username}, {email_address}, {password}")
            clear_tree()
            get_data()
            messagebox.showinfo(title="Main", message="A new client has added!")
    except Exception as msg:
        print(f"Error: {msg}")

def selected_items():
    selected_data = tree.focus()
    details = tree.item(selected_data)

    if not details["values"]:
        messagebox.showerror(title="Main", message="No item selected!")
        return
    
    ID = details.get("values")[0]
    Name = details.get("values")[1]
    Email = details.get("values")[2]
    Password = details.get("values")[3]

    id_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)

    id_entry.insert(END, ID)
    name_entry.insert(END, Name)
    email_entry.insert(END, Email)
    password_entry.insert(END, Password)

def delete_data():
    try:
        selected_data = tree.focus()
        details = tree.item(selected_data)

        if not details["values"]:
            messagebox.showerror(title="Main", message="No item selected!")
            return
        
        id_to_delete = details["values"][0]

        with open(f"{path}", "r") as get_id:
            lines = get_id.readlines()

        with open(f"{path}", "w") as edit_data:
            for line in lines:
                values = line.strip().split(",")
                if values[0] != str(id_to_delete):
                    edit_data.write(line)
        
        tree.delete(selected_items)
        clear_tree()
        get_data()
        messagebox.showinfo(title="Main", message=f"Client ID [{id_to_delete}] has removed!")
    except Exception as msg:
        print(f"Error: {msg}")
        clear_tree()
        get_data()
        messagebox.showinfo(title="Main", message=f"Client ID [{id_to_delete}] has removed!")

def update_data():
    try:
        selected_data = tree.focus()
        details = tree.item(selected_data)

        if not details["values"]:
            messagebox.showerror(title="Main", message="No item selected!")
            return
        
        old_id = details["values"][0]
        new_id = id_entry.get()
        new_name = name_entry.get()
        new_email = email_entry.get()
        new_password = password_entry.get()

        if not new_id or not new_name or not new_email or not new_password:
            messagebox.showwarning(title="PyDatabse", message="Empty input found!")
        else:
            with open(f"{path}", "r") as get_id:
                lines = get_id.readlines()

            with open(f"{path}", "w") as edit_data:
                for line in lines:
                    values = line.strip().split(",")
                    if values[0] == str(old_id):
                        edit_data.write(f"{new_id},{new_name},{new_email},{new_password}\n")
                    else:
                        edit_data.write(line)
        
            clear_tree()
            get_data()
            messagebox.showinfo(title="Main", message=f"Client ID [{old_id}] has updated!")
    except Exception as msg:
        print(f"Error: {msg}")
        clear_tree()
        get_data()

def destroy():
    root.destroy()


menus = Menu(root)
root.config(menu=menus)

file_menu = Menu(menus, tearoff=0)
file_menu.add_command(label="Open file", command=open_data)
file_menu.add_separator()
file_menu.add_command(label="Create file", command=create_data)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=destroy)
menus.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menus, tearoff=0)
help_menu.add_command(label="How to use?", command=help_option)
menus.add_cascade(label="Help", menu=help_menu)

title_label = Label(root, text="PyDataBase v0.5", width=20, height=2, bg="white", font=("arila",25,"bold")).pack(side=TOP)

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(root, yscrollcommand=scroll.set)
tree.pack(pady=10, fill=BOTH, expand=True)
tree['columns'] = ("ID", "Name", "Email", "Password")

scroll.config(command=tree.yview)

tree.heading("#0", text="")
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.heading("Email", text="Email")
tree.heading("Password", text="Password")
tree.column("#0", width=0)
tree.column("ID", anchor=CENTER, width=50)
tree.column("Name", anchor=CENTER, width=160)
tree.column("Email", anchor=CENTER, width=190)
tree.column("Password", anchor=CENTER, width=180)

labels_frame = Frame(root, bg="white", relief=GROOVE, bd=2)
labels_frame.pack(pady=10, fill=X, padx=20)

Label(labels_frame, text="ID:", bg="white", fg="black", font=("arila",11)).grid(row=0, column=0, padx=5, pady=5, sticky=W)
Label(labels_frame, text="Name:", bg="white", fg="black", font=("arila",11)).grid(row=0, column=2, padx=5, pady=5, sticky=W)
Label(labels_frame, text="Email:", bg="white", fg="black", font=("arila",11)).grid(row=1, column=0, padx=5, pady=5, sticky=W)
Label(labels_frame, text="Password:", bg="white", fg="black", font=("arila",11)).grid(row=1, column=2, padx=5, pady=5, sticky=W)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="white", foreground="#333", rowheight=25, fieldbackground="white")
style.map("Treeview", background=[("selected", "#347083")])

btns_frame = Frame(root, bg="white")
btns_frame.pack(pady=10, fill=X, padx=20)

id_entry = ttk.Entry(labels_frame, width=20, font=("arila",13))
id_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
name_entry = ttk.Entry(labels_frame, width=20, font=("arila",13))
name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)
email_entry = ttk.Entry(labels_frame, width=20, font=("arila",13))
email_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
password_entry = ttk.Entry(labels_frame, width=20, font=("arila",13))
password_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

select_btn = ttk.Button(btns_frame, text="Select", width=12, command=selected_items).grid(row=0, column=0, padx=10)
update_btn = ttk.Button(btns_frame, text="Update", width=12, command=update_data).grid(row=0, column=1, padx=10)
add_btn = ttk.Button(btns_frame, text="Add Data", width=12, command=add_data).grid(row=0, column=2, padx=10)
remove_btn = ttk.Button(btns_frame, text="Remove Data", width=12, command=delete_data).grid(row=0, column=3, padx=10)

root.mainloop()