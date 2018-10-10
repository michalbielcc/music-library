new_entries = []

def add_new_album():
    a = input('Enter artist name: ').lower()
    new_entries.append(str(a.title()))
    new_entries.append(',')

    b = input('Enter album name: ').lower()
    new_entries.append(str(b.title()))

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
            x = int(e[-2])
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
            
    new_entries.extend((',', c, ',', d, ',', e, ',', '\n'))


    export_file(new_entries, input)

        
def another():
    a = input('Want to add another one? [ 1 ] for yes ')
    while a == '1':
        add_new_album()
    else:
        pass  


def export_file(new_entries, input):
    x = input('Export to local library [ 1 ] or external file [ 2 ]? : ')
    if x == '1':
        y = open('text_albums_data.txt', 'a')
        for i in new_entries:
            y.write(i)
        y.close()
        another()


    if x == '2':
        x = input('Enter file name: ')
        y = open(str(x), 'w')
        for i in new_entries:
            y.write(i)
        y.close()   
        another()

    else:
        pass

add_new_album()
