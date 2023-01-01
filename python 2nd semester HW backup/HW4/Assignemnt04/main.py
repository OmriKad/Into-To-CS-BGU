from Wizard import *
from School import *
from House import *
from Guider import *


if __name__ == '__main__':
    # Objects creation - School, Houses, Wizards
    s_hogwarts = School(name='Hogwarts', headmaster='Albus Dumbeldore')
    print(s_hogwarts)

    h_griffyndor = House(name='Griffyndor', school=s_hogwarts, head='Prof. McGonnagel', password='grifgrif')
    h_slytherin = House(name='Slytherin', school=s_hogwarts, head='Severus Snape', password='sleek')

    w_harry = Wizard(name='Harry Potter', house=h_griffyndor, potions=75, charms=90)
    w_ron = Wizard(name='Ron Wisely', house=h_griffyndor, potions=65, charms=75)
    w_malfoy = Wizard(name='Draco Malfoy', house=h_slytherin, potions=90, charms=95)
    w_goyle = Wizard(name='Gregory Goyle', house=h_slytherin, potions=65, charms=45)

    # Adding Wizards to Houses
    wiz_list = [w_harry, w_ron, w_malfoy, w_goyle]
    h_griffyndor.add_wizard(wiz_list[:2])
    h_slytherin.add_wizard(wiz_list[2:])
    print(h_griffyndor.is_wizard_in_house(w_harry))  # True
    print(h_slytherin.is_wizard_in_house(w_goyle))  # True

    # Wizard average
    print(w_harry.get_avg()) # 82.5
    w_harry.set_grade(1, 100)
    print(w_harry.get_avg()) # 95.0

    # Enter dormitory
    w_harry.enter_dorm('grifgrif')
    w_ron.enter_dorm('incorrectpassword')
    print(w_harry.is_wizard_in_dorm()) # True
    print(w_ron.is_wizard_in_dorm()) # False
    w_harry.exit_dorm()

    # Wizard comparisons
    print(w_harry == w_malfoy) # False, 95.0 != 92.5
    print(w_ron > w_goyle) # True, 70.0 > 55.0

    # Print Wizard
    print(w_harry) # name: Harry Potter, average: 95.0, house: Gryffindor, in_dorm: False

    # House Tests
    h_griffyndor.get_wizards()

    # Score houses
    h_griffyndor.add_score(50)
    h_slytherin.add_score(45)
    print(h_griffyndor <= h_slytherin) # False, 50 > 45

    # change password
    h_griffyndor.change_password('quidditch')
    w_ron.enter_dorm('quidditch')
    print(w_ron.is_wizard_in_dorm()) # True

    # rank wizards
    print(h_slytherin.rank_wizards(1)) # Should return w_malfoy

    # add houses to School
    houses_list = [h_griffyndor, h_slytherin]
    s_hogwarts.add_house(houses_list)
    print(s_hogwarts.best_house_avg()) # Should return h_gryffindor

    # Guider Class
    g_fred = Guider(name = 'Fred Weesley', house = h_griffyndor, potions = 55, charms = 65, play_quidditch = True)
    print(g_fred) # Guider (Fred Weesley, Gryffindor, 60.0)