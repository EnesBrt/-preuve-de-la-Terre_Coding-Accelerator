# 12 to 24

import sys


def to_mimitary_time(time):
    if time[:2] == "12" and time[5:7] == "AM":
        print("00" + time[2:-2])
    elif time[:2] == "12" and time[5:7] == "PM":
        print(time[:-2])
    elif "01" <= time[:2] <= "11" and time[5:7] == "AM":
        print(time[:-2])
    elif "01" <= time[:2] <= "11" and time[5:7] == "PM":
        print(str(int(time[:2]) + 12) + time[2:-2])


if len(sys.argv) > 2:
    print("Erreur : Veuillez entrer qu'un seul argument..")
elif len(sys.argv) == 2:
    message = sys.argv[1]
    to_mimitary_time(message)
else:
    print("Erreur : Veuillez entrer qu'un seul argument..")
