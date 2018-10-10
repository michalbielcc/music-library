from tabulate import tabulate
music = []

def import_music(music, filename='text_albums_data.txt'):
    txt = open(filename, 'r')
    music1 = []
    for line in txt:
        i = line.split(',')
        music1.append(i)
    for i in music1:
        del i[-1]
    for i in music1:
        music.append(i)
    txt.close()

import_music(music, filename='text_albums_data.txt')

genre_list = []
time_list = []

def find_genre(genre):
    genre_list1 = []
    for x in music:
        if genre in x:
            genre_list1.append(x)

    for i in genre_list1:
        genre_list.append(i)

find_genre('pop')


def find_by_album():
    search = input("Type your album: ")

    for i in music:
        if search in i[1]:
            print("Album: ", i)
            AskAgain = input("wanna search again? Press y for yes or n for no ")

            if AskAgain == "y":
                find_by_album()
            if AskAgain == "n":
                print("ide do menu")

    if search not in music:
        print("Type album correctly")
        find_by_album()


def find_by_artist():
    search = input("Type artist name: ")

    for i in music:
        if search in i[0]:
            print("Album: ", i)
            AskAgain = input("wanna search again? Press y for yes or n for no ")

            if AskAgain == "y":
                find_by_artist()
            if AskAgain == "n":
                print("ide do menu")

    if search not in music:
        print("Type name correctly")
        find_by_artist()


