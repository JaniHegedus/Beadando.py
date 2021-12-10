# Szükséges függvények importálása:
from datetime import datetime  # idő
from tkinter import *  # Grafikus
import tkinter.font as tkf  # Grafikus karakterváltoztatás Entry-hez
from enum import Enum  # Enum
import tkinter as tk  # Grafikus
import configparser  # config file olvasó
import io  # file olvasás írás
import os  # file megnyitás törlés

# config fájl beolvasása:
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
config.sections()

""" ALAP VÁLTOZÓK DEFINIÁLÁSA CONFIG FILE NÉLKÜL
ts=25
x=40
y=10
text_type="Arial"
Text_color="blue"
Bg_color="white"
txt_file="Rendelés.txt"
input_file="Ettermek.txt"
input_file0="Prices.txt"
input_file1="Nyitvatartas.txt"
justify_entry="center"
text_type_entry="Arial"
text_size_entry=22
width_entry=18
bg_entry="white"
fg_entry="red"
disabledforeground_entry="red"
disabledbackground_entry="red"
highlightbackground_entry="black"
highlightcolor_entry="blue"
highlightthickness_entry=1
bd_entry=0
encoding_in="utf-8"
encoding_out="utf-8"
root.title("Ételrendelés")
root.iconbitmap('my_ico.ico')
"""
# Listák/Mátrixok/Változók definiálása:
b = 1
rendelt = 1
nyitva = False
nyitvaa = 0
matrix = []
matrix0 = []
matrix1 = []
Ettermek = []
Foetelek = []
Koretek = []
Italok = []
AR = []
ARAK = []

# Változódefiniálás
root_title = config['root']['root_title']
root_icon = config['root']['root_icon']

txt_file = config['my_files']['txt_file']
input_file = config['my_files']['input_file']
input_file0 = config['my_files']['input_file0']
encoding_in = config['my_files']['encoding_in']
encoding_out = config['my_files']['encoding_out']
ts = int(config['Text']['Text_size'])
text_type = config['Text']['text_type']
Text_color = config['Text']['Text_color']
Important_text_color = config['Text']['Important_text_color']
Bg_color = config['Text']['Bg_color']
x = int(config['other']['Buttonsize_x'])
y = int(config['other']['Buttonsize_y'])

fullscreen = config['other']['Fullscreen']
custom_resolution = config['other']['custom_resolution']

justify_entry = config['Entry']['justify_entry']
text_type_entry = config['Entry']['text_type_entry']
text_size_entry = int(config['Entry']['text_size_entry'])
width_entry = int(config['Entry']['width_entry'])
bg_entry = config['Entry']['bg_entry']
fg_entry = config['Entry']['fg_entry']
disabledforeground_entry = config['Entry']['disabledforeground_entry']
disabledbackground_entry = config['Entry']['disabledbackground_entry']
highlightbackground_entry = config['Entry']['highlightbackground_entry']
highlightcolor_entry = config['Entry']['highlightcolor_entry']
highlightthickness_entry = int(config['Entry']['highlightthickness_entry'])
bd_entry = int(config['Entry']['bd_entry'])

root = Tk()
root.title(root_title)
root.iconbitmap(root_icon)

for o in range(14):  # sorbeállítás
    root.columnconfigure(o, minsize=25)

root.overrideredirect(fullscreen)  # Teljesképernyő ki/be

if fullscreen:
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
else:
    root.geometry(custom_resolution)

# File beolvasás
with io.open(input_file, "r", encoding=encoding_in) as fbee:
    for sor in fbee:
        kis_lista = []
        sor = sor.strip().split()
        for elem in sor:
            kis_lista.append(elem)
        matrix.append(kis_lista)
    fbee.close()
with io.open(input_file0, "r", encoding=encoding_in) as fbeee:
    for sor in fbeee:
        kis_lista = []
        sor = sor.strip().split()
        for elem in sor:
            kis_lista.append(elem)
        matrix0.append(kis_lista)
    fbeee.close()

# Listák feltöltése
for j in range(len(matrix)):
    kis_lista = []
    kis_lista0 = []
    kis_lista1 = []
    kis_lista2 = []
    kis_lista3 = []
    for i in range(len(matrix[j])):
        if matrix[j][i] == '-':
            kis_lista.append(matrix[j - 1][len(matrix[j]) - 1])
            kis_lista.append(matrix[j - 1][len(matrix[j])])
            for k in range(1, 5):
                kis_lista0.append(matrix[j + k][0])
                kis_lista0.append(matrix[j + k][1])
                kis_lista1.append(matrix[j + k][2])
                kis_lista2.append(matrix[j + k][3])
                kis_lista3.append(matrix[j + k][4])
        """
        kis_lista.append(matrix[k + 2][0])
        kis_lista.append(matrix[k + 2][1])
        kis_lista.append(matrix[k + 3][0])
        kis_lista.append(matrix[k + 3][1])
        kis_lista.append(matrix[k + 4][0])
        kis_lista.append(matrix[k + 4][1])
        kis_lista0.append(matrix[k + 2][2])
        kis_lista0.append(matrix[k + 3][2])
        kis_lista0.append(matrix[k + 4][2])
        kis_lista1.append(matrix[k + 2][3])
        kis_lista1.append(matrix[k + 3][3])
        kis_lista1.append(matrix[k + 4][3])
        kis_lista2.append(matrix[k + 2][4])
        kis_lista2.append(matrix[k + 3][4])
        kis_lista2.append(matrix[k + 4][4])
        """
        if kis_lista:
            Foetelek.append(kis_lista0)
        if kis_lista0:
            Koretek.append(kis_lista1)
        if kis_lista1:
            Italok.append(kis_lista2)
        if kis_lista2:
            AR.append(kis_lista3)
    if kis_lista:
        Ettermek.append(kis_lista)


# Classek létrehozása
class Étterem:
    def __init__(self, et=" "):
        self.et = et

    def nev(self, et):
        self.et = ""
        self.et += Ettermek[et - 1][0]
        self.et += " "
        self.et += Ettermek[et - 1][1]
        """
        if et==1:
            self.et+=Ettermek[0][0]
            self.et+=" "
            self.et+=Ettermek[0][1]
        elif et==2:
            self.et+=Ettermek[1][0]
            self.et+=" "
            self.et+=Ettermek[1][1]
        elif et==3:
            self.et+=Ettermek[2][0]
            self.et+=" "
            self.et+=Ettermek[2][1]
        elif et==4:
            self.et+=Ettermek[3][0]
            self.et+=" "
            self.et+=Ettermek[3][1]
        """
        return self.et

class Menü(Étterem):
    def __init__(self):
        self.et = Étterem.__init__(self)

    def foetel(self, et, foetel):
        self.foetel = foetel
        et -= 1
        global i
        global j
        for i in range(len(Foetelek)):
            if et == i:
                if foetel == 1:
                    self.foetel = ""
                    self.foetel += Foetelek[i][0]
                    self.foetel += " "
                    self.foetel += Foetelek[i][1]
                elif foetel == 2:
                    self.foetel = ""
                    self.foetel += Foetelek[i][2]
                    self.foetel += " "
                    self.foetel += Foetelek[i][3]
                elif foetel == 3:
                    self.foetel = ""
                    self.foetel += Foetelek[i][4]
                    self.foetel += " "
                    self.foetel += Foetelek[i][5]
                elif foetel == 4:
                    self.foetel = ""
                    self.foetel += Foetelek[i][6]
                    self.foetel += " "
                    self.foetel += Foetelek[i][7]
        return self.foetel

    def koret(self, et, koret):
        global i
        global j
        self.koret = koret
        et -= 1
        koret -= 1
        if 4 >= et >= 0:
            for i in range(len(Koretek)):
                for j in range(len(Koretek[i])):
                    if et == i:
                        if koret == j:
                            self.koret = ""
                            self.koret = Koretek[i][j]
        return self.koret

    def ital(self, et, ital):
        global i
        global j
        self.ital = ital
        et -= 1
        ital -= 1
        if 4 >= et >= 0:
            for i in range(len(Italok)):
                for j in range(len(Italok[i])):
                    if et == i:
                        if ital == j:
                            self.ital = ""
                            self.ital = Italok[i][j]
        return self.ital

    def ar(self, et, ar):
        global i
        global j
        self.ar = ar
        et -= 1
        ar -= 1
        if 4 >= et >= 0:
            for i in range(len(AR)):
                for j in range(len(AR[i])):
                    if et == i:
                        if ar == j:
                            self.ar = ""
                            self.ar = AR[i][j]
        return self.ar

    def print_nev(self):
        print("A menü: ", self.nev, "!")


class Nyitvatartás(Étterem):
    def __init__(self, nyitashk=8, nyitashv=10, zarashk=22, zarashv=20):
        global nyitva
        nyitva = False
        self.et = Étterem.__init__(self)
        self.nyitva = nyitva
        self.nyitashk = nyitashk
        self.nyitashv = nyitashv
        self.zarashk = zarashk
        self.zarashv = zarashv
        self.hetkoznap = str(self.nyitashk) + "-" + str(self.zarashk)
        self.hetvege = str(self.nyitashv) + "-" + str(self.zarashv)
        self.nyitva = False

    def Hétköznap(self):
        # print("A nyitvatartás hétköznap: ", self.hetkoznap, "!")
        return self.hetkoznap

    def Hétvége(self):
        # print("A nyitvatartás hétvégén: ", self.hetvege, "!")
        return self.hetvege

    """
    def Nyitva(self, hetnapja, ora):
        self.hetnapja = hetnapja
        self.ora = ora
        if self.hetnapja <= 4:
            if self.ora>=self.zarashk and self.ora<=self.zarashk:
                self.nyitva=True
        else:
            if self.ora>=self.nyitashv and self.ora<=self.nyitashv:
                self.nyitva=True
        return self.nyitva
    """



def Menu_4():
    return Menü().foetel(b, 4) + " " + Menü().koret(b, 4) + " " + Menü().ital(b, 4) + " " + Menü().ar(b, 4)


def Menu_3():
    return Menü().foetel(b, 3) + " " + Menü().koret(b, 3) + " " + Menü().ital(b, 3) + " " + Menü().ar(b, 3)


def Menu_2():
    return Menü().foetel(b, 2) + " " + Menü().koret(b, 2) + " " + Menü().ital(b, 2) + " " + Menü().ar(b, 2)


def Menu_1():
    return Menü().foetel(b, 1) + " " + Menü().koret(b, 1) + " " + Menü().ital(b, 1) + " " + Menü().ar(b, 1)


class Napok(Enum):  # Enum használat (primitív de van)
    Hétfő = 0
    Kedd = 1
    Szerda = 2
    Csütörtök = 3
    Péntek = 4
    Szombat = 5
    Vasárnap = 6


def Mai_Nap() -> str:  # (Ez a függvény nem akart classben működni)
    global i
    dt = int(datetime.today().weekday())
    for i in range(7):
        if i == dt:
            return Napok(i).name


def Nyitva(hetnapja, ora, nyitashk=8, nyitashv=10, zarashk=22, zarashv=20):  # (Ezse)
    global nyitva
    if hetnapja <= 4:
        if nyitashk <= ora <= zarashk:
            nyitva = True
    else:
        if nyitashv <= ora <= zarashv:
            nyitva = True
    return nyitva


def clear_screen():  # Grafikus megjelenítésen a tartalom törlése, mivel nem találtam label törlő lehetőséget
    a = 2
    g = 1
    Label(root, text="                                          ", font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    g += 1
    Label(root, text="                                          ", font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    g += 1
    Label(root, text="                                          ", font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    g += 1
    Label(root, text="                                          ", font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text="                     ", font=(text_type, ts)).grid(row=a, column=4)


def clear_menu():  # Grafikus megjelenítésen a tartalom törlése, mivel nem találtam label törlő lehetőséget
    a = 12
    Label(root, text="\n                                           \n                                           \n    "
                     "                                       \n                                           \n          "
                     "                                 \n                                           \n                "
                     "                           \n                                           \n                      "
                     "                     \n                                           \n                            "
                     "               \n",
          font=(text_type, ts)).grid(row=a, column=0)
    Label(root,
          text="\n                                           \n                                           \n          "
               "                                 \n                                           \n                      "
               "                     \n                                           \n                                  "
               "         \n                                           \n                                           \n "
               "                                          \n                                           \n",
          font=(text_type, ts)).grid(row=a, column=1)
    Label(root,
          text="\n                                           \n                                           \n          "
               "                                 \n                                           \n                      "
               "                     \n                                           \n                                  "
               "         \n                                           \n                                           \n "
               "                                          \n                                           \n",
          font=(text_type, ts)).grid(row=a, column=2)
    Label(root,
          text="\n                                           \n                                           \n          "
               "                                 \n                                           \n                      "
               "                     \n                                           \n                                  "
               "         \n                                           \n                                           \n "
               "                                          \n                                           \n",
          font=(text_type, ts)).grid(row=a, column=3)


def clear_10():
    a = 10
    Label(root,
          text="                                                                                                      ",
          font=(text_type, ts)).grid(row=a, column=0, columnspan=5)


def etlap_frissit():  # Ételek frissítése az éttermek közötti ugrálás után
    global b
    a = 2
    g = 1
    Label(root, text="1. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    g += 1
    Label(root, text="2. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    g += 1
    Label(root, text="3. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    g += 1
    Label(root, text="4. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)

    Label(root, text="                                      ", font=(text_type, ts)).grid(row=0, column=2)
    Label(root, text=Étterem().nev(b), font=(text_type, ts)).grid(row=0, column=2)


if rendelt > 0:  # Ha rendelt az adott étteremből akkor kiírja az étterem nevét
    with io.open(txt_file, "w", encoding=encoding_out) as fki:
        fki.write(Étterem().nev(b) + "\n")
        rendelt = 0


def kepernyo():  # A grafikus felület megjelenítése
    global c
    global Menu5_3
    global Menu5_2
    global Menu5_1
    clear_menu()
    hetnapjaa = int(datetime.today().weekday())
    oraa = int(datetime.now().strftime("%H"))
    FontOfEntryList = tkf.Font(family=text_type_entry, size=text_size_entry)

    tk.StringVar()
    tk.StringVar()
    tk.StringVar()
    a = 0

    Button(root, text="Fizetés", padx=x, pady=y, command=grandtotal, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=5)

    Button(root, text="<", padx=x, pady=y, command=b_csokkento, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Étterem().nev(b), font=(text_type, ts)).grid(row=a, column=2)
    Button(root, text=">", padx=x, pady=y, command=b_novelo, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    Label(root, text="Mai nap:\n" + Mai_Nap(), font=(text_type, ts)).grid(row=a, column=5)
    Label(root, text="Menü:", font=(text_type, ts)).grid(row=a, column=0)
    a += 1
    g = 1
    Label(root, text="1. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)

    if Nyitva(hetnapjaa, oraa):
        Label(root, text="Nyitva", font=(text_type, ts), fg=Important_text_color).grid(row=a, column=5)
    else:
        Label(root, text="Zárva", font=(text_type, ts), fg=Important_text_color).grid(row=a, column=5)
    a += 1
    g += 1
    Label(root, text="2. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)

    a += 1
    g += 1
    Label(root, text="3. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)

    a += 1
    g += 1
    Label(root, text="4. Menü: ", font=(text_type, ts)).grid(row=a, column=0)
    Label(root, text=Menü().foetel(b, g), font=(text_type, ts)).grid(row=a, column=1)
    Label(root, text=Menü().koret(b, g), font=(text_type, ts)).grid(row=a, column=2)
    Label(root, text=Menü().ital(b, g), font=(text_type, ts)).grid(row=a, column=3)
    Label(root, text=Menü().ar(b, g), font=(text_type, ts)).grid(row=a, column=4)

    a += 1
    Label(root, text="Saját:", font=(text_type, ts)).grid(row=a, column=0)

    a += 1
    Menu5_1 = Entry(root, font=FontOfEntryList, justify=justify_entry, width=width_entry, bg=bg_entry, fg=fg_entry,
                    disabledbackground=disabledbackground_entry, disabledforeground=disabledforeground_entry,
                    highlightbackground=highlightbackground_entry, highlightcolor=highlightcolor_entry,
                    highlightthickness=highlightthickness_entry, bd=bd_entry)
    Menu5_1.grid(row=a, column=0, padx=x, pady=y, ipady=y)
    Menu5_1.insert(0, "Fő étel")
    # entry0.set("Főétel")
    Menu5_2 = Entry(root, font=FontOfEntryList, justify=justify_entry, width=width_entry, bg=bg_entry, fg=fg_entry,
                    disabledbackground=disabledbackground_entry, disabledforeground=disabledforeground_entry,
                    highlightbackground=highlightbackground_entry, highlightcolor=highlightcolor_entry,
                    highlightthickness=highlightthickness_entry, bd=bd_entry)
    Menu5_2.grid(row=a, column=1, padx=x, pady=y, ipady=y)
    Menu5_2.insert(0, "Köret")
    Menu5_3 = Entry(root, font=FontOfEntryList, justify=justify_entry, width=width_entry, bg=bg_entry, fg=fg_entry,
                    disabledbackground=disabledbackground_entry, disabledforeground=disabledforeground_entry,
                    highlightbackground=highlightbackground_entry, highlightcolor=highlightcolor_entry,
                    highlightthickness=highlightthickness_entry, bd=bd_entry)
    Menu5_3.grid(row=a, column=2, padx=x, pady=y, ipady=y)
    Menu5_3.insert(0, "Innivaló")
    Button(root, text="Számít", padx=x, pady=y, command=Calculate, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=4)
    a += 1
    Button(root, text="1. Menü", padx=x, pady=y, command=Menu01, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=0)
    Button(root, text="2. Menü", padx=x, pady=y, command=Menu02, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=1)
    Button(root, text="3. Menü", padx=x, pady=y, command=Menu03, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=2)
    Button(root, text="4. Menü", padx=x, pady=y, command=Menu04, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=3)
    Button(root, text="Saját Menü", padx=x, pady=y, command=sajatmenu, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=4)
    a += 1

    Button(root, text="Hétközbeni nyitvatartás", padx=x, pady=y, command=Menu05, fg=Text_color,
           bg=Bg_color, font=(text_type, ts)).grid(row=a, column=1)
    Button(root, text="Hétvégi nyitvatartás", padx=x, pady=y, command=Menu06, fg=Text_color,
           bg=Bg_color, font=(text_type, ts)).grid(row=a, column=2)
    a += 1
    c = a
    a += 1
    Button(root, text="Kilépés", padx=x, pady=y, command=root.quit, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=a, column=5)
    Button(root, text="Ételek, Italok", padx=x, pady=y, command=Ételek_Italok, fg=Text_color,
           bg=Bg_color, font=(text_type, ts)).grid(row=a, column=0)


def b_csokkento():  # Éttermek közötti ugrálás
    global b
    global rendelt
    global fki
    if b == 1:
        b = 4
    else:
        b = b - 1
    clear_screen()
    etlap_frissit()
    if rendelt > 0:
        with io.open(txt_file, "a", encoding=encoding_out) as fki:
            fki.write("\n" + Étterem().nev(b) + "\n")
        rendelt = 0


def b_novelo():  # Éttermek közötti ugrálás
    global b
    global rendelt
    global fki
    if b == 4:
        b = 1
    else:
        b += 1
    clear_screen()
    etlap_frissit()

    Label(root, text="                                      ", font=(text_type, ts)).grid(row=0, column=2)
    Label(root, text=Étterem().nev(b), font=(text_type, ts)).grid(row=0, column=2)
    # print(b)
    if rendelt > 0:
        with io.open(txt_file, "a", encoding=encoding_out) as fki:
            fki.write("\n" + Étterem().nev(b) + "\n")
        rendelt = 0


def Calculate():  # Saját menü számítása
    global elem
    global Menu5_1
    global Menu5_2
    global Menu5_3
    global Ár
    entry0 = Menu5_1.get()
    entry1 = Menu5_2.get()
    entry2 = Menu5_3.get()
    Ár = 0
    for elem in matrix0:
        try:
            if entry0.lower() == elem[0] + " " + elem[1]:
                Ár += int(elem[2])
        except IndexError:
            break
    for eleme in matrix0:
        if entry1.lower() == eleme[0]:
            Ár += int(eleme[1])
        elif entry2.lower() == eleme[0]:
            Ár += int(eleme[1])

    válasz = ("Rendelés: \n" + entry0 + " " + "\n" + entry1 + " " + entry2 + "\n Ár: " + str(Ár) + "Ft")

    Label(root, text=válasz, font=(text_type, ts)).grid(row=6, rowspan=2, column=3)
    if Ár != 0:
        return True
    else:
        return False

def sajatmenu():  # Saját menü meg
    global c
    clear_menu()
    Menu5_1.get()
    Menu5_2.get()
    Menu5_3.get()
    if Calculate():
        clear_10()
        Label(root, text="A rendelés elfogadva", font=(text_type, ts)).grid(row=c, columnspan=5)
    else:
        clear_10()
        Label(root, text="Nincs Étel/Köret/Ital kiválasztva", font=(text_type, ts)).grid(row=c, columnspan=5)
    sajatmenu.foetel = Menu5_1.get()
    sajatmenu.koret = Menu5_2.get()
    sajatmenu.ital = Menu5_3.get()
    sajatmenu.ar = str(Ár) + "Ft"
    kiir()


def kiir():  # Sajátmenü fájlbaírása
    global fki
    with io.open(txt_file, "a", encoding=encoding_out) as fki:
        fki.write(sajatmenu.foetel + " " + sajatmenu.koret + " " + sajatmenu.ital + " " + sajatmenu.ar + "\n")
    # fki.write()
    return sajatmenu.foetel, sajatmenu.koret, sajatmenu.ital, sajatmenu.ar


# A gombok függvényei:
def Menu01():
    global rendelt
    global fki
    global sor
    rendelt += 1
    clear_10()
    a = 10
    # print(Menü().Menu_3())
    for sor in Menu_1():
        with io.open(txt_file, "a", encoding=encoding_out) as fki:
            fki.write(sor)
    with io.open(txt_file, "a", encoding=encoding_out) as fki:
        fki.write("\n")
    Label(root, text="Az első menüt választotta!", font=(text_type, ts)).grid(row=a, columnspan=5)


def Menu02():
    global rendelt
    global fki
    global sor
    rendelt += 1
    a = 10
    clear_10()
    # print(Menü().Menu_2())
    for sor in Menu_2():
        with io.open(txt_file, "a", encoding=encoding_out) as fki:
            fki.write(sor)
    with io.open(txt_file, "a", encoding=encoding_out) as fki:
        fki.write("\n")
    Label(root, text="A második menüt választotta!", font=(text_type, ts)).grid(row=a, columnspan=5)


def Menu03():
    global rendelt
    global fki
    global sor
    rendelt += 1
    a = 10
    clear_10()
    # print(Menü().Menu_3())
    for sor in Menu_3():
        with io.open(txt_file, "a", encoding=encoding_out) as fki:
            fki.write(sor)
    with io.open(txt_file, "a", encoding=encoding_out) as fki:
        fki.write("\n")

    Label(root, text="A harmadik menüt választotta!", font=(text_type, ts)).grid(row=a, columnspan=5)


def Menu04():
    global rendelt
    global fki
    global sor
    rendelt += 1
    a = 10
    clear_10()
    # print(Menu_4())
    for sor in Menu_4():
        with io.open(txt_file, "a", encoding=encoding_out) as fki:
            fki.write(sor)
    with io.open(txt_file, "a", encoding=encoding_out) as fki:
        fki.write("\n")
    Label(root, text="A negyedik menüt választotta!", font=(text_type, ts)).grid(row=a, columnspan=5)


def Menu05():
    clear_10()
    a = 10
    Label(root, text="A nyitvatartás hétköznap: {0}".format(Nyitvatartás().Hétköznap()),
          font=(text_type, ts)).grid(row=a, columnspan=5)


def Menu06():
    clear_10()
    a = 10
    Label(root, text="A nyitvatartás hétvégén: {0}".format(Nyitvatartás().Hétvége()),
          font=(text_type, ts)).grid(row=a, columnspan=5)


def Ételek_Italok():  # A lehetséges választható Ételek és Italok megjelenítése és eltüntetése függvény
    global nyitvaa
    global sor

    c = 12
    clear_menu()
    oszlop_0 = ""
    oszlop_1 = ""
    oszlop_2 = ""
    oszlop_3 = ""
    ""
    db = 0
    for sor in matrix0:
        if len(sor) == 3:
            if db < 6:
                oszlop_0 += sor[0] + " " + sor[1] + " \n " + sor[2] + "Ft\n"
            elif 6 <= db < 11:
                oszlop_1 += sor[0] + " " + sor[1] + " \n " + sor[2] + "Ft\n"
            elif 11 <= db < 16:
                oszlop_2 += sor[0] + " " + sor[1] + " \n " + sor[2] + "Ft\n"
            elif db >= 16:
                oszlop_3 += sor[0] + " " + sor[1] + " \n " + sor[2] + "Ft\n"
        else:
            if db < 6:
                oszlop_0 += sor[0] + " " + sor[1] + " - " + sor[2] + "Ft\n"
            elif 6 <= db < 11:
                oszlop_1 += sor[0] + " - " + sor[1] + "Ft\n"
            elif 11 <= db < 16:
                oszlop_2 += sor[0] + " - " + sor[1] + "Ft\n"
            elif 16 <= db < 20:
                oszlop_3 += sor[0] + " - " + sor[1] + "Ft\n"
        db += 1
    Label(root, text=oszlop_0, font=(text_type, ts)).grid(row=c, column=0)
    Label(root, text=oszlop_1, font=(text_type, ts)).grid(row=c, column=1)
    Label(root, text=oszlop_2, font=(text_type, ts)).grid(row=c, column=2)
    Label(root, text=oszlop_3, font=(text_type, ts)).grid(row=c, column=3)
    if nyitvaa == 0:
        nyitvaa = 1
    elif nyitvaa == 1:
        nyitvaa = 0
        clear_menu()
    # Label(root, text= ,font=(text_type, ts)).grid(row=c,column=3)


def grandtotal():  # Végső Fizetendő Ár kiszámító a Rendelés file-ból
    global c
    global sor
    global elem
    global kis_lista
    clear_menu()

    lista = []
    fbe = open(txt_file, "r")
    for sor in fbe:
        kis_lista = []
        sor = sor.strip().split()
        for elem in sor:
            kis_lista.append(elem)
        lista.append(kis_lista)
    global grand_total
    grand_total = 0
    clear_menu()
    try:
        for sor in lista:
            if len(sor) > 4:
                if sor[4] != "0Ft":
                    if len(sor[4]) > 5:
                        # print(int(sor[4][:4]))
                        grand_total += int(sor[4][:4])
                    else:
                        print(int(sor[4][:3]))
                        grand_total += int(sor[4][:3])
    except IndexError:
        for sor in lista:
            if len(sor) > 3:
                if sor[3] != "0Ft":
                    if len(sor[3]) > 4:
                        # print(int(sor[3][:3]))
                        grand_total += int(sor[3][:4])
                    else:
                        print(int(sor[3][:3]))
                        grand_total += int(sor[3][:3])
    Label(root, text=str(grand_total) + "Ft fizetendő a futárnál", font=(text_type, ts)).grid(row=c,
                                                                                              columnspan=5)
    c += 1
    Button(root, text="Megrendelem", padx=x, pady=y, command=Megrendelem, fg=Text_color, bg=Bg_color,
           font=(text_type, ts)).grid(row=c, column=2)

    Button(root, text="Rendelés törlése", padx=x, pady=y, command=Rendeles_torles, fg=Text_color,
           bg=Bg_color, font=(text_type, ts)).grid(row=c, column=1)


def Megrendelem():  # Végső Fizetendő Ár kiszámító a Rendelés file-ból
    os.startfile(txt_file)
    root.destroy()


def Rendeles_torles():  # Rendelés törlése és Visszaigazolás
    global c
    c -= 1
    clear_menu()
    clear_10()
    os.remove(txt_file)
    Label(root, text="A Rendelés törlésre került!", font=(text_type, ts)).grid(row=c, columnspan=5)
    a = 11
    Label(root,
          text="\n                                                                                           \n       "
               "                                                                                    ",
          font=(text_type, ts)).grid(row=a, column=1, columnspan=2)


"""  ***DEBUG***
print(matrix)
print(matrix0)
print(matrix1)
print(Ettermek)
print(Foetelek)
print(Koretek)
print(Italok)
print(AR)
"""

if __name__ == "__main__":  # Main függvény: Emódon futtatható a program console ból illetve EXE/Batch fileként
    kepernyo()
    root.mainloop()
    fki.close()
    quit()
