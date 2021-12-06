A program config.ini fájljában állíthatóak a grafikus felület tulajdonságai \
A Beadandó nevü fájlhoz tartozik az Ettermek,\
Rendeles és Prices txt fájl melyek módosításával módosul a program adatbázisa

***config.ini***:

[my_files]\
txt_file = Rendeles.txt\
input_file=Ettermek.txt\
input_file0=Prices.txt

[Text]\
Text_size=25\
text_type= Arial\
Text_color =blue\
Bg_color = white\
Important_text_color=Red

[Entry]\
justify_entry=center\
text_type_entry=Arial\
text_size_entry=22\
width_entry=18\
bg_entry=white\
fg_entry=red\
disabledforeground_entry=red\
disabledbackground_entry=red\
highlightbackground_entry=black\
highlightcolor_entry=blue\
highlightthickness_entry=1\
bd_entry=0

[other]\
Buttonsize_x=40\
Buttonsize_y=10

Fullscreen = True


Opciók átállításával lehet változtatni a program megjelenítésében

A bat file-t futtatva IDE nélkül is használható a rpogram.