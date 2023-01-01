from hw4a import *


def verify_question_1a():
    print('Q 1a:')
    print("'abba'", 'Pass test' if is_palindrom_no_helper('abba') == True else 'Fail test')
    print("'aba'", 'Pass test' if is_palindrom_no_helper('aba') == True else 'Fail test')
    print("'ima'", 'Pass test' if is_palindrom_no_helper('ima') == False else 'Fail test')
    print("'??!!@!!??'", 'Pass test' if is_palindrom_no_helper('??!!@!!??') == True else 'Fail test')
    print("' asdsa '", 'Pass test' if is_palindrom_no_helper(' asdsa ') == True else 'Fail test')
    print("'asdsa '", 'Pass test' if is_palindrom_no_helper('asdsa ') == False else 'Fail test')


def verify_question_1b():
    print('Q 1b:')
    print("' asdsa '", 'Pass test' if is_palindrom_with_helper(' asdsa ') == True else 'Fail test')
    print("'asdsa '", 'Pass test' if is_palindrom_with_helper('asdsa ') == False else 'Fail test')


def verify_question_1c():
    print('Q 1c:')
    print("'??!!@!!??'", 'Pass test' if is_palindrom_no_spaces('??!!@!!??') == True else 'Fail test')
    print("' asdsa          '", 'Pass test' if is_palindrom_no_spaces(' asdsa          ') == True else 'Fail test')
    print("'ima'", 'Pass test' if is_palindrom_no_spaces('ima') == False else 'Fail test')


def verify_question_2():
    print('Q 2:')
    print([(89, 4.5), (95, 5)], 'Pass test' if weighted_average([(89, 4.5), (95, 5)]) == 92.16 else 'Fail test')
    print([(89, 4.5)], 'Pass test' if weighted_average([(89, 4.5)]) == 89.0 else 'Fail test')



def verify_question_3():
    print('Q 3:')
    print(4, 'Pass test' if is_prime(4) == False else 'Fail test')
    print(13, 'Pass test' if is_prime(13) == True else 'Fail test')
    print(169, 'Pass test' if is_prime(169) == False else 'Fail test')
    print(23, 'Pass test' if is_prime(23) == True else 'Fail test')

def verify_question_4():
    print('Q 4:')
    print(8, 'Pass test' if is_perfect(8) == False else 'Fail test')
    print(6, 'Pass test' if is_perfect(6) == True else 'Fail test')
    print(169, 'Pass test' if is_perfect(169) == False else 'Fail test')
    print(28, 'Pass test' if is_perfect(28) == True else 'Fail test')


def verify_question_5():
    print('Q 5:')
    print(8, 'Pass test' if is_7_boom(8) == False else 'Fail test')
    print(14, 'Pass test' if is_7_boom(14) == True else 'Fail test')
    print(143, 'Pass test' if is_7_boom(143) == False else 'Fail test')
    print(47741, 'Pass test' if is_7_boom(47741) == True else 'Fail test')
    print(70, 'Pass test' if is_7_boom(70) == True else 'Fail test')

if __name__ == '__main__':
    verify_question_1a()
    verify_question_1b()
    verify_question_1c()
    verify_question_2()
    verify_question_3()
    verify_question_4()
    verify_question_5()
