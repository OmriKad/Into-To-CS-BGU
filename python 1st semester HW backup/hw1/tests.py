import question1
import question2
import question3
import question4
import question5


def test_question1():
    leg_a = 10  # Change me!
    leg_b = 40  # Change me!
    question1.question1(leg_a, leg_b)


def test_question2():
    player1 = 'scissors'  # Change me!
    player2 = 'paper'  # Change me!
    question2.question2(player1, player2)


def test_question3():
    input_num = 26  # Change me!
    question3.question3(input_num)


def test_question4():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8]  # Change me!
    question4.question4(input_list)


def test_question5():
    sentence = 'jskladslpbnvjckfhjjd'  # Change me!
    question5.question5(sentence)


if __name__ == '__main__':
    test_question1()
    test_question2()
    test_question3()
    test_question4()
    test_question5()