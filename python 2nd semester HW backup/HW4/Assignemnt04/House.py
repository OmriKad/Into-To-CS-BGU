import copy


class House:
    def __init__(self, name, school, head, password, score=0, wizard_list=[]):
        self.name = name
        self.school = school
        self.head = head
        self.password = password
        self.score = score
        self.wizard_list = copy.copy(wizard_list)

    def get_wizards(self):
        # Returns list of wizards.
        return self.wizard_list

    def set_head(self, head):
        # Setting headmaster.
        self.head = head

    def add_score(self, points):
        # Adding score for house as int.
        self.score += points

    def change_password(self, new_password):
        # Changing house password for dorm entry use.
        self.password = new_password

    def add_wizard(self, wiz):
        # Adding a wizard to the house. Only adds wizards that aren't already in the wizard list.
        for i in wiz:
            if not self.is_wizard_in_house(i):
                i.house = self
                self.wizard_list.append(i)

    def is_wizard_in_house(self, wiz):
        # The method check if a wizard is already in the house using recursion.
        wiz_lst = self.get_wizards()
        # Calling helper function passing the wizard, the wizard list and 0 index.
        return self.is_wizard_in_house_helper(wiz, wiz_lst, 0)

    def is_wizard_in_house_helper(self, wiz, wiz_lst, indx):
        # Base case, the index is out of list bounds and the wizard wasn't found.
        if indx > len(wiz_lst) - 1:
            return False
        # Base case, wizard was found.
        if wiz_lst[indx] == wiz:
            return True
        # Recursive calling with index going up.
        else:
            return self.is_wizard_in_house_helper(wiz, wiz_lst, indx + 1)

    def rank_wizards(self, rank):
        # This function takes an int as a rank position regarding score average and returns the corresponding wizard
        # in that place. The sorting is being implemented using a recursive merge-sort.

        # Case of rank input that is non-whole number.
        if rank <= 0:
            return None
        # A list holding all wizards averages - non-sorted.
        avgs_lst = []
        # Filling the averages list using a for loop.
        for i in self.wizard_list:
            avgs_lst.append(i.get_avg())
        # The list sorting part, calling the merge-sort method.
        ranked_avgs_list = self.__mergeSort(avgs_lst)
        if rank <= len(ranked_avgs_list):
            return self.wizard_list[avgs_lst.index(ranked_avgs_list[rank * -1])]
        else:
            return self.wizard_list[avgs_lst.index(ranked_avgs_list[0])]

    def __mergeSort(self, lst):
        # A private method, only accessed through public "rank_wizards". Uses recursion of merge-sort to sort a list of
        # averages. The sort has a time complexity of O(n*log(n)).

        # With each iteration the lst is being separate into 2 parts. Base case is when the sub list is less or
        # equal to 1.
        l = len(lst)
        if l <= 1:
            return lst
        else:
            return self.__merge(self.__mergeSort(lst[0:l // 2]), self.__mergeSort(lst[l // 2:l]))

    def __merge(self, A, B):
        # The merge function of the merge-sort function. Its part is combining the deformed section by order.
        n, m, a, b, c = len(A), len(B), 0, 0, 0
        C = [0] * (n * m)
        while a < n and b < m:
            if A[a] < B[b]:
                C[c], a = A[a], a + 1
            else:
                C[c], b = B[b], b + 1
            c += 1
        C[c:] = A[a:] + B[b:]
        return C

    def __repr__(self):
        # The representation for the house. First takes all names field and then adds them to a specific concatenation
        # with "|" separating them on between.
        names_list = [i.name for i in self.wizard_list]
        res = ""
        for i in names_list:
            if i == names_list[-1]:
                res = res + i
            else:
                res = res + i + " | "
        return f"House of {self.name} has {self.score} points. The proud wizards on {self.name} are:\n{res}"

    def __eq__(self, other):
        # A House type is equal to another only if their scores are the same.
        if self.score == other.score:
            return True
        else:
            return False

    def __ne__(self, other):
        # Checks for equality and returns the opposite.
        return not self == other

    def __gt__(self, other):
        # Compares both scores, if self score is greater returns True.
        if self.score > other.score:
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

    def __contains__(self, wizard_name):
        # Returns a boolean of a given name is in the house wizard list.
        for i in self.get_wizards():
            if i.name == wizard_name:
                return True
            else:
                return False

