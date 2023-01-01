class Wizard:
    def __init__(self, name, house, potions, charms, in_dorm=False):
        self.name = name
        self.house = house
        self.potions = potions
        self.charms = charms
        self.in_dorm = in_dorm

    def get_avg(self):
        # Returns the average score of a student.
        return (self.charms + self.potions) / 2

    def enter_dorm(self, password):
        # Every house has a specific password for entry, the password is defined as a field in the house class.
        if password == self.house.password:
            self.in_dorm = True
        # Message indicating for a wrong password.
        else:
            return "wrong password, try again."

    def exit_dorm(self):
        # Leaving the dorm.
        self.in_dorm = False

    def set_grade(self, course, grade):
        # Grade setter function, 1 represent potions and 2 for charms.
        if course == 1:
            self.potions = grade
        elif course == 2:
            self.charms = grade

    def is_wizard_in_dorm(self):
        # Returns the current field state.
        return self.in_dorm

    def __repr__(self):
        return f"name: {self.name}, average: {self.get_avg()}, house: {self.house.name}, in_dorm: {self.is_wizard_in_dorm()}"

    def __eq__(self, other):
        # A wizard type is equal to another only if their averages are the same.
        if self.get_avg() == other.get_avg():
            return True
        else:
            return False

    def __ne__(self, other):
        # Checks for equality and returns the opposite.
        return not self == other

    def __gt__(self, other):
        # Compares both averages, if self average is greater returns True.
        if self.get_avg() > other.get_avg():
            return True
        else:
            return False

    def __lt__(self, other):
        # Checks for __gt__ and returns the opposite.
        return not self > other

    def __ge__(self, other):
        # Combination of either __gt__ or __eq__.
        if self > other or self == other:
            return True
        else:
            return False

    def __le__(self, other):
        # Combination of either __lt__ or __eq__.
        if self < other or self == other:
            return True
        else:
            return False

