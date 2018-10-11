music = []
new_entries = []
musicx = []

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


def edit(music, filename='text_albums_data.txt'):

    album_list = []

    import_music(music, filename='text_albums_data.txt')

    for i in music:
        album_list.append(i[1])
    for i in album_list:
        print(i)
        
    search = input('Enter name of album You want to edit: ').lower().title()

    while search not in album_list:
        search = input('Name does not apear in database, try again: ').lower().title()
        
        
    else:
        pass

    for i in music:
        if search in i[1]:
            index_of_album = music.index(i)
            print(index_of_album)
            music.remove(i)

            a = input('Enter artist name: ').lower()
            b = input('Enter album name: ').lower()

            while True:
                try:
                    c = int(input('Enter year of production: '))
                    c = str(c)
                    break
                except ValueError:
                    print('Numbers only please')

            d = input('Enter genre: ').lower()

            while True:
                try:

                    e = input('Enter length of album (format: minutes:seconds): ')
                    list(e)
                    x = int(e[-2:-1])
                    x = int(e[-1])
                    x = int(e[:-4])

                    if int(e[-2] + e[-1]) >= 60:
                        print('A minute part can\'t exceed the value of 59')
                        continue
                    else:
                        pass

                    if e[-3] == ':':
                        pass
                    else:
                        continue
                    
                    
                    break
                except ValueError:
                    print('Please submit time in given format: minutes:seconds')
                                    
            new_entries.extend(((str(a.title())), (str(b.title())), c, d, e))            
            music.insert(index_of_album , new_entries)
            
            for i in music:
                musicx.append((','.join(i))+','+'\n')
    
            music_file = open('text_albums_data.txt', 'w')
            for i in musicx:
                music_file.write(i)
            music_file.close()
            a = input('Want to edit another one? [ 1 ] for yes ')
            while a == '1':
                add_new_album()
            else:
                pass  
        
edit(music, filename='text_albums_data.txt')



