from hw3 import *


def verify_question_1():
    board = [
        [True, False, False],
        [True, True, False],
        [False, False, True],
    ]
    rows_constraints = [1, 2, 1]
    columns_constraints = [2, 1, 1]
    # should print True
    print(verify_nonogram_board(board, rows_constraints, columns_constraints))

    board = [
        [True, False, False],
        [True, False, True],
        [True, True, False],
    ]
    rows_constraints = [1, 2, 2]
    columns_constraints = [3, 1, 1]
    # should print False
    print(verify_nonogram_board(board, rows_constraints, columns_constraints))


def verify_question_2():
    # PART A
    text = 'AbCdE'
    # should print ['A', 'C', 'E']
    print(get_all_capital_letters(text))

    # PART B
    text = 'Dormam4mu I’ve co|me to bar+gain'
    # should print ['Dormammu', 'Ive', 'come', 'to', 'bargain']
    print(split_text_to_tokens(text))

    # PART C
    text = ' yO a^ReC sO    “funny”'
    # should print 0.375
    print(float(grade_text_tone(text)))


def verify_question_3():
    # PART A
    students_raw_submissions = [
        "Ada Lovelace|Who wrote the fiRst Algorithm??",
        "Allen turing|I cracked tHe Enigma machine",
        "Rick SanChez|I don't make mistakes",
        "Ada lovelace|I wrOte the fiRst Algorithm"
    ]
    # should print the following dictionary
    # {
    #     'Ada Lovelace': "I wrOte the fiRst Algorithm",
    #     'Allen Turing': "I cracked tHe Enigma machine",
    #     'Rick Sanchez': "I don't make mistakes"
    # }
    print(register_students_submissions(students_raw_submissions))

    # PART B
    students_submissions = {'Ada Lovelace': 'Hi DarK MoOn',
                            'Allen Turing': 'I',
                            'Rick Sanchez': "I don't CONFOUND TO THESE CONSTRAINTS OF ARTIFICIAL LANGUAGE AND OR MIND CONTROL"}
    # should print the following dictionary
    #    {'Ada Lovelace': '0.5000',
    #    'Allen Turing': 'F',
    #    'Rick Sanchez': 'F'}
    print(grade_students_submissions(students_submissions))

    # PART C
    students_submissions = {'Ada Lovelace': 'I wrOte the fiRst Algorithm',
                            'Allen Turing': 'I cracked the enigma machine',
                            'Rick Sanchez': "I went back in time and cRACked the e'nigma MachIne too"}
    # should print the following dictionary
    # {'i': 3, 'wrote': 1, 'the': 3,
    # 'first': 1, 'algorithm': 1, 'cracked': 2,
    # 'enigma': 2, 'machine': 2, 'went': 1,
    # 'back': 1, 'in': 1, 'time': 1,
    # 'and': 1, 'too': 1}
    print(calculate_tokens_frequencies(students_submissions))


if __name__ == '__main__':
    verify_question_1()
    verify_question_2()
    verify_question_3()
