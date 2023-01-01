# 1.1
def subset_sum_count(ls, sm):
    """
    This function sums up all the possible solutions for a subset to reach a given sum using recursion.
    The recursion works as follows: The base cases split to either if sm reached 0 (and returns 1) and either sm is
    negative or ls reached 0 (and returns 0). Otherwise, we call the function 2 calls: 1. ls without last index and
    sm - that value, 2. same but sm stays the same. Both calls are summed. This will create a recursion tree that
    every 2 nodes are being summed, the total sum is returned.
    :param ls: (list) A list of a given subset
    :param sm: (int) The sum goal
    :return: (int) The number of possible solutions.
    """
    if sm == 0:
        return 1
    elif len(ls) == 0:
        return 0
    elif sm < 0:
        return 0
    else:
        return subset_sum_count(ls[:-1], sm - ls[-1]) + subset_sum_count(ls[:-1], sm)


# 1.2
def subset_sums_helper(sm, ls, final, tmp):
    if sm == 0:
        final.append(tmp[:])
        return
    if sm < 0 or len(ls) == 0:
        return
    subset_sums_helper(sm - ls[0], ls[1:], final, tmp + [ls[0]])
    subset_sums_helper(sm, ls[1:], final, tmp)


def subset_sums(ls, sm):
    """
    This function returns the possible solutions from a given subset to reach a given sum.
    :param ls: (list) A list containing a subset.
    :param sm: (int) A number representing a sum.
    :return: (list) A list with nested lists for each solution.
    """
    final = []
    subset_sums_helper(sm, ls, final, [])
    return final


# 1.3

def subset_sum_memo_help(ls, sm, mem):
    if (str(ls), sm) in mem:
        return mem[(str(ls), sm)]

    else:
        if sm == 0:
            return True
        elif len(ls) == 0:
            return False
        elif sm < 0:
            return False
        else:
            option1 = subset_sum_memo_help(ls[:-1], sm - ls[-1], mem)
            option2 = subset_sum_memo_help(ls[:-1], sm, mem)
            mem[(str(ls), sm)] = option1 or option2
            return option1 or option2


def subset_sum_memo(ls, sm):
    """
    This function returns if a given subset has a solution for a given sum. The function is using memoization and
    recursion with a helper function ("subset_sum_memo_help").
    :param ls: (list) A list containing a subset.
    :param sm: (int) A number representing a sum.
    :return: (bool) True for a solution was found, False for no solution was found.
    """
    mem = {}
    return subset_sum_memo_help(ls, sm, mem)


# 1.4
def susu_repeats_help(sm, ls, final, aux):
    if sm == 0:
        final.append(aux[:])
    if sm < 0:
        return 0
    for combs in ls:
        susu_repeats_help(sm - combs, ls, final, aux + [combs])


def subset_sum_with_repeats(ls, sm):
    """
    This function gives all possible susu problem combinations usuing recursion. The algorithm is similar to the
    previous questions only this time, The helper function ("susu_repeats_help") is using a single iterating loop on ls
    to call the recursion. If a solution was found the base case sm == 0 appends the aux parameter into the final list
    which is being returned with all different combinations.
    :param ls: (list) List of a given subset
    :param sm: (int) The sum goal
    :return: (list) A list containing nested lists of all possible combinations repeating.
    """
    final = []
    susu_repeats_help(sm, ls, final, [])
    return final


# 2.1
def abc_words_help(num, final, tmp):
    if num == 0:
        final.append(tmp[:])
    if num < 0:
        return
    abc_words_help(num - 1, final, tmp + 'a')
    abc_words_help(num - 1, final, tmp + 'b')
    abc_words_help(num - 1, final, tmp + 'c')
    return final


def abc_words(num):
    """
    This function outputs all variations of 'a' 'b' 'c' sorted lexicographically with a given length for each variation.
    :param num: (int) A number for the length of each variation.
    :return: (lst) A list of all variations.
    """
    tmp = ''
    final = []
    return abc_words_help(num, final, tmp)


# 2.2
def char_to_char_help(ord_lst, num, aux, final):
    if ord_lst[0] == ord_lst[1]:
        return [num * ord_lst[0]]
    else:
        if num == 0:
            final.append(aux)
            return
        if num < 0:
            return
        for combs in ord_lst:
            char_to_char_help(ord_lst, num - 1, aux + combs, final)
        return final


def char_lst(ch1, ch2, lst):
    if ch2 == ch1:
        return
    else:
        char_lst(ch1, ch2 - 1, lst)
    lst += [chr(ch2)]
    return lst


def char_to_char_words(ch1, ch2, num):
    """
    This function gives a list with all options of ch1 ('A' - 'Z') to ch2 (ch1 - 'Z'). The options are sorted
     lexicographic. We use 2 helper functions: 1. ("char_lst") is returns a list containing ch1 - ch2.
     2. ("char_to_char_help") is responsible for the final list output.
    :param ch1: (str) A letter from 'A' to 'Z'
    :param ch2: (str) A letter from 'ch1' to 'Z'
    :param num: (int) The max length for each variation.
    :return: (list) A list with all variations.
    """
    lst = [ch1]
    if ch1 == ch2:
        ord_lst = [ch1, ch2]
    else:
        ord_lst = char_lst(ord(ch1), ord(ch2), lst)
    aux = ''
    final = []
    return char_to_char_help(ord_lst, num, aux, final)


# 3
def maze_help(maze, max_columns, max_rows, i, j, res, truthflag):
    if not truthflag[0]:
        if i == max_rows - 1 and j == max_columns - 1:
            truthflag[0] = True
            return res

        if j + 1 < max_columns and truthflag[0] == False:
            # right
            if maze[i][j + 1] > maze[i][j]:
                res.append([i, j + 1])
                maze_help(maze, max_columns, max_rows, i, j + 1, res, truthflag)
        if i + 1 < max_rows and truthflag[0] == False:
            # down
            if maze[i + 1][j] > maze[i][j]:
                res.append([i + 1, j])
                maze_help(maze, max_columns, max_rows, i + 1, j, res, truthflag)
        if j - 1 >= 0 and truthflag[0] == False:
            # left
            if maze[i][j - 1] > maze[i][j]:
                res.append([i, j - 1])
                maze_help(maze, max_columns, max_rows, i, j - 1, res, truthflag)
        if i - 1 >= 0 and truthflag[0] == False:
            # up
            if maze[i - 1][j] > maze[i][j]:
                res.append([i - 1, j])
                maze_help(maze, max_columns, max_rows, i - 1, j, res, truthflag)
    if not truthflag[0]:
        res.pop()
    return res


def solve_maze_monotonic(maze):
    """
    This function receives a maze and recursively finds a path to the solution. In the wrapper function - we eliminate
    an option for an empty input. Then initializing the parameters for max rows/columns to know our boundaries. i & j
    parameters are being set to zero (i for row and j for column), and the work function ("maze_help") is being called.
    The base case for this function is when i & j are at the max -1 point (the maze gate). At this point, a parameter
    named truthflag is being set to True. Until then, we try recursively to go at each direction as long as truthflag
    is False (no solution was found yet), and track out path using a list. If we get stuck, we pop out the -1 index of
    the solution and return to find another way.
    :param maze: (list) A list with nested lists that make up the maze.
    :return: (list) A list of the found solution for the maze. The list of nested lists contain the coordinates.
    """
    if not maze:
        return []
    if len(maze) > 1:
        max_rows = len(maze)
    if len(maze) == 1:
        max_rows = 1
    if len(maze[0]) > 1:
        max_columns = len(maze[0])
    if len(maze[0]) == 1:
        max_columns = 1
    # column
    j = 0
    # row
    i = 0
    return maze_help(maze, max_columns, max_rows, i, j, [[0, 0]], [False])
