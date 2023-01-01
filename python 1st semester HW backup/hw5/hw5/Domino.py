from Exceptions import InvalidNumberException


class Domino:
    def __init__(self, left, right):
        if left > 6 or left < 0 or right > 6 or right < 0:
            raise InvalidNumberException("Invalid number - Given number is greater than 6 or negative")
        else:
            self.__left = left
            self.__right = right

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def __str__(self):
        return '[' + str(self.get_left()) + '|' + str(self.get_right()) + ']'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if (self.get_right() == other.get_right() and self.get_left() == other.get_left()) or (self.get_left() == other.get_right() and self.get_right() == other.get_left()):
            return True
        else:
            return False

    def __ne__(self, other):
        if Domino.__eq__(self, other):
            return False
        else:
            return True

    def __gt__(self, other):
        if self.get_left() + self.get_right() > other.get_left() + other.get_right():
            return True
        else:
            return False

    def __contains__(self, key):
        if key == self.get_left() or key == self.get_right():
            return True
        else:
            return False

    def flip(self):
        return Domino(self.__right, self.__left)



