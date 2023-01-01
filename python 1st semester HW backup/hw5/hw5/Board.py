from Collection import Collection
from Domino import Domino
from Exceptions import InvalidNumberException, EmptyBoardException, FullBoardException


class Board(Collection):
    def __init__(self, max_capacity):
        array = []
        Collection.__init__(self, array)
        if max_capacity < 1 or max_capacity > 28:
            raise InvalidNumberException("Given number is not between 1 to 28")
        else:
            self.max_capacity = max_capacity
            self.array = array

    def in_left(self):
        if not len(self):
            raise EmptyBoardException('Board is empty!')
        else:
            return Domino.get_left(self[0])

    def in_right(self):
        if not len(self):
            raise EmptyBoardException('Board is empty!')
        else:
            return Domino.get_right(self[-1])

    def add(self, domino, add_to_right=True):
        if len(self) == self.max_capacity:
            raise FullBoardException("The Board is full!!, can't add a piece!")
        else:
            if len(self) == 0:
                self.array.append(domino)
                return True
            else:
                if add_to_right:
                    if Board.in_right(self) == Domino.get_left(domino):
                        self.array.append(domino)
                        return True
                    elif Board.in_right(self) == Domino.get_left(Domino.flip(domino)):
                        self.array.append(Domino.flip(domino))
                        return True
                    else:
                        if self.add_left(domino):
                            return True
                        else:
                            return False
                else:
                    if Board.in_left(self) == Domino.get_right(domino):
                        self.array.insert(0, domino)
                        return True
                    elif Board.in_left(self) == Domino.get_right(Domino.flip(domino)):
                        self.array.insert(0, Domino.flip(domino))
                        return True
                    else:
                        return False

    def add_left(self, domino):
        return Board.add(self, domino, False)

    def add_right(self, domino):
        return Board.add(self, domino)

    def __getitem__(self, i):
        try:
            return self.array[i]
        except Exception:
            return None

    def __contains__(self, key):
        for i in self:
            if key != i:
                return False
            else:
                return True

    def __eq__(self, other):
        if self.max_capacity != other.max_capacity:
            return False
        else:
            for x, y in zip(self, other):
                if x is None:
                    return True
                else:
                    if Domino.get_left(x) != Domino.get_left(y) or Domino.get_right(x) != Domino.get_right(y):
                        return False

    def __ne__(self, other):
        if Board.__eq__(self, other):
            return False
        else:
            return True

