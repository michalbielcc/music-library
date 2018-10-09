
from tabulate import tabulate
from music_reports import music

print(tabulate(music,["Artist","Album", "Year", "Genre", "Time",""]))