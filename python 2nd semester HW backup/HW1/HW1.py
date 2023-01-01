# **** QUESTION 1 ****
def question1(x1, y1, x2, y2):
    # Finds the distance using the formula.
    num = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return "{:.2f}".format(num)


# **** QUESTION 2 ****
def question2(PIN, GUESS):
    sum_pin = 0
    for i in PIN:
        sum_pin += i
    sum_guess = 0
    for j in GUESS:
        sum_guess += j
    # The sums are the same
    if sum_pin == sum_guess:
        return "JACKPOT"
    # The absolute value distance is 1
    elif ((sum_guess - sum_pin) ** 2) ** 0.5 == 1:
        return "ALMOST"
    else:
        # The sums are way far from each other
        return "JACK WHO"


# **** QUESTION 3 ****
def question3(sentence):
    # Lowering Capital cases
    sentence = sentence.lower()
    # Responsible for non-alphanumerical to be removed
    if not sentence.isalpha():
        for i in sentence:
            if not (i.isalpha() or i.isnumeric()):
                sentence = sentence.replace(i, "")
    # Comparing if palindrome
    if sentence == sentence[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"


# **** QUESTION 4 ****
def question4(pizzas):
    len_kinds = len(set(pizzas))
    len_num = len(pizzas) // 2
    return min(len_num, len_kinds)


# **** QUESTION 5 ****
def question5(p):
    # Default sign for non prime num
    deg = -1
    # Flag used for exiting the while loop
    flag = 0
    if p <= 2:
        return deg
    # This is the working loop, with each successful iteration updates the p value by the germain definition and the
    # degree is raised by 1. If a non prime was found, the loop terminates.
    while flag == 0:
        loop_range = int(p ** 0.5)
        count = 2
        while count <= loop_range:
            if p % count == 0:
                flag = 1
                return deg
            else:
                count += 1
        deg += 1
        p = 2 * p + 1


def func_help(lst):
    # mid num of current list
    mid = len(lst) // 2
    # situation where the original list is either ascending or descending
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[0]
        else:
            return lst[1]
    if lst[mid] > lst[mid + 1] and lst[mid] > lst[mid - 1]:   # solution
        return lst[mid]
    if lst[mid] < lst[mid - 1]:
        return func_help(lst[:mid + 1])
    if lst[mid] < lst[mid + 1]:
        return func_help(lst[mid:])

def func(lst):
    highnum = func_help(lst)
    return lst.index(highnum)



lst3 = [1, 2, 3, 4, 5, 6, 7, 8, 1]
print(func(lst3))




