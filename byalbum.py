from music_reports import music


print(music)

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


find_by_album()