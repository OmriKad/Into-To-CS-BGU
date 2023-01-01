from HW1 import *
#from unittest import TestCase

#class TestBoard(TestCase):
 #   def test_q1(self):

print("################# Q1 - Tests #################")
print(float == type(question1(4, 6, 7, 9)))
print(4.24 == question1(4, 6, 7, 9))
print(11.40 == question1(11, 1, 0, 4), "the 11.40 test")
print(question1(11, 1, 0, 4), "correct answer is 11.40")
print(3.16 == question1(2, 2, 5, 3))

print("################# Q2 - Tests #################")
print(str == type(question2([4, 1, 0], [2, 3, 0])))
print("JACKPOT" == question2([4, 1, 0], [2, 3, 0]))
print("JACK WHO" == question2([4, 1, 0], [2, 6, 1]))
print("ALMOST" == question2([4, 1, 0], [2, 3, 1]))

print("################# Q3 - Tests #################")
print(str == type(question3("a@b!Ba")))
print("Palindrome" == question3("a@b!Ba"))
print("Not Palindrome" == question3("raCE a cAr"))
print("Palindrome" == question3("Yo, banana boy!"))
print("Palindrome" == question3(""))
print("Palindrome" == question3("a@1bb1a"))


print("################# Q4 - Tests #################")
print(int == type(question4([1, 1, 2, 2, 3, 3])))
print(3 == question4([1, 1, 2, 2, 3, 3]))
print(2 == question4([1, 1, 2, 3]))
print(4 == question4([1, 2, 3, 4, 5, 6, 7, 8]))
print(4 == question4([1, 1, 2, 2, 3, 3, 4, 6]))
print(2 == question4([1, 1, 1, 1, 3, 1, 3]))
print(2 == question4([1, 1, 2, 2]))

print("################# Q5 - Tests #################")
print(int == type(question5(0)))
print(-1 == question5(0))
print(-1 == question5(1))
print(3 == question5(5))
print(2 == question5(11))
print(-1 == question5(8))
print(5 == question5(89))
print(0 == question5(47))
