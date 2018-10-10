from music_reports import music


print(music)

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






find_by_artist()