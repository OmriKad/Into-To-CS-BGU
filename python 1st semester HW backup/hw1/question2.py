# ************************ HOMEWORK 1 QUESTION 2 **************************
def question2(player1, player2):
    print('************ TO DO: Question 2 ************')  # TODO - DELETE BEFORE SUBMISSION
    ### WRITE CODE HERE

    # The conditions for player 1 to win.
    if player1 == str("rock") and player2 == str("scissors") or player1 == str("paper") and player2 == str("rock") \
            or player1 == str("scissors") and player2 == str("paper"):
        print("Player 1 won!")
    # The condition for a tie.
    elif player1 == player2:
        print("It is a tie!")
    # The other options which player 2 is the winner.
    else:
        print("Player 2 won!")

