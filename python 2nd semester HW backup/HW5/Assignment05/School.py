import copy


class School:
    def __init__(self, name, school_years):
        self.name = name
        self.school_years = copy.copy(school_years)

    def get_excellent(self):
        # This function returns the top third grades of the students in the current school. If the number is not
        # divisible in 3, the number is rounded up.

        # Case of empty school
        if not self.school_years:
            return []
        # A temp list to hold all classes the school
        classes_tmp = []
        # A final list to hold all the grades of students
        final = []
        # Running on a deep copy of he schools years and dequeue the classes to the temp list
        for i in copy.deepcopy(self.school_years):
            while i.classes_queue.len != 0:
                classes_tmp.append(i.classes_queue.dequeue())
        # Running on the temp list and for each class running on each student and adding their grade to the final list
        for y in classes_tmp:
            for z in y.stack_vals:
                final.append(z.get_average())
        # Sorting the final list in reverse
        final.sort(reverse=True)
        final_len = len(final)
        divisible = final_len % 3
        # The number of students is divisible in 3 so the top third are returned
        if divisible == 0:
            return final[:(final_len / 3)]
        # The number of students is not divisible in 3 so a round up is made to return a third
        else:
            return final[:(final_len + (3 - divisible)) // 3]



