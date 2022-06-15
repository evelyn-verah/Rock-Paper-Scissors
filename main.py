import random


def play():

    computer_selection = random.choice(['p', 'r', 's'])
    # print(computer_selection)
    user_input = input(" 1. P for Paper \n 2. S for Scissors \n 3. R for Rock \n Please enter your choice: ")
        # ignore case
    user_input = user_input.lower()

    # if user_input != "p" or "r" or "s":
    #     print("Invalid input")
    #     # break

    while user_input == "p" or user_input ==  "r" or user_input == "s":

        # user_input = input(" 1. P for Paper \n 2. S for Scissors \n 3. R for Rock \n Please enter your choice: ")
        # # ignore case
        # user_input.lower()
        
        # if user_input != "p" or "r" or "s":
        #     print("Invalid input")
        #     break

        # else: 
        #    user_input = input(" 1. P for Paper \n 2. S for Scissors \n 3. R for Rock \n Please enter your choice: ")
            # ignore case
            #   user_input = user_input.lower()
            # continue

        # computer_selection = random.choice(['p', 'r', 's'])

        if user_input == computer_selection:
            print("Player({})! : Computer({})!It's a tie ".format(user_input,computer_selection))
            user_input = input(" 1. P for Paper \n 2. S for Scissors \n 3. R for Rock \n Please enter your choice: ")
            # ignore case
            user_input = user_input.lower()
        elif is_win(user_input, computer_selection) == True:
            print("Player({})! : Computer({})! you won ".format(user_input, computer_selection))
            print("Player WON")
            break 
        else: 
           print("Player({})! : Computer({})!" .format(user_input,computer_selection))
           print("CPU WON")
           break
           

    # user_input = input(" 1. P for Paper \n 2. S for Scissors \n 3. R for Rock \n Please enter your choice: ")

        


def is_win(player,opponent):
    # retun true if the player has won against the opponent
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent =="r"):
         return True
    return False

if __name__ == '__main__':
    play()
