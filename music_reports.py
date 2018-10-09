from tabulate import tabulate
music = []

def import_music(music, filename='text_albums_data.txt'):
    txt = open(filename, 'r')
    music1 = []
    for line in txt:
        i = line.split(',')
        music1.append(i)
    for i in music1:
        music.append(i)
    txt.close()

import_music(music, filename='text_albums_data.txt')





print(tabulate(music,["Artist","Album", "Year", "Genre", "Time",""]))


