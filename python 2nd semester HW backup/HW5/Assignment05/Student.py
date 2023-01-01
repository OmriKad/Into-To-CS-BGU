
from Node import *
from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, head, year, class_number):
        # Creating nodes
        nodes_lst = [Node(i) for i in head]
        # Concatenating nodes
        for i in range(len(nodes_lst) - 1):
            nodes_lst[i].next = nodes_lst[i + 1]
        self.name = name
        if not nodes_lst:
            self.head = None
        else:
            self.head = nodes_lst[0]
        self.year = year
        self.class_number = class_number

    def get_average(self):
        # The function return the average grade of student including the value of all subjects.

        # Case of no subjects
        if self.head is None:
            return 0
        else:
            # Calling the recursive function to get scores
            total_score = self.get_average_help(self.head, 1)
            # Calling the recursive function to get sum of points
            total_points = self.get_average_help(self.head, 0)
            # Formula of weighted average - sum of scores times their corresponding weight(points) divided by the sum
            # of weights(points)
            return total_score / total_points

    def get_average_help(self, obj, target):
        # The recursive function, target parameter helps to differentiate between a call for total points*scores or a
        # call for total points.

        # Base case - the next node is a None. All values are recursively calculated.
        if obj.next is None:
            if target == 1:
                return obj.value.grade * obj.value.points
            if target == 0:
                return obj.value.points
        else:
            # Calls for rec functions with next nodes.
            if target == 1:
                return (obj.value.grade * obj.value.points) + self.get_average_help(obj.next, target)
            if target == 0:
                return obj.value.points + self.get_average_help(obj.next, target)

    # Comparing students is based on their averages, is implemented using total_ordering.
    def __eq__(self, other):
        return self.get_average() == other.get_average()

    def __lt__(self, other):
        return self.get_average() < other.get_average()

    def __repr__(self):
        hebrew_name = ''
        if self.year == 10:
            hebrew_name = 'Yod'
        elif self.year == 11:
            hebrew_name = 'YodAlef'
        elif self.year == 12:
            hebrew_name = 'YodBet'
        str_res = ''
        tmp = self.head
        while tmp is not None:
            str_res += f', {tmp.value.name}({tmp.value.points})-{tmp.value.grade}'
            tmp = tmp.next

        return f'Student:{self.name}, class:{hebrew_name}{self.class_number}' + str_res
