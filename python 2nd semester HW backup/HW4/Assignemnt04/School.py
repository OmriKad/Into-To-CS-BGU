import copy


class School:
    def __init__(self, name, headmaster, houses=[]):
        self.name = name
        self.headmaster = headmaster
        self.houses = copy.copy(houses)

    def set_name(self, new_name):
        # Setter for school name.
        self.name = new_name

    def add_house(self, houses):
        # Adding a new house to the school house list only if it's not already there.
        for i in houses:
            if i not in self.houses:
                i.school = self
                self.houses.append(i)

    def set_headmaster(self, new_headmaster):
        # Setter for school headmaster.
        self.headmaster = new_headmaster

    def best_house_avg(self):
        # The function returns the house with the best overall average. The sorting is being implemented using
        # merge-sort.
        house_avgs = []
        for i in self.houses:
            temp = 0
            for j in i.get_wizards():
                temp += j.get_avg()
            house_avgs.append(temp/len(i.get_wizards()))
        sorted_house_avgs = self.__mergeSort(house_avgs)
        return self.houses[house_avgs.index(sorted_house_avgs[-1])]

    def best_house_score(self):
        # The function returns the house with the best score. The sorting is being implemented using
        # merge-sort.
        houses_scores = [i.score for i in copy.copy(self.houses)]
        ranked_houses = self.__mergeSort(houses_scores)
        return ranked_houses[-1]

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
        return f"{self.name} school for witchcraft and wizardry, under head master {self.headmaster}"

