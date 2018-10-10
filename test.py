music = [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00'], ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20'], ['The Beatles', 'Revolver', '1966', 'rock', '34:43'], ['Deep Purple', 'Machine Head', '1972', 'hard rock', '37:25'], ['Old Timers', 'Old Time', '1966', 'ancient', '123:45'], ['Pink Floyd', 'Wish You Were Here', '1975', 'progressive rock', '44:28'], ['Boston', 'Boston', '1976', 'hard rock', '37:41'], ['Monika Brodka', 'Granada', '2010', 'pop', '37:42'], ['David Bowie', 'Low', '1977', 'rock', '38:26'], ['Massive Attack', 'Blue Lines', '1991', 'hip hop', '45:02']]

genre_list = []
time_list = []
length_list = []
longest_shortest = []
all_genres = []
oldest_youngest = []


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
    search=input("Type your album: ")
    for i in music:
        if search in i[1]:
            print("Album: ", i)
            AskAgain=input("wanna search again? Press y for yes or n for no ")
            if AskAgain=="y":
                find_by_album()
            else:
                print("ide do menu")
                break


def oldest_youngest_album():
    oldest_youngest1 = []
    for x in music:
        oldest_youngest1.append(int(x[2]))
    sorted(oldest_youngest).append(x[0])
    sorted(oldest_youngest).append(x[-1])



#find_longest_shortest()
#print(longest_shortest)


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
        print(tabulate(music,["Artist","Album", "Year", "Genre", "Time",""]))

    if choice == '2':
        find_all_genres()
        print('Music genres in database:')
        for x in all_genres:
            print(x)
        a = input('Enter genre: ')
        find_genre(a)

    if choice == '3':
        year = input(' Enter starting date(year): ')
        year2 = input(' Enter ending date (year): ')
        find_time_range(year, year2)
        print(time_list)

    if choice == '4':
        find_longest_shortest()
        print(longest_shortest)

    if choice == '5':
        

    if choice == '6'
        find_by_album()

    if choice == '7':
        find_longest_shortest()





main()



    longest album, shortest album, oldest album, youngest album, all
albums count + additional info, how many albums are given the genres
