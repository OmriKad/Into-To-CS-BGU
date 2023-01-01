class Collection:
    def __init__(self, array):
        self.array = array

    def get_collection(self):
        return self.array

    def add(self, item, option):
        raise NotImplementedError("This method is not implemented with this class")

    def __getitem__(self, i):
        try:
            return self.array[i]
        except IndexError:
            return None

    def __eq__(self, other):
        for i in range(0, len(other)):
            if self[i] != other[i]:
                return False
        else:
            return True

    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True

    def __len__(self):
        return len(self.array)

    def __contains__(self, item):
        return Collection.__eq__(self, item)

    def __str__(self):
        return str(''.join([str(x) for x in self.array]))

    def __repr__(self):
        return Collection.__str__(self)
