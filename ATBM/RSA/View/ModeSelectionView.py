from tkinter import *
from tkinter import ttk
from View import MainView


class ModeSelectionView:
    def __init__(self):
        self.main = Tk()
        self.main.title("RSA Mode Select")
        self.icon = PhotoImage(file="Image/shield.png")
        self.main.iconphoto(False, self.icon)
        self.main.attributes("-topmost", True)
        self.main.resizable(False, False)

        self.MainFrame = Frame(self.main, width=200, height=100)

        self.Label = Label(self.MainFrame, text="RSA Mode", font=("Arial", "12"))
        self.PrivateKeyButton = ttk.Button(self.MainFrame, text="Private Key", command=self.PrivateKeyButtonClick)
        self.PublicKeyButton = ttk.Button(self.MainFrame, text="Public Key", command=self.PublicKeyButtonClick)

        self.MainFrame.grid(column=0, row=0)
        self.Label.grid(column=0, row=0, columnspan=2, pady=5)
        self.PrivateKeyButton.grid(column=0, row=1, padx=40, pady=20)
        self.PublicKeyButton.grid(column=1, row=1, padx=40, pady=20)

        self.main.mainloop()

    def PrivateKeyButtonClick(self):
        self.main.destroy()
        MainView.PrivateKeyView()

    def PublicKeyButtonClick(self):
        self.main.destroy()
        MainView.PublicKeyView()
