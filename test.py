
from tabulate import tabulate
music = []
genre_list = []
time_list = []
length_list = []
longest_shortest = []
all_genres = []
oldest_youngest = []
count_by_genre_list = []
count_by_genre_set = set(count_by_genre_list)




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



print(music)





def find_all_genres():
    for x in music:
        all_genres.append(x[3])



def find_genre(genre):
    for x in music:
        if genre in x:
            genre_list.append(x)


#find_genre('pop')
#print(genre_list)

def find_time_range(year, year2):
    for x in music:
        if int(x[2]) in range(int(year), int(year2)+1):
            time_list.append(x)



def find_time_range(year, year2):
    for x in music:
        if int(x[2]) in range(int(year), int(year2)+1):
            time_list.append(x)

  

#find_time_range('1972','1973')
#print(time_list)

def find_longest_shortest():
    length_list1 = []
    length_list2 = []
    for x in music:
        length_list1.append(x[4])
    for x in length_list1:
        y = x.split(':')
        x = ''.join(y)
        length_list2.append(int(x))

    length_list1 =  sorted(length_list2)
    print(length_list1)

    min = list(str(length_list1[0]))
    min.insert(-2, ':')
    min = ''.join(min)
    for x in music:
        if x[4] == min:
            longest_shortest.append(x)


    max = list(str(length_list1[-1]))
    max.insert(-2, ':')
    max = ''.join(max)
    for x in music:
        if x[4] == max:
            longest_shortest.append(x)

#find_longest_shortest()
#print(longest_shortest)





    

def find_longest_shortest():
    length_list1 = []
    length_list2 = []
    for x in music:
        length_list1.append(x[4])
    for x in length_list1:
        y = x.split(':')
        x = ''.join(y)
        length_list2.append(int(x))

    length_list1 =  sorted(length_list2)
    min = list(str(length_list1[0]))
    min.insert(-2, ':')
    min = ''.join(min)
    for x in music:
        if x[4] == min:
            longest_shortest.append(x)

    max = list(str(length_list1[-1]))
    max.insert(-2, ':')
    max = ''.join(max)
    for x in music:
        if x[4] == max:
            longest_shortest.append(x)


def find_by_album():

    search = input("Album: ")

    for i in music:
        if search in i[1]:
            print("Album: ", i)
            AskAgain = input("wanna search again? Press y for yes or n for no ")
            if AskAgain == "y":
                find_by_album()
            if AskAgain == "n":
                print("ide do menu")
                main()

    if search not in music:
        print("Type album correctly")
        find_by_album()

def find_by_artist():

    search = input("Type artist name: ")

    for i in music:
        if search in i[0]:
            print("Album: ", i)
            AskAgain=input("wanna search again? Press y for yes or n for no ")

            if AskAgain == "y":
                find_by_artist()
            if AskAgain == "n":
                print("ide do menu")

    if search not in music:
        print("Type name correctly")
        find_by_artist()

def oldest_youngest_album():
    oldest_youngest1 = []
    for x in music:
        oldest_youngest1.append(int(x[2]))
    sorted(oldest_youngest).append(x[0])
    sorted(oldest_youngest).append(x[-1])



#find_longest_shortest()
#print(longest_shortest)

def count_by_genre():
    for x in music:
        count_by_genre_list.append(x[3])
    for x in count_by_genre_list:
        count_by_genre_set.add(x)




def main():

    print('''Welcome to music library!

    Press 1 to display full content of database
    Press 2 to display album sorted by genres
    Press 3 to display albums within given time frame
    Press 4 to find longest and shortest album
    Press 5 to find albums by artist
    Press 6 to find album by its name
    press 7 to display full report on database
    ''')
    choice = input('Enter number: ')

    if choice == '1':
        print(tabulate(music,["Artist","Album", "Year", "Genre", "Time"]))

        if input("Do you want back to menu? y for yes, n for no") == "y":
            main()
        else:
            print("Good bye :) ")

    if choice == '2':
        find_all_genres()
        print('Music genres in database:')
        for x in all_genres:
            print(x)
        a = input('Enter genre: ')
        find_genre(a)
        print(tabulate(genre_list, ["Artist", "Album", "Year", "Genre", "Time"]))
        SearchGenreAsk = input("Do you want back to menu? y for yes, n for no")
        if SearchGenreAsk == "y":
            main()
        if SearchGenreAsk == "n":
            print("Good Bye")





    if choice == '3':
        year = input(' Enter starting date(year): ')
        year2 = input(' Enter ending date (year): ')
        find_time_range(year, year2)
        print(tabulate(time_list, ["Artist", "Album", "Year", "Genre", "Time"]))


        SearchYearAsk = input("Do you want back to menu? y for yes, n for no")
        if SearchYearAsk == "y":
            main()
        if SearchYearAsk == "n":
            print("Good Bye")



    if choice == '4':
        find_longest_shortest()
        print(longest_shortest)

    if choice == '5':
        find_by_artist()

    if choice == "6":
        find_by_album()

    if choice == '7':
        print('The longest and shortest albums are:')
        find_longest_shortest()
        print(longest_shortest)
        print('The oldest and youngest albums are:')
        oldest_youngest_album()
        print(oldest_youngest)
        print('Number of albums in database: ', end = '')
        album_count()
        print('Albums count by genre:')
        count_by_genre()


main()
