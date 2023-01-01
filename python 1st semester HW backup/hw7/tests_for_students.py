from hw7 import *


def part1_possible_tests():
    print(f'##########\nPART 1\n##########')
    q_num = 1
    monthly_shopping = {'January': [199, 100, 200], 'February': [200, 100, 201], 'March': [150, 87, 35, 100]}
    assert get_months_under_limit(monthly_shopping, 500) == ['January', 'March'], f'question {q_num} is NOT okay'

    q_num = 2
    assert sum_under_limit_number_of_purchases(monthly_shopping, 5) == 1372, f'question {q_num} is NOT okay'

    q_num = 3
    monthly_shopping = {'January': [1, 2, 3], 'February': [4, 5, 5]}
    assert verify_monthly_monotonic_growing_expenses(monthly_shopping), f'question {q_num} is NOT okay'

    q_num = 4
    apartment_bills = {"Electricity": [2, 7, 1], "Water": [1, 1, 3], "Rent": [100, 2, 3]}
    bob_weekly_income = 5
    expected_ans = "Alice: Electricity, Bob: Water, Alice: Rent"
    assert divide_monthly_bills(apartment_bills, bob_weekly_income) == expected_ans, f'question {q_num} is NOT okay'


def part2_possible_tests():
    print(f'##########\nPART 2\n##########')
    q_num = 1
    code = '01'
    operation = operations_parser_function(code)
    assert operation(1, 1) == 2, f'question {q_num} is NOT okay'

    q_num = 2
    lines_of_code_triplets = [
        ('001', '101', '001'),
        ('001', '101', '111')
    ]
    assert binary_code_compiler(lines_of_code_triplets, lambda x: sum([int(i) for i in x]), operations_parser_function) == '1', f'question {q_num} is NOT okay'

if __name__ == '__main__':
    part1_possible_tests()
    part2_possible_tests()