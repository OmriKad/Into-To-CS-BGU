from Stack import *


class ClassRoom(Stack):
    def __init__(self, year, class_number, students_lst):
        super().__init__()
        self.year = year
        self.class_number = class_number
        for i in students_lst:
            self.push(i)

    def __repr__(self):
        hebrew_name = ''
        if self.year == 10:
            hebrew_name = 'Yod'
        elif self.year == 11:
            hebrew_name = 'YodAlef'
        elif self.year == 12:
            hebrew_name = 'YodBet'
        return f'Class {hebrew_name}{self.class_number}, {self.len} students.'
