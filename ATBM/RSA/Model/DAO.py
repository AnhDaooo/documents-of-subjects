import numpy as np


def SetText(s):
    f = open("Data/text.txt", "w")
    f.write(txt_dec(str(s)))
    f.close()


def SetCrypt(s):
    f = open("Data/crypt.txt", "w")
    f.write(txt_dec(str(s)))
    f.close()


def GetText():
    f = open("Data/text.txt", "r")
    s = dec_txt(f.read())
    f.close()
    return s


def GetDecText():
    f = open("Data/text.txt", "r")
    s = f.read()
    f.close()
    return s


def GetCrypt():
    f = open("Data/crypt.txt", "r")
    s = dec_txt(f.read())
    f.close()
    return s


def GetDecCrypt():
    f = open("Data/crypt.txt", "r")
    s = f.read()
    f.close()
    return s


def txt_dec(s):
    output = ""
    for i in s:
        output += str(ord(i) - 32).zfill(2)
    return output


def dec_txt(s):
    output = ""
    if len(s) % 2 != 0:
        dec = "0" + s
    else:
        dec = s
    char = [dec[2 * i] + dec[2 * i + 1] for i in range(len(dec) // 2)]
    for i in char:
        output += chr(int(i) + 32)
    return output
