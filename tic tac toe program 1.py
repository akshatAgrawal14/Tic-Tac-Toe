board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

'''
def draw_board(board):
    print(board[7] + " |" + board[8] + " |" + board[9])
    print("--+--+--")
    print(board[4] + " |" + board[5] + " |" + board[6])
    print("--+--+--")
    print(board[1] + " |" + board[2] + " |" + board[3])
'''

def draw_board(board):
    print(board[1] + " |" + board[2] + " |" + board[3])
    print("--+--+--")
    print(board[4] + " |" + board[5] + " |" + board[6])
    print("--+--+--")
    print(board[7] + " |" + board[8] + " |" + board[9])

    
player1 = raw_input("Enter 1st Player name: ")
player2 = raw_input("Enter 2nd Player name: ")

print(player1 + ": X |" + player2 + ": O")


def game():
    turn = "X"
    count = 0
    player_turn = player1
    print("For your reference")
    print("1 |2 |3")
    print("--+--+--")
    print("4 |5 |6")
    print("--+--+--")
    print("7 |8 |9\n\n")

    for i in range(10):
        print("STATUS:")
        draw_board(board)
        print("\n")
        print("It's your turn, " + player_turn + ". Where would you put the " + turn +"?")
        move = eval(raw_input())

        if board[move] == " ":
            board[move] = turn
            count += 1
        else:
            print("That block is already filled. Again, where would you put the " + turn +"?")
            continue

        if count >= 5:
            if board[7] == board[8] == board[9] != " ":  # across the top
                declare_winner(turn)
                break
            elif board[4] == board[5] == board[6] != " ":  # across the middle
                declare_winner(turn)
                break
            elif board[1] == board[2] == board[3] != " ":  # across the bottom
                declare_winner(turn)
                break
            elif board[1] == board[4] == board[7] != " ":  # down the left side
                declare_winner(turn)
                break
            elif board[2] == board[5] == board[8] != " ":  # down the middle
                declare_winner(turn)
                break
            elif board[3] == board[6] == board[9] != " ":  # down the right side
                declare_winner(turn)
                break
            elif board[7] == board[5] == board[3] != " ":  # diagonal
                declare_winner(turn)
                break
            elif board[1] == board[5] == board[9] != " ":  # diagonal
                declare_winner(turn)
                break

        # declare tie
        if count == 9:
            print("\nGAME OVER\n")
            print(" ** It's a Tie **")
            break
        
        # give the move to the other player
        if turn == "X":
            turn = "O"
            player_turn = player2
        else:
            turn = "X"
            player_turn = player1

    # ask to play again
    restart = raw_input("\nDo want to play again?(y/n): ")
    if restart == "y" or restart == "Y":
        for element in board:
            board[board.index(element)] = " "
        game()


def declare_winner(turn):
    draw_board(board)
    print("\nGAME OVER\n")
    if turn == "X":
        print(" ** " + player1 + " won **")
    else:
        print(" ** " + player2 + " won **")


if __name__ == "__main__":
    game()
