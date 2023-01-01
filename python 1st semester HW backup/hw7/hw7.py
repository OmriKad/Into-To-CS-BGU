########################################################
# Intro to CS - Assignment 7
# replace the exception raising in each function with your solution
################### GOOD LUCK ##########################
########################################################

########################################################
# Q1:
########################################################
# 1
import math
from functools import reduce


def get_months_under_limit(monthly_shopping_costs, monthly_limit):
    """
    This function returns the months which Alice and bob stayed within the monthly limit, using built-in HOF.
    :param monthly_shopping_costs: [Dict[str, List[int]]: A dictionary with months as keys and list
    of expenses as values.
    :param monthly_limit: [int]: An integer representing the monthly limit for expenses.
    :return: [List]: The months that comply the monthly limit.
    """
    return list(filter(lambda x: not '1' in x, map(lambda x, y: x if sum(y) < monthly_limit else '1', monthly_shopping_costs.keys(), monthly_shopping_costs.values())))


# 2
def sum_under_limit_number_of_purchases(monthly_shopping_costs, max_number_of_purchases):
    """
    This function returns the sum of purchases that are under the max amount per month, using built-in HOF.
    :param monthly_shopping_costs: [Dict[str, List[int]]: A dictionary with months as keys and list
    of expenses as values.
    :param max_number_of_purchases: An integer representing the max amount of purchases recommended per month.
    :return: [int/float]: If the amount per month is equal or less the max_number_of_purchases, The sum is returned.
    Else, the total sum in equal to  -infinity.
    """
    return reduce(lambda x, y: x+y , map(lambda x: int(sum(x)) if len(x) <= max_number_of_purchases else float(-math.inf), monthly_shopping_costs.values()))

# 3
def verify_monthly_monotonic_growing_expenses(monthly_shopping_costs):
    """
    The function check weather all purchases during all months are a monotonic raising series, using built-in HOF.
    :param monthly_shopping_costs: [Dict[str, List[int]]: A dictionary with months as keys and list
    of expenses as values.
    :return: [bool]: True if is a monotonic raising series, False if it's not.
    """
    return reduce(lambda x,y: x and y ,map(lambda x,y: True if x <= y else False, list(reduce(lambda x,y: x+y, list(monthly_shopping_costs.values())))[::2], list(reduce(lambda x,y: x+y, list(monthly_shopping_costs.values())))[1::2]))

# 4
def divide_monthly_bills(apartment_bills, bob_weekly_income):
    """
    The function return a partition plan of the bills based on Bob's weekly income, using built-in HOF.
    :param apartment_bills: [Dict[str, List[int]]: A dictionary with services as keys and list
    of expenses as values.
    :param bob_weekly_income: [int]: An int representing Bob's weekly income.
    :return: [str]: A formatted partition plan for all expenses, Bob's paying for services that they're sum in within
    he's weekly income, Alice is paying for everything else.
    """
    return ', '.join(list(map(lambda x,y: f'Bob: {x}' if y <= bob_weekly_income else f'Alice: {x}' ,apartment_bills.keys() ,map(lambda x: sum(x), list(apartment_bills.values())))))

########################################################
# Q2:
########################################################
# 1
def add(a,b):
    return a+b

def multiply(a,b):
    return a*b

def operations_parser_function(code):
    """
    This function classifies a given 2 bits code weather if it's addition of multiplication. If the sum of bit's is
    equal to 1, an addition is returned. Else, a multiplication is returned.
    :param code:
    :return:
    """
    if code == '01' or code == '10':
        return add
    else:
        return multiply

# 2
def value_parser(code):
    if code[0] == '0':
        ans = 0
        for char in code[1:]:
            ans += int(char)
        return float(ans)
    else:
        raise ValueError

def operations_parser1(code):
    if code[0] == '1':
        if code[1:] == '01' or code[1:] == '10':
            return add
        else:
            return multiply
    else:
        raise TypeError

def binary_code_compiler(lines_of_code_triplets, value_parser, operations_parser):
    """
    This function is an abstract generic interpreter. The function receives lines of code as triplets, two number and
    an operation in the middle, and then sums up all results.
    :param lines_of_code_triplets: [list[tuple[str,str,str]]]: Each tuple in the list represent a line of code.
    Numbers need to be on sides, and have a 0 in the 0 index. An operation must be in the middle with a 1 in the 0 index
    If these are not complied, a matching error is being raised and the current index is returned.
    :param value_parser:
    :param operations_parser:
    :return:
    """
    indx = 0
    final = 0
    for line in lines_of_code_triplets:
        try:
            num_left = value_parser(line[0])
            num_right = value_parser(line[2])
        except ValueError:
            return str(indx)
        try:
            operation = operations_parser1(str(line[1]))
        except TypeError:
            return str(indx)
        final += operation(num_left, num_right)
        indx += 1
    return final


lines_of_triplets = [('101', '101', '001'),
                  ('001', '101', '011')]
ans = binary_code_compiler(lines_of_triplets, value_parser, operations_parser1)
print(ans)
print(type(ans))