music = [['Pink Floyd', 'The Dark Side Of The Moon', '1973', 'progressive rock', '43:00', '\n'], ['Britney Spears', 'Baby One More Time', '1999', 'pop', '42:20', '\n'], ['The Beatles', 'Revolver', '1966', 'rock', '34:43', '\n'], ['Deep Purple', 'Machine Head', '1972', 'hard rock', '37:25', '\n'], ['Old Timers', 'Old Time', '1966', 'ancient', '123:45', '\n'], ['Pink Floyd', 'Wish You Were Here', '1975', 'progressive rock', '44:28', '\n'], ['Boston', 'Boston', '1976', 'hard rock', '37:41', '\n'], ['Monika Brodka', 'Granada', '2010', 'pop', '37:42', '\n'], ['David Bowie', 'Low', '1977', 'rock', '38:26', '\n'], ['Massive Attack', 'Blue Lines', '1991', 'hip hop', '45:02', '\n']]
genre_list = []
time_list = []

def find_genre(genre):
    genre_list1 = []
    for x in music:
        if genre in x:
            genre_list1.append(x)

    for i in genre_list1:
        genre_list.append(i)

#find_genre('pop')





def find_time_range(year, year2):
    time_list1 = []
    for x in music:
        if int(x[2]) in range(int(year), int(year2)+1):
            time_list1.append(x)

    for i in time_list1:
        time_list.append(i)    

find_time_range('1972','1973')

print(time_list)

def find_longest_shortest():
    
