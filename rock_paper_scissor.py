import random
restart = True
while restart:
    list = ["rock", "paper", "scissors"]

    randnum = random.randrange(0,len(list))

    user = str(input("Input rock, paper, or scissors: ")).lower()
    
    x = True
    while x:
        if user not in list:
            print("Uh oh! You did not type in one of the options! Please try again")
            user = str(input("Input rock, paper, or scissors: ")).lower()
        else:
            x = False

    print("The Robot had played:" , str(list[randnum]))
    loss = str(list[randnum]) + " beats " + user + " You have Lost!"


    win = user + " beats " + str(list[randnum]) + " You have Won!"

    if user == str(list[randnum]):
        print("You have Tied")

    if user == "rock":
        if randnum == 1:
            #Rock loses to paper
            print(loss)
        elif randnum == 2:
            #Rock beats scissors
            print(win)

    if user == "paper":
        if randnum == 0:
            #Paper beats rock
            print(win)
        elif randnum == 2:
            #Paper loses to scissors
            print(loss)

    if user == "scissors":
        if randnum == 0:
            print(loss)
        elif user == 1:
            print(win)
    o = True   
    while o:     
        ask = str(input("Do you want to play again? Type yes or no!")).lower()
        if ask == "yes":
            restart = True
            o = False
        elif ask == "no":
            restart = False
            o = False
        else:
            print("this was not an option")
            

