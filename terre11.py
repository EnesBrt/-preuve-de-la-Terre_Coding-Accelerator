# 24 to 12

import sys


def to_am_pm(time):
    if time[:2] == "00":
        print("12" + time[2:] + " AM")
    elif time[:2] == "12":
        print(time + " PM")
    elif "01" <= time[:2] <= "11":
        print(time + " AM")
    elif "13" <= time[:2] < "24":
        hour = int(time[:2]) - 12
        formatted_hour = f"{hour:02d}"
        print(formatted_hour + time[2:] + " PM")


if len(sys.argv) > 2:
    print("Erreur : Veuillez entrer un seul argument.")
elif len(sys.argv) == 2:
    message = sys.argv[1]
    to_am_pm(message)
else:
    print("Erreur : Veuillez entrer un argument.")

