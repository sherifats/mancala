binAmount = [4,4,4,4,4,4,0,4,4,4,4,4,4,0]

playing = True

while (playing):
    
    i = 0
    
    for element in binAmount:
        binAmount[i] = int(binAmount[i])
        if int(binAmount[i]) < 10:
            binAmount[i] = " "+str(binAmount[i])
        else:
            binAmount[i] = str(binAmount[i])
        i += 1

    print("+-----+-----+-----+-----+-----+-----+-----+-----+")
    print("|     | "+binAmount[12]+"  | "+binAmount[11]+"  | "+binAmount[10]
          +"  | "+binAmount[9]+"  | "+binAmount[8]+"  | "+binAmount[7]+"  |     |")
    print("| "+binAmount[13]+"  +-----+-----+-----+-----+-----+-----+ "+binAmount[6]+"  |")
    print("|     | "+binAmount[0]+"  | "+binAmount[1]+"  | "+binAmount[2]
          +"  | "+binAmount[3]+"  | "+binAmount[4]+"  | "+binAmount[5]+"  |     |")  
    print("+-----+-----+-----+-----+-----+-----+-----+-----+")

    userInput = input("Enter 'q' to quite the game")
    if userInput == "q":
        playing = False
    
    #playing = False
####END OF WHILE PLAYING LOOP####