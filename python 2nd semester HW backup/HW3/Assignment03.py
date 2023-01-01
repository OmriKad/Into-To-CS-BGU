# Question 1
from msilib.schema import Binary


def question1(p):
    """
    This function checks if a given number is a germain prime number using recursion.
    :param p: (int) Given number.
    :return: (bool) True if is a germain prime, False if not.
    """
    # Bounce numbers smaller than 1
    if p <= 1:
        return False
    # The only even Prime (and also germain)
    if p == 2:
        return True
    if question1_helper(p, 2):
        # The definition for germain prime
        return question1_helper((2 * p) + 1, 2)
    else:
        return False


def question1_helper(p, denominator):
    # Helper for q1, checks if a given is prime using recursion.
    if p % denominator == 0:
        return False
    if denominator == p - 1:
        return True
    else:
        return question1_helper(p, denominator + 1)


# Question 2_a
def question2_a(num_str):
    """
    This functions checks if a given binary string has valid structure using recursion.
    :param num_str: (str) Binary num.
    :return: (Bool) True for valid number, False for not valid.
    """
    # Bounce case of empty string
    if num_str == "":
        return False
    # Enters the help function. The string has a space character attached to it at the end to serve has a mark for
    # the last index
    return question2_a_helper(num_str + " ", 0)


def question2_a_helper(num_str, indx):
    # Base case, all the characters are valid and now the length is being checked
    if num_str[indx] == " ":
        if indx % 8 == 0:
            return True
        else:
            return False
    # The current index character is valid, ready to step into next index
    elif num_str[indx] == "0" or num_str[indx] == "1":
        return question2_a_helper(num_str, indx + 1)
    # Case of spotted invalid character
    else:
        return False


# Question 2_b
def question2_b(num_str):
    """
    This function converts a binary number to decimal using the 2's compliment rule.
    :param num_str: (str) Binary num.
    :return: (int) Decimal num, (None) for invalid input binary.
    """
    # First checks if the given binary is valid using the previous function
    if question2_a(num_str):
        # The MSB is 1, therefore it needs to go through the complement section first
        if num_str[0] == "1":
            # Number is converted to the complement form using the special function
            complemented_num = complement_rec(num_str + " ", 0)
            # Number is converted to the int form using the special function
            complemented_num_int = binary_to_int_rec(" " + complemented_num[:-1], -1, 0)
            # Added offset and multiplied by -1 to give the True negative form
            complemented_num_int += 1
            return complemented_num_int * -1
        # The MSB is 1, therefore it can go through normal conversion
        else:
            return binary_to_int_rec(" " + num_str, -1, 0)
    # Given number is invalid binary
    else:
        return None


def complement_rec(num_str, indx):
    # Using recursion, each time the index increments by 1 and the value flips. The base case is when
    # The " " is met
    if num_str[indx] == " ":
        return num_str
    if num_str[indx] == "0":
        return complement_rec(num_str[:indx] + "1" + num_str[indx + 1:], indx + 1)
    if num_str[indx] == "1":
        return complement_rec(num_str[:indx] + "0" + num_str[indx + 1:], indx + 1)


def binary_to_int_rec(complemented_num, indx, res):
    # Using recursion, each time the index increments by 1 and the value is calculated. The base case is when
    # The " " is met
    if complemented_num[indx] == " ":
        return res
    if complemented_num[indx] == "1":
        res += 2 ** ((indx + 1) * -1)
    return binary_to_int_rec(complemented_num, indx - 1, res)


# Question 3
def question3(lst, n):
    """
    This function returns the number of subsets that their product is n.
    :param lst: (list) List of numbers.
    :param n: (int) Target number.
    :return: (int) The number of different subsets.
    """
    # Base case when subtraction res is 1
    if n == 1:
        return 1
    # Empty List
    elif len(lst) == 0:
        return 0
    # The subtraction results a fraction
    elif 1 < n < 0:
        return 0
    else:
        return question3(lst[:-1], n / lst[-1]) + question3(lst[:-1], n)


# Question 4
def question4(game_list):
    """
    This function is a mini-game where each player takes one stone from the end or the beginning of the game list.
    Every time the score updates and all game options are reviewed to select the total winner with most options to win.
    :param game_list: (list) A list representing the board with numbers as the score for selecting the stone.
    :return: (bool) True if player A has more chances for winning, False if not.
    """
    # Initial scores
    score_a = 0
    score_b = 0
    # The total amount of wins for player A is returned. The total permutations is n*log(n). If player A has more
    # wins than half of it, it means he is the winner. (The question here is represented different in order not to
    # import math.
    wins = play_A(game_list[1:], score_a + game_list[0], score_b) + play_A(game_list[:-1], score_a + game_list[-1], score_b)
    if 2 ** wins > len(game_list) ** (len(game_list) / 2):
        return True
    else:
        return False


def play_A(game_list, score_a, score_b):
    # Base case is when the game has only 1 piece left, so in the next turn the opponent has to take it. The scores are
    # measured, if player A has more points 1 is return. If he doesn't 0 is return.
    if len(game_list) == 1:
        score_b += game_list[0]
        if score_a >= score_b:
            return 1
        else:
            return 0
    else:
        # The options for next turn, Player B can either take a piece from the left or right.
        return play_B(game_list[1:], score_a, score_b + game_list[0]) + play_B(game_list[:-1], score_a, score_b + game_list[-1])


def play_B(game_list, score_a, score_b):
    # Same as Play_A logic
    if len(game_list) == 1:
        score_a += game_list[0]
        if score_a >= score_b:
            return 1
        else:
            return 0
    else:
        return play_A(game_list[1:], score_a + game_list[0], score_b) + play_A(game_list[:-1], score_a + game_list[-1], score_b)


# Question 5
def question5(terrain):
    """
    This function uses recursion to return the largest river in a given matrix where 1 is a river and 0 is land.
    The functions scan column by column and row by row for a leading 1. When met, the search function is initiated to
    search the surroundings for another 1. Every 1 encountered is being added to a list. When all matrix is scanned,
    the results are being added recursively to final big list, where the max one is returned.
    :param terrain: (list(list(int))) A multi-dimensional list that forms a binary matrix.
    :return: (int) The area of the largest river.
    """
    row = 0
    col = 0
    res = numRivers(terrain, row, col)
    return max(res)


def numRivers(terrain, row, col):
    # If the matrix is empty
    if not terrain:
        return 0
    # answers bank
    ans = [0]
    # 1 was found, can search the surroundings
    if terrain[row][col] == 1:
        search(terrain, row, col, ans)
    # All surroundings scanned, can hop to next right column
    col += 1
    # Bumped to the end column, reset to the first column and hop to next down row
    if col == len(terrain[0]):
        col = 0
        row += 1
    # Bumped to the end row, all matrix is scanned, return results.
    if row == len(terrain):
        return ans

    return ans + numRivers(terrain, row, col)


def search(grid, i, j, ans):
    # All options of land surrounding tile, can return
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
        return
    # Switches 1 to -1 in order to mark visited river tile
    grid[i][j] = -1
    # 1 is added to ans list
    ans[0] += 1
    # search upper tile
    search(grid, i+1, j, ans)
    # search lower tile
    search(grid, i-1, j, ans)
    # search right tile
    search(grid, i, j+1, ans)
    # search left tile
    search(grid, i, j-1, ans)


# main
if __name__ == '__main__':

    # Tests for Q1
    input_list = [5, 11, 23, 6, 17]
    expected_output = [True, True, True, False, False]
    for i in range(0, len(input_list)):
        your_output = question1(input_list[i])
        print("Function: question1\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                        expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # Tests for Q2_a
    input_list = ['11110000', '10121111', '1000', '0', '00110101']
    expected_output = [True, False, False, False, True]
    for i in range(0, len(input_list)):
        your_output = question2_a(input_list[i])
        print("Function: question2\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                        expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # Tests for Q2_b
    input_list = ['10001100', '11111111', '1000', '0', '00110101', '1111111110000000']
    expected_output = [-116, -1, None, None, 53, -128]
    for i in range(0, len(input_list)):
        your_output = question2_b(input_list[i])
        print("Function: question2b\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
                                                                                         expected_output[i]),
              your_output, "\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # Tests for Q3
    input_list = [([2,4,6,12,7,3,1], 12), ([2,3,6,1], 6), ([5,4,2,10,8,3], 24)]
    expected_output = [6, 4, 2]
    for i in range(0, len(input_list)):
        your_output = question3(*input_list[i])
        print("Function: question3\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
        expected_output[i]), your_output,"\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # Tests for Q4
    input_list = [[1,5,2], [1,14,20,35]]
    expected_output = [False, True]
    for i in range(0, len(input_list)):
        your_output = question4(input_list[i])
        print("Function: question4\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
        expected_output[i]), your_output,"\nisEqual: {}\n-----".format(your_output == expected_output[i]))

    # Tests for Q5
    input_list = [ [[0,1,1,1],[0,1,0,0],[1,1,1,0],[0,0,1,1]], [[1,0,0,0],[1,1,0,0],[0,0,0,0],[1,1,0,1]],
                   [[0,0,0],[1,1,1],[0,1,0],[1,0,1]] ]
    expected_output = [9, 3, 4]
    for i in range(0, len(input_list)):
        your_output = question5(input_list[i])
        print("Function: question5\nInput: {}\nExpectedOutput: {}\nYourOutput: ".format(input_list[i],
        expected_output[i]), your_output,"\nisEqual: {}\n-----".format(your_output == expected_output[i]))



