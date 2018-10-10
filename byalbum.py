from music_reports import music

print(music)

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

    if search not in music:
        print("Type album correctly")
        find_by_album()

find_by_album()