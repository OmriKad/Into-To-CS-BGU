class Subject:
    def __init__(self, name, grade, points):
        self.name = name
        self.grade = grade
        self.points = points

    def __repr__(self):
        return f'Subject:{self.name}, grade:{self.grade}, points:{self.points}'


