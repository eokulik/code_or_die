# Напишите программу, которая добавляет ‘ing’ к словам (к каждому слову) в тексте
# “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,
# dignissim vitae libero”
# и после этого выводит получившийся текст на экран.

my_text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. ' \
          'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
list_from_text = my_text.split()
middle_text = []
for word in list_from_text:
    if word.endswith(','):
        word = word.replace(',', 'ing,')
    elif word.endswith('.'):
        word = word.replace('.', 'ing.')
    else:
        word = word + 'ing'
    middle_text.append(word)
final_text = ' '.join(middle_text)
print(final_text)
