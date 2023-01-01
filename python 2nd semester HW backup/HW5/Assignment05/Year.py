from s_queue import *


class Year:
    def __init__(self, year_number, classes_queue):
        self.year_number = year_number
        self.classes_queue = s_queue()
        for i in classes_queue:
            self.classes_queue.enqueue(i)

    def count_classes(self):
        return self.classes_queue.len

    def __repr__(self):
        hebrew_name = ''
        if self.year_number == 10:
            hebrew_name = 'Yod'
        elif self.year_number == 11:
            hebrew_name = 'YodAlef'
        elif self.year_number == 12:
            hebrew_name = 'YodBet'
        return f'School year {hebrew_name}, {self.count_classes()} classes.'
