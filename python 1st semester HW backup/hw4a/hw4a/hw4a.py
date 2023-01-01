def is_palindrom_no_helper(st):
    # enter your answer here
    """
    The functions checks if a certain text is a palindrom using recursion. Each time the string is being sliced
    at both ends and being compared.
    :param st: a text
    :return: (bool) True if is palindrom, False if it isn't.
    """
    if st == '':
        return True
    if st[0] == st[-1]:
        is_palindrom_no_helper(st[1:-1])
        return True
    else:
        return False


def palindrom_helper(st, first_indx, last_indx):
    if st[first_indx] == st[last_indx] and first_indx < last_indx:
        return palindrom_helper(st, first_indx + 1, last_indx - 1)
    if last_indx < first_indx or first_indx == last_indx:
        return True
    else:
        return False


def is_palindrom_with_helper(st):
    # enter your answer here
    """
    The functions takes more memory friendly approach as it does the same as above only with a helper function
    ("palindrom_helper"). With every recursion the values of first and last indx are being shifted.
    :param st: A text
    :return: (bool) True if is palindrom, False if it isn't.
    """
    return palindrom_helper(st, 0, len(st) - 1)


def palindrom_helper_spaces(st, first_indx, last_indx):
    if st[first_indx] == st[last_indx] and first_indx < last_indx:
        return palindrom_helper_spaces(st, first_indx + 1, last_indx - 1)
    if last_indx < first_indx or first_indx == last_indx:
        return True
    if st[first_indx] == ' ':
        return palindrom_helper_spaces(st, first_indx + 1, last_indx)
    if st[last_indx] == ' ':
        return palindrom_helper_spaces(st, first_indx, last_indx - 1)
    else:
        return False


def is_palindrom_no_spaces(st):
    # enter your answer here
    """
    This function does the same only it can ignore if any spaces characters are in the string. The helper function -
    ("palindrom_helper_spaces") applies the recursion in 3 situations: if space is from the left - shift first index +1,
    if index from the right - shift last index -1 and if if first == last.
    :param st: A text
    :return:(bool) True if is palindrom, False if it isn't.
    """
    return palindrom_helper_spaces(st, 0, len(st) - 1)


def average_calc(grades, indx, weight, total_w):
    if indx > len(grades) - 1:
        return round(weight / total_w, 2)
    else:
        weight += grades[indx][0] * grades[indx][1]
        total_w += grades[indx][1]
        return average_calc(grades, indx + 1, weight, total_w)


def weighted_average(grades):
    # enter your answer here
    """
    This functions calculates the weighted average of grades using recursion. The helper function - ("average_calc")
    Base case is when the counting index is greater then the length of the list. until then each recursion the grade
    is multiplied with the weight and the the total weight is being counted. At the base case the everything is divided
    by the total weight and being rounded with 2 digits after the decimal point.
    :param grades: lst[(tup)] : List of tuples that contain grade at index 0 and weight at index 1.
    :return: int : The weighted_average.
    """
    return average_calc(grades, 0, 0, 0)


def is_prime_helper(num, nextnum):
    if num % nextnum == 0 and nextnum != num:
        return False
    if nextnum == num:
        return True
    else:
        return is_prime_helper(num, nextnum + 1)


def is_prime(num):
    # enter your answer here
    """
    This functions checks if a given number is a prime number using recursion. The helper function - ("is_prime_helper")
    Base case is when the number % nextnum is zero and their different (Found a divisor). Until then next num parameter
    adds each recursion (starts at 2 cause 1 is irrelevant). If none were found it means nextnum == num - The number is
    Prime.
    :param num: (int) A given number.
    :return: (bool) True if prime, False if it isn't.
    """
    return is_prime_helper(num, 2)


def is_perfect_helper(num, nextnum, divisors):
    if num % nextnum == 0:
        divisors.append(nextnum)
    if num == nextnum:
        return divisors
    return is_perfect_helper(num, nextnum + 1, divisors)


def is_perfect_counter(divisors, counter):
    if not divisors:
        return counter
    else:
        counter += divisors[0]
        divisors.pop(0)
    return is_perfect_counter(divisors, counter)


def is_perfect(num):
    # enter your answer here
    """
    The function checks if a given number is perfect using recursion. The works splits to 2 working recursion functions:
    1. is_perfect_helper 2.is_perfect_counter. At first, function 1 collects all the divisors of the number into a list,
    every recursion next_num parameter is being added 1 and breaks when it equals the original num. Then functions 2 job
    is to to count all indexes, using recursion. At the end, the sum product minus the original number is being compared
    and the result is being returned.
    :param num: (int) A given number
    :return: (bool) True if is perfect, False if it isn't.
    """
    divisors = is_perfect_helper(num, 2, [])
    sum_of_divisors = is_perfect_counter(divisors, 1)
    if sum_of_divisors - num == num:
        return True
    else:
        return False


def is_7_boom_seek7(num, indx):
    if indx > len(num) - 1:
        return False
    if '7' == num[indx]:
        return True
    else:
        return is_7_boom_seek7(num, indx + 1)


def is_7_boom(num):
    # enter your answer here
    """
    The function check if a given number is "boom" (divisible by 7 or contains 7) using recursion. The helper function-
    ("is_7_boom_seek7") Takes the num casted as a string and runs through it's characters to seek a 7. If found returns
    True and False if isn't. Then, if the value is True or the % 7 = 0, there's a boom. If not, it returns False.
    :param num: (int) A given number.
    :return: (bool) True if boom, False if isn't.
    """
    num_here = is_7_boom_seek7(str(num), 0)
    if num % 7 == 0 or num_here == True:
        return True
    if not num_here:
        return False
