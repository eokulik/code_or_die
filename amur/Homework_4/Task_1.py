from random import choice, randint

try:
    salary = int(input('What is the salary in $? '))
    bonus_variants = [True, False]
    bonus = choice(bonus_variants)

    if bonus is True:
        bonus_value = randint(1, 1000)
        salary += bonus_value
        print('The bonus value is ' + str(bonus_value) + '$')
        print('The salary at this month is: ' + str(salary) + '$')
    else:
        print('The salary at this month is: ' + str(salary) + '$')
        print('No bonuses for this month')

except ValueError:
    print('Please, enter integer number !')
    quit()
