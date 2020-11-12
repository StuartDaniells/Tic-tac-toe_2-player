# 2 Player Tic Tac Toe game with board:

lines = "     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     "
turns = 0


def lines_grid():
    global lines, turns
    
    lines = "     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     "
    turns = 0


def grid():
    print(lines)
grid()


def user_selection():
    
    position = ''
    
    while (position.isdigit() == False) or (int(position) not in range(1,10)):
        position = input("\nChoose a position on the tic-tac grid: (from 1-9):  -> ")
        
        if position.isdigit() == False:
            print("\n ----> Please choose a number, not a character...")
            
        elif int(position) not in range(1,10):
            print("\n ----> Choose a number ONLY from 1 to 9")
            
    return position


def players():
    
    Pchoice = True
    
    while Pchoice:
        player_choice1 = input("\nChoose Player 1, either 'X' or 'O'  -> ")

        if player_choice1.upper() == 'X':
            player_choice2 = 'O'
            Pchoice = False
            
        elif player_choice1.upper() == 'O':
            player_choice2 = 'X'
            Pchoice = False
            
        else:
            print("\n--> [Please select either X or O as player 1]")

    return [player_choice1.upper(), player_choice2];
    

def filling_grid(): 
    
    global lines, turns
    
    player1 = player_choice[0]
    player2 = player_choice[1]
    
# Player 1 turn:
    if turns%2 == 0:
        if player1 == 'X':
            if lines.find(position) != -1:
                lines = lines.replace(position, 'X')
                turns += 1
                clear_output()
                print(f"[Player 1 = {player1}, Player 2 = {player2}]\n")
                print("\n -> Player 2 turn now")
                grid()                
            else:
                print("\n -> [Position already selected, please select another]") 
                
        elif player1 == 'O':
            if lines.find(position) != -1:
                lines = lines.replace(position, 'O')
                turns += 1
                clear_output()
                print(f"[Player 1 = {player1}, Player 2 = {player2}]\n")
                print("\n -> Player 2 turn now")
                grid()
            else:
                print("\n -> [Position already selected, please select another]")
                
# Player 2 turn:
    elif turns%2 != 0:
        if player2 == 'X':
            if lines.find(position) != -1:
                lines = lines.replace(position, 'X')
                turns += 1
                clear_output()
                print(f"[Player 1 = {player1}, Player 2 = {player2}]\n")
                print("\n -> Player 1 turn now")
                grid()
            else:
                print("\n -> [Position already selected, please select another]") 

        elif player2 == 'O':
            if lines.find(position) != -1:
                lines = lines.replace(position, 'O')
                turns += 1
                clear_output()
                print(f"[Player 1 = {player1}, Player 2 = {player2}]\n")
                print("\n -> Player 1 turn now")
                grid()
            else:
                print("\n -> [Position already selected, please select another]")


def winner():
    
    player1 = player_choice[0]
    player2 = player_choice[1]
    
# 20,26,32,74,80,86,128,134,140
# 1 , 2, 3, 4, 5, 6, 7,  8,  9

    cell_1 = lines[20]
    cell2 = lines[26]
    cell3 = lines[32]
    cell4 = lines[74]
    cell5 = lines[80]
    cell6 = lines[86]
    cell7 = lines[128]
    cell8 = lines[134]
    cell9 = lines[140]
    
    
#For rows
    if (cell_1 == cell2 == cell3 == player1) or (cell4 == cell5 == cell6 == player1) or (cell7 == cell8 == cell9 == player1):
        clear_output()
        grid()
        print(f"--------------------------------> Winner is Player1 - '{player1}'\n")
        return continuing()
        
    elif (cell_1 == cell2 == cell3 == player2) or (cell4 == cell5 == cell6 == player2) or (cell7 == cell8 == cell9 == player2):
        clear_output()
        grid()
        print(f"--------------------------------> Winner is Player2 - '{player2}'\n")
        return continuing()
        
        
#For columns
    elif (cell_1 == cell4 == cell7 == player1) or (cell2 == cell5 == cell8 == player1) or (cell3 == cell6 == cell9 == player1):
        clear_output()
        grid()
        print(f"--------------------------------> Winner is Player1 - '{player1}'\n")
        return continuing()
        
    elif (cell_1 == cell4 == cell7 == player2) or (cell2 == cell5 == cell8 == player2) or (cell3 == cell6 == cell9 == player2):
        clear_output()
        grid()
        print(f"--------------------------------> Winner is Player2 - '{player2}'\n")
        return continuing()
          
            
#For diagonals
    elif (cell_1 == cell5 == cell9 == player1) or (cell3 == cell5 == cell7 == player1):
        clear_output()
        grid()
        print(f"--------------------------------> Winner is Player1 - '{player1}'\n")
        return continuing()
        
    elif (cell_1 == cell5 == cell9 == player2) or (cell3 == cell5 == cell7 == player2):
        clear_output()
        grid()
        print(f"--------------------------------> Winner is Player2 - '{player2}'\n")
        return continuing()
    
    else:
        return 'No_Winner'



def continuing():
    
    decision = True 
    
    while decision:
        choice = input("\nWould you like to continue playing? \n\n\n ---> Input either 'Y' - (for yes) or 'N' - (for no)\n\n->")
        choice = choice.upper()
        
        if choice == 'Y':
            clear_output()
            return True
            
        elif choice == 'N':
            print("\n--------------------------------Game Over!--------------------------------")
            return False
            
        else:
            clear_output()
            print("\n[Enter either Y or N to proceed]")



from IPython.display import clear_output
clear_output()

lines = "     |     |     \n  1  |  2  |  3  \n_____|_____|_____\n     |     |     \n  4  |  5  |  6  \n_____|_____|_____\n     |     |     \n  7  |  8  |  9  \n     |     |     "
turns = 0
Y_or_N_choice = True

while Y_or_N_choice:
    
    lines_grid()
    
    grid()
    
    player_choice = players()
    
    next_turn = True
    
    while (turns < 9) and next_turn:
        position = user_selection()
        
        filling_grid()
        
        checking = winner()
        
            
        if checking == True:
            next_turn = False
            
        elif checking == False:
            next_turn = False
            Y_or_N_choice = False
    
    
    if turns == 9 and checking == 'No_Winner':
        print("\n----------------------> It's a draw!")
        Y_or_N_choice = continuing()
    
    