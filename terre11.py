# 24 to 12
import sys


def to_am_pm(time):

    if time[:2] == "00":
        print("12" + time[2:] + "AM")
    elif time[:2] == "12":
        print(time + "PM")
    elif "01" <= time[:2] <= "11":
        print( time + "AM")
    elif "13" <= time[:2] < "24":
        print("0" + str(int(time[:2]) - 12) + time[2:] + "PM")


if len(sys.argv) > 2:
    print("Erreur : Veuillez fournir un seul élement en tant qu'argument.")
elif len(sys.argv) == 2:
    message = sys.argv[1]
    to_am_pm(message)
else:
    print("Erreur : Veuillez fournir un seul message en tant qu'argument.")
