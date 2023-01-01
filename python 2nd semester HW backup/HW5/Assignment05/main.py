from Subject import *
from Student import *
from ClassRoom import *
from School import *
from Year import *


if __name__ == '__main__':
    # Subject Class
    Algebra = Subject('Algebra', 89, 4.5)
    Hedva = Subject('Hedva', 67, 5)
    print(Algebra)
    print(Hedva)

    # Student Class
    Algebra = Subject('Algebra', 89, 4.5)
    Hedva = Subject('Hedva', 67, 5)
    uriel = Student('uriel', [Algebra, Hedva], 10, 1)
    yohai = Student('Yohai', [Subject('Algebra', 98, 4.5), Subject('Hedva', 90, 5)], 12, 3)
    print(uriel.get_average())
    print(uriel)
    print(yohai)
    print(uriel >= yohai)
    print(uriel > yohai)
    print(uriel <= yohai)
    print(uriel < yohai)
    print(uriel == yohai)
    print(uriel != yohai)

    # ClassRoom Class
    yod1 = ClassRoom(10, 1, [uriel, Student('Yael', [], 10, 1)])
    yod_bet_3 = ClassRoom(12, 3, [yohai])
    print(yod1)
    print(yod_bet_3)

    # Queue Class
    q = s_queue()
    q.enqueue('ma')
    q.enqueue('kore')
    q.enqueue('ah')
    q.enqueue('shelo')
    q.enqueue('gibor?')
    print(q.front())
    print(q.rear())
    print(q.dequeue())
    print(len(q))
    print(q.front())
    print(q.rear())

    # Year Class
    yod = Year(10, [yod1])
    yod_alef = Year(11, [])
    print(yod)
    print(yod_alef)

    # School Class
    Algebra = Subject('Algebra', 89, 4.5)
    Hedva = Subject('Hedva', 67, 5)
    uriel = Student('uriel', [Algebra, Hedva], 10, 1)
    yohai = Student('Yohai', [Subject('Algebra', 98, 4.5), Subject('Hedva', 90, 5)], 12, 3)
    yuvali = Student('Yuvali', [Subject('Algebra', 99, 4.5), Subject('Hedva', 99, 5)], 11, 3)
    hnana = Student('Hnana', [Subject('Algebra', 100, 4.5)], 11, 4)
    yod1 = ClassRoom(10, 1, [uriel, Student('Yael', [], 10, 1)])
    yod_bet_3 = ClassRoom(12, 3, [yohai])
    yod_alef_3 = ClassRoom(11, 3, [yuvali])
    yod_alef_4 = ClassRoom(11, 4, [hnana])
    yod = Year(10, [yod1])
    yod_alef = Year(11, [yod_alef_3, yod_alef_4])
    yod_bet = Year(12, [yod_bet_3])
    ort_arad = School('Ort_arad', [yod, yod_alef, yod_bet])
    print(ort_arad.get_excellent())


