import random

print("\n\nWelcome to Rock, Paper, Scissors, Lizzard, Spock by The Lonely Dash - based on the popular hand-game from The Big Bang Theory.")

win = 0
lose = 0
tie = 0

while True:
    print("\n")
    print("A. Rock")
    print("B. Paper")
    print("C. Scissors")
    print("D. Lizzard")
    print("E. Spock")
    print("F. QUIT\n")

    user_choice = (input("Choose your hand gesture: ")).lower()
    computer_choices = ["Rock", "Paper", "Scissors", "Lizzard", "Spock"]
    computer_input = random.choice(computer_choices)


    if user_choice == "a":
        if computer_input == "Rock":
            print("You chose Rock and the computer chose Rock!")
            print("It's a tie! You hear a CLACK as the rocks bounce off one another! Try again?")
            tie += 1
        elif computer_input == "Paper":
            print("You chose Rock and the computer chose Paper!")
            print("You lose! Paper covers Rock! Try again?")
            lose += 1    
        elif computer_input == "Scissors":
            print("You chose Rock and the computer chose Scissors!")
            print("You win! Those pesky Scissors are crushed by Rock! Congrats! Try again?")
            win += 1
        elif computer_input == "Lizzard":
            print("You chose Rock and the computer chose Lizzard!")
            print("You win! The poor Lizzard is crushed by your Rock. Congrats! Try again?")
            win += 1
        elif computer_input == "Spock":
            print("You chose Rock and the computer chose Spock!")
            print("You lose! Apparently, Spock has a phaser that vaporizes Rock. Try again?")
            lose += 1
    elif user_choice == "b":
        if computer_input == "Rock":
            print("You chose Paper and the computer chose Rock!")
            print("You win! Paper covers rock! Try again?")
            win += 1
        elif computer_input == "Paper":
            print("You chose Paper and the computer chose Paper!")
            print("You tie! Your limp papers smack into one another and nothing happens. Try again?")
            tie += 1    
        elif computer_input == "Scissors":
            print("You chose Paper and the computer chose Scissors!")
            print("You lose! Those pesky Scissors slice through your paper easily! Try again?")
            lose += 1
        elif computer_input == "Lizzard":
            print("You chose Paper and the computer chose Lizzard!")
            print("You lose! Lizzards eat paper?  Who knew? Try again?")
            lose += 1
        elif computer_input == "Spock":
            print("You chose Paper and the computer chose Spock!")
            print("You win! Your paper is most logical and defeats Spock easily! Congrats! Try again?")
            win += 1
    elif user_choice == "c":
        if computer_input == "Rock":
            print("You chose Scissors and the computer chose Rock!")
            print("You lose! Rock smashes your puny Scissors! Try again?")
            lose += 1
        elif computer_input == "Paper":
            print("You chose Scissors and the computer chose Paper!")
            print("You win! Your Scissors slice through paper like it's...well, Scissors cutting paper. Try again?")
            win += 1    
        elif computer_input == "Scissors":
            print("You chose Scissors and the computer chose Scissors!")
            print("You tie! The Scissors clash together like tiny little swords! Nothing happens. Try again?")
            tie += 1
        elif computer_input == "Lizzard":
            print("You chose Scissors and the computer chose Lizzard!")
            print("You win! SNIP!  Your scissors decapitate Henry the Lizzard.  He had a name you know...Try again?")
            win += 1
        elif computer_input == "Spock":
            print("You chose Scissors and the computer chose Spock!")
            print("You lose! Defying all logic, Spock smashes your Scissors. Try again?")
            lose += 1
    elif user_choice == "d":
        if computer_input == "Rock":
            print("You chose Lizzard and the computer chose Rock!")
            print("You lose! Rock smashes Henry the Lizzard! Try again?")
            lose += 1
        elif computer_input == "Paper":
            print("You chose Lizzard and the computer chose Paper!")
            print("You win! Henry the Lizzard mistakes the paper for a fly and eats it! Try again?")
            win += 1    
        elif computer_input == "Scissors":
            print("You chose Lizzard and the computer chose Scissors!")
            print("You lose! You get Henry the Lizzard to attack Scissors...which easily chop off his head. Try again?")
            lose += 1
        elif computer_input == "Lizzard":
            print("You chose Lizzard and the computer chose Lizzard!")
            print("You tie! Apparently there are TWO Henry the Lizzards.  They just stare at each other. Try again?")
            tie += 1
        elif computer_input == "Spock":
            print("You chose Lizzard and the computer chose Spock!")
            print("You win! The poison secreted by Henry the Lizzard is deadly to Spock. Poor Spock. Try again?")
            win += 1
    elif user_choice == "e":
        if computer_input == "Rock":
            print("You chose Spock and the computer chose Rock!")
            print("You win! Spock vaporizes Rock with his phaser! Try again?")
            win += 1
        elif computer_input == "Paper":
            print("You chose Spock and the computer chose Paper!")
            print("You lose! Sadly, the logic of the paper defeats Spock easily. Try again?")
            lose += 1    
        elif computer_input == "Scissors":
            print("You chose Spock and the computer chose Scissors!")
            print("You win! Spock takes the Scissors and smashes them on the ground like a child! Try again?")
            win += 1
        elif computer_input == "Lizzard":
            print("You chose Spock and the computer chose Lizzard!")
            print("You lose! Spock dies from the poisoned barbs on Henry the Lizzard. Try again?")
            lose += 1
        elif computer_input == "Spock":
            print("You chose Spock and the computer chose Spock!")
            print("You tie! Due to a transporter accident, there are TWO Spocks! They just bore each other to death. Try again?")
            tie += 1
    elif user_choice == "f":
        print("Thanks for playing with The Lonely Dash bot!  Let's see how you did: You won " + str(win) + ". You lost " + str(lose) + ". You tied " + str(tie) + "!")
        total = win + lose + tie
        win_percent = round(100*(win/total))
        print("You won " + str(win_percent) + " percent of your games! See you again next time!")
        quit()
    else:
        print("You didn't make a valid choice! Please choose A, B, C, D, E, or F.  Try again.\n")



#Create a menu of choices from which the user may choose including rock, paper, scissors, lizzard, spock, and quit.  Include a user input variable!
#Create an array of choices from which the computer may choose - include a random variable input for the computer!
#Create a series of if statements which provide the outcome of the game.
#Create variables to track win, lose, or tie.
#When the user quits, calculate their win percentage based on the above win/lose/tie variables.