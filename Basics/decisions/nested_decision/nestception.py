print("Where should I look?")
place = str(input())

if place == "in the bedroom":

    print("Where in the bedroom should I look?")
    room = str(input())

    if room == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

elif place == "in the bathroom":

    print("Where in the bathroom should I look?")
    toilet = str(input())

    if toilet == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")

elif place == "in the lab":

    print("Where in the lab should I look?")
    lab = str(input())

    if lab == "on the table":
        print("Yes! I found my battery")
    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but I will keep looking")

