"""
Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову)
в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel.
Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
и после этого выводит получившийся текст на экран.
"""
import re

string = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
         "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
split_string = re.sub('[,.]', '', string).split(' ')
print('ing '.join(split_string))
