from Collection import Collection
from Exceptions import NoSuchDominoException
from Domino import Domino


class Hand(Collection):
    def __init__(self, dominoes):
        Collection.__init__(self, dominoes)

    def add(self, domino, index=None):
        if index is None:
            self.array.append(domino)
        else:
            self.array.insert(index, domino)

    def remove_domino(self, domino):
        if domino not in self.array:
            raise NoSuchDominoException["The given piece is not on the board."]
        else:
            indx = self.array.index(domino)
            self.array.remove(domino)
            return indx

    def __getitem__(self, i):
        try:
            return self.array[i]
        except:
            return None

    def __contains__(self, key):
        if key in self.array:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.array == other.array:
            return True
        else:
            return False

    def __ne__(self, other):
        if Hand.__eq__(self, other):
            return False
        else:
            return True
