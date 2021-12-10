A program config.ini fájljában állíthatóak a grafikus felület tulajdonságai \
A Beadandó nevü fájlhoz tartozik az Ettermek,\
Rendeles és Prices txt fájl melyek módosításával módosul a program adatbázisa

A Beadando.exe fájl a python file-ból lett legenerálva auto-py-to-exe segítségével!\
Futttatható fájl, a beállításai változtathatók a config fájlon keresztül!

***config.ini***:

<span style="color: orange">[root]</span>\
root_title=Etelrendeles\
root_icon=my_ico.ico

<span style="color: orange">[my_files]</span>\
txt_file = Rendeles.txt\
input_file = Ettermek.txt\
input_file0 = Prices.txt\
encoding_in = utf-8\
encoding_out = utf-8

<span style="color: orange">[Text]</span>\
Text_size = 20\
text_type = Arial\
Text_color = blue\
Bg_color = white\
Important_text_color = Red\
text_justify = center

<span style="color: orange">[Entry]</span>\
justify_entry = center\
text_type_entry = Arial\
text_size_entry = 20\
width_entry = 18\
bg_entry = white\
fg_entry = orange\
disabledforeground_entry = red\
disabledbackground_entry = red\
highlightbackground_entry = black\
highlightcolor_entry = blue\
highlightthickness_entry = 1\
bd_entry = 0

<span style="color: orange">[other]</span>\
Buttonsize_x = 40\
Buttonsize_y = 10

Fullscreen = True\
custom_resolution = 1920x1080

Opciók átállításával lehet változtatni a program megjelenítésében

A futtatásnál fontos, hogy a Scale a Windows-ban 100%\
és a felbontás 1920x1080 legyen különben,\
a config.ini ben változtatásokat kell ejteni!