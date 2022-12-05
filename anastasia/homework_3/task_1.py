# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero '
new_text = ''

for index, symbol in enumerate(text):
    if symbol.isalpha():
        new_text += symbol
    elif text[index - 1].isalpha():
        new_text += 'ing' + symbol
    else:
        new_text += symbol

print(new_text)

