"""
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
и после этого выводит получившийся текст на экран.
"""
import re

string = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
         "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"


def add_ing_ending(word):
    if len(re.findall('[,.]', word)):
        word = word[:-1] + 'ing' + word[-1]
    else:
        word = word + 'ing'
    return word


result = ' '.join(list(map(add_ing_ending, string.split(' '))))
print(result)
