from Controller import RSAController
from View import ModeSelectionView
from Model import DAO
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
import math
import random
import numpy as np


class PublicKeyView:
    def __init__(self):
        self.main = Tk()
        self.main.title("RSA Public Mode")
        self.icon = PhotoImage(file="Image/shield.png")
        self.main.iconphoto(False, self.icon)
        self.main.attributes("-topmost", True)
        self.main.resizable(False, False)


        self.TextLabel = Label(self.main, text="Bản rõ:", font=("Arial", "12"))
        self.TextField = Text(self.main, borderwidth=2, relief="ridge", width=60, height=10)
        self.TextScrollbar = Scrollbar(self.main, command=self.TextField.yview, orient=VERTICAL)
        self.TextField['yscrollcommand'] = self.TextScrollbar.set

        self.CryptLabel = Label(self.main, text="Bản mã:", font=("Arial", "12"))
        self.CryptField = Text(self.main, borderwidth=2, relief="ridge", width=60, height=10, state="disabled")
        self.CryptScrollbar = Scrollbar(self.main, command=self.CryptField.yview, orient=VERTICAL)
        self.CryptField['yscrollcommand'] = self.CryptScrollbar.set

        self.CipherOptionLabel1 = Label(self.main, text="Mã hóa RSA", font=("Arial", "14", "bold"))
        self.CipherOptionLabel2 = Label(self.main, text="Chế độ mã hóa", font=("Arial", "14", "bold"))

        self.KLabel = Label(self.main, text="Khóa công khai:", font=("Arial", "12"))
        self.KField = Entry(self.main, font=("Arial", "12"))

        self.var = IntVar()
        self.var.set(0)
        self.DefaultRadioButton = Radiobutton(self.main, text="Mặc định", variable=self.var, value=0)
        self.FileRadioButton = Radiobutton(self.main, text="Chọn file", variable=self.var, value=1)

        self.EncryptButton = ttk.Button(self.main, text="Encrypt", command=self.EncryptButtonClick)
        self.MenuButton = ttk.Button(self.main, text="Menu", command=self.MenuButtonClick)

        self.TextLabel.grid(column=0, row=0, sticky=W)
        self.TextField.grid(column=0, row=1, columnspan=2, rowspan=2)
        self.TextScrollbar.grid(column=2, row=1, rowspan=2, sticky=W + N + S)

        self.CryptLabel.grid(column=0, row=3, sticky=W)
        self.CryptField.grid(column=0, row=4, columnspan=2, rowspan=3)
        self.CryptScrollbar.grid(column=2, row=4, rowspan=3, sticky=W + N + S)

        self.CipherOptionLabel1.grid(column=3, row=1, columnspan=2, padx=10, sticky=S)
        self.CipherOptionLabel2.grid(column=3, row=2, columnspan=2, sticky=N)

        self.KLabel.grid(column=3, row=3, columnspan=2, sticky=W, padx=10)
        self.KField.grid(column=3, row=4, columnspan=2, sticky=N, padx=10)

        self.DefaultRadioButton.grid(column=3, row=5, sticky=S)
        self.FileRadioButton.grid(column=4, row=5, sticky=S)

        self.EncryptButton.grid(column=3, row=6)
        self.MenuButton.grid(column=4, row=6)

        self.main.mainloop()

    def MenuButtonClick(self):
        self.main.destroy()
        ModeSelectionView.ModeSelectionView()

    def EncryptButtonClick(self):
        s = self.TextField.get('1.0', 'end-1c')
        k = self.KField.get()
        if s == "":
            self.TextField.insert(END, DAO.GetText().strip())
            self.CryptField.configure(state="normal")
            self.CryptField.delete('1.0', 'end-1c')
            self.CryptField.configure(state="disabled")
        else:
            DAO.SetText(s)
            if k == "":
                messagebox.showerror("Error", "Khóa công khai không được để trống")
            else:
                try:
                    k = tuple(int(num) for num in
                              k.replace(", ", ",").replace("(", "").replace(")", "")
                              .replace("[", "").replace("]", "").replace("{", "")
                              .replace("}", "").replace(",", " ").split(" "))
                    if len(k) != 2:
                        messagebox.showerror("Error", "Khóa công khai không hợp lệ")
                    else:
                        crypt = RSAController.Encrypt(k)
                        crypt = DAO.dec_txt(str(crypt))
                        DAO.SetCrypt(crypt)
                        self.CryptField.configure(state="normal")
                        self.CryptField.delete('1.0', 'end-1c')
                        self.CryptField.insert(END, crypt)
                        self.CryptField.configure(state="disabled")
                except:
                    messagebox.showerror("Error", "Khóa công khai không hợp lệ")


class PrivateKeyView:
    def __init__(self):
        self.main = Tk()
        self.main.title("RSA Private Mode")
        self.icon = PhotoImage(file="Image/shield.png")
        self.main.iconphoto(False, self.icon)
        self.main.attributes("-topmost", True)
        self.main.resizable(False, False)

        self.TextLabel = Label(self.main, text="Bản rõ:", font=("Arial", "12"))
        self.TextField = Text(self.main, borderwidth=2, relief="ridge", width=60, height=10, state="disabled")
        self.TextScrollbar = Scrollbar(self.main, command=self.TextField.yview, orient=VERTICAL)
        self.TextField['yscrollcommand'] = self.TextScrollbar.set

        self.CryptLabel = Label(self.main, text="Bản mã:", font=("Arial", "12"))
        self.CryptField = Text(self.main, borderwidth=2, relief="ridge", width=60, height=10)
        self.CryptScrollbar = Scrollbar(self.main, command=self.CryptField.yview, orient=VERTICAL)
        self.CryptField['yscrollcommand'] = self.CryptScrollbar.set

        self.CipherOptionLabel1 = Label(self.main, text="Mã hóa RSA", font=("Arial", "14", "bold"))
        self.CipherOptionLabel2 = Label(self.main, text="Chế độ giải mã", font=("Arial", "14", "bold"))

        self.KLabel = Label(self.main, text="Khóa bí mật:", font=("Arial", "12"))
        self.KField = Entry(self.main, font=("Arial", "12"))

        self.var = IntVar()
        self.var.set(0)
        self.DefaultRadioButton = Radiobutton(self.main, text="Mặc định", variable=self.var, value=0)
        self.FileRadioButton = Radiobutton(self.main, text="Chọn file", variable=self.var, value=1)

        self.DecryptButton = ttk.Button(self.main, text="Decrypt", command=self.DecryptButtonClick)
        self.MenuButton = ttk.Button(self.main, text="Menu", command=self.MenuButtonClick)

        self.TextLabel.grid(column=0, row=3, sticky=W)
        self.TextField.grid(column=0, row=4, columnspan=2, rowspan=3)
        self.TextScrollbar.grid(column=2, row=1, rowspan=3, sticky=W + N + S)

        self.CryptLabel.grid(column=0, row=0, sticky=W)
        self.CryptField.grid(column=0, row=1, columnspan=2, rowspan=2)
        self.CryptScrollbar.grid(column=2, row=4, rowspan=2, sticky=W + N + S)

        self.CipherOptionLabel1.grid(column=3, row=1, columnspan=2, padx=10, sticky=S)
        self.CipherOptionLabel2.grid(column=3, row=2, columnspan=2, sticky=N)

        self.KLabel.grid(column=3, row=3, columnspan=2, sticky=W, padx=10)
        self.KField.grid(column=3, row=4, columnspan=2, sticky=N, padx=10)

        self.DefaultRadioButton.grid(column=3, row=5, sticky=S)
        self.FileRadioButton.grid(column=4, row=5, sticky=S)

        self.DecryptButton.grid(column=3, row=6)
        self.MenuButton.grid(column=4, row=6)

        self.main.mainloop()

    def MenuButtonClick(self):
        self.main.destroy()
        ModeSelectionView.ModeSelectionView()

    def DecryptButtonClick(self):
        s = self.CryptField.get('1.0', 'end-1c')
        k = self.KField.get()
        if s == "":
            self.CryptField.insert(END, DAO.GetCrypt().strip())
            self.TextField.configure(state="normal")
            self.TextField.delete('1.0', 'end-1c')
            self.TextField.configure(state="disabled")
        else:
            DAO.SetCrypt(s)
            if k == "":
                messagebox.showerror("Error", "Khóa bí mật không được để trống")
            else:
                try:
                    k = tuple(int(num) for num in
                              k.replace(", ", ",").replace("(", "").replace(")", "")
                              .replace("[", "").replace("]", "").replace("{", "")
                              .replace("}", "").replace(",", " ").split(" "))
                    if len(k) != 2:
                        messagebox.showerror("Error", "Khóa bí mật không hợp lệ")
                    else:
                        text = RSAController.Decrypt(k)
                        text = DAO.dec_txt(str(text))
                        DAO.SetText(text)
                        self.TextField.configure(state="normal")
                        self.TextField.delete('1.0', 'end-1c')
                        self.TextField.insert(END, text)
                        self.TextField.configure(state="disabled")
                except:
                    messagebox.showerror("Error", "Khóa bí mật không hợp lệ")
