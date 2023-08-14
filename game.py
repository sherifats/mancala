binAmount = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]

playing = True

playerOne = True

messageCode = 0

while (playing):
    

    if playerOne and messageCode ==0:
        message = "Plaayer One's turn..."
    elif not(playerOne) and messageCode == 0:
        message = "Player Two's turn..."
    elif playerOne and messageCode == -1:
        message = "Invalid input. Try again, Player One."
    elif not(playerOne) and messageCode == -1:
        message = "Invalid inout. Try again, Player Two."
    elif (playerOne) and messageCode == -2:
        message = "You must choose a non-empty bin, Player One."
    elif not(playerOne) and messageCode == -2:
        message = "You must choose a non-empty bin, Player Two."

    print("")
    print(message)
    print("")
    messageCode = 0

    i = 0
    for element in binAmount:
        binAmount[i] = int(binAmount[i])
        if int(binAmount[i])<10:
            binAmount[i] = " "+str(binAmount[i])
        else:
            binAmount[i] = str(binAmount[i])
        i += 1

    if not(playerOne):
        print("        a      b     c     d     e     f")

    print("+-----+-----+-----+-----+-----+-----+-----+-----+")
    print("|     | " + binAmount[12] + "  | " + binAmount[11] + "  | " 
          + binAmount[10] + "  | " + binAmount[9] + "  | " 
          + binAmount[8] + "  | " + binAmount[7] + "  |     |")
    print("| " + binAmount[13] + "  |-----|-----|-----|-----|-----|-----| " + binAmount[6] + "  |")
    print("|     | " + binAmount[0] + "  | " + binAmount[1] + "  | " + binAmount[2] 
          + "  | " + binAmount[3] + "  | " + binAmount[4] + "  | " 
          + binAmount[5] + "  |     |")
    print("+-----+-----+-----+-----+-----+-----+-----+-----+")
    
    if playerOne:
        print("        f      e      d     c     b    a")
    print("")
    
    chosenBin = 0
    userInput = input("enter 'q' to quit the game: ")
    
    if userInput == 'q':
        playing = False
        chosenBin = 0
    elif playerOne and userInput == "a":
        chosenBin = 5
    elif playerOne and userInput == "b":
        chosenBin = 4
    elif playerOne and userInput == "c":
        chosenBin = 3
    elif playerOne and userInput == "d":
        chosenBin = 2
    elif playerOne and userInput == "e":
        chosenBin = 1
    elif playerOne and userInput == "f":
        chosenBin = 0
    elif not(playerOne) and userInput == "a":
        chosenBin = 12
    elif not(playerOne) and userInput == "b":
        chosenBin = 11
    elif not(playerOne) and userInput == "c":
        chosenBin = 10
    elif not(playerOne) and userInput == "d":
        chosenBin = 9
    elif not(playerOne) and userInput == "e":
        chosenBin = 8
    elif not(playerOne) and userInput == "f":
        chosenBin = 7
    else:
        chosenBin = -1
        messageCode = -1 # invalid input

    if int(chosenBin) >=0:
        giveAwayPile = binAmount[chosenBin]
        binAmount[chosenBin] = 0
        if int(giveAwayPile) > 0:
            playerOne = not(playerOne)
        else:
            messageCode = -2 #empty bin was chosen
    
    recipient = chosenBin + 1
    while(int(giveAwayPile) > 0):
        if(playerOne and int(recipient) == 13):
            recipient = 0
        if(not(playerOne) and int(recipient) == 6):
            recipient = 7

        binAmount[recipient] = int(binAmount[recipient]) + 1
        giveAwayPile = int(giveAwayPile) - 1
        
        
        if int(giveAwayPile) == 0:
            lastRecipient = recipient
        else:
            recipient = int(recipient) + 1
            if int(recipient) > 13:
                recipient = 0

    if(playerOne and int(lastRecipient) == 6):
        playerOne = True
    elif(not(playerOne) and int(lastRecipient) == 13):
        playerOne = False
    else:
        playerOne = not(playerOne)
    
####END OF WHILE PLAYING LOOP####