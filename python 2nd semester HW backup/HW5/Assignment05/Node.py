class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        return '[' + str(self.value) + ']'
