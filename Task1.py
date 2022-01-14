name = input("What is your name: ")
if name == "Arthur":
    print("You may pass")
else:
    quest = input("What is your quest? ")
    if quest != "Grail" and quest != "grail": 
        print("Only those who seek the grail may pass")
    else:
        color = input("What is you favroit color: ")
        if color[0] == name[0]:
            print("You may pass")
        else:
            print("Incorrect! You must now face the gorge of Eternal Peril")
