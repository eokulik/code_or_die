import random

employees = {'Jim': True, 'Kim': False, 'Tim': True}


def add_bonus():
    name = input('Enter \'stop\' if you want to finish.\nEnter your name:')
    while name != 'stop':
        salary = int(input('Enter your salary:'))
        if name in employees:
            if employees.get(name):
                print(salary + random.randint(500, 1000))
            else:
                print(salary)
        else:
            print('Name is not exist!')
        name = input('Enter \'stop\' if you want to finish.\nEnter your name:')


add_bonus()
