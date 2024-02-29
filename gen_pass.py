import tkinter as tk
from tkinter import simpledialog, messagebox
from random import sample
import pyperclip

lower_letter = "bcdfghjklmnpqrstvwxyz"
upper_letter = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "aeiou"
numbers = "1234567890"
special_characters = '!"£$%&/()=_-[]*#,;'

def gen_pass():
    characters = lower_letter + upper_letter + vowels + numbers + special_characters
    
    min_length = 8
    min_uppercase = 1
    min_special_chars = 1

    try:
        desired_length = int(simpledialog.askstring("Password Length", "Specify password length:"))
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer for the password length.")
        return

    if desired_length < min_length:
        messagebox.showwarning("Invalid Input", f"Password length must be at least {min_length}.")
        return

    if desired_length < min_uppercase + min_special_chars:
        min_uppercase = min_special_chars = 1

    password = []
    uppercase_count = special_char_count = 0
    
    while uppercase_count < min_uppercase:
        random_char = sample(upper_letter, 1)[0]
        if random_char not in password:
            password.append(random_char)
            uppercase_count += 1

    while special_char_count < min_special_chars:
        random_char = sample(special_characters, 1)[0]
        if random_char not in password:
            password.append(random_char)
            special_char_count += 1

    for i in range(len(password), desired_length):
        random_char = sample(characters, 1)[0]
        password.append(random_char)

    password = ''.join(password)
    pyperclip.copy(password)
    messagebox.showinfo("Password Generated", f"Password generated is --> {password} \n Password copied to clipboard")


def check_password():
    password = simpledialog.askstring("Check Password", "Insert password:")
    if not password:
        return
    try:
        if len(password) < 8:
            messagebox.showwarning("Password Criteria", "Password must be at least 8 characters long.")
            return
        if not any(char.islower() for char in password):
            messagebox.showwarning("Password Criteria", "Password must contain at least one lowercase letter.")
            return
        if not any(char.isupper() for char in password):
            messagebox.showwarning("Password Criteria", "Password must contain at least one uppercase letter.")
            return
        if not any(char.isdigit() for char in password):
            messagebox.showwarning("Password Criteria", "Password must contain at least one number.")
            return
        if not any(char in special_characters for char in password):
            messagebox.showwarning("Password Criteria", "Password must contain at least one special character.")
            return
        messagebox.showinfo("Password Criteria", "Password is valid!")
    except KeyboardInterrupt:
        messagebox.showinfo("KeyboardInterrupt", "KeyboardInterrupt detected. Program execution stopped.")
        return

def main():
    root = tk.Tk()
    root.title("Password Generator & Checker")

    btn_gen = tk.Button(root, text="Generate Password", command=gen_pass)
    btn_gen.pack(pady=10)

    btn_check = tk.Button(root, text="Check Password", command=check_password)
    btn_check.pack(pady=10)

    btn_exit = tk.Button(root, text="Exit", command=root.destroy)
    btn_exit.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()