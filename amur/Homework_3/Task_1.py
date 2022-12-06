text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. " \
       "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"

list_from_text = text.split()
new_text = ''

for word in list_from_text:
    if word[-1].isalpha():
        word += 'ing'
    else:
        word = word[:-1] + 'ing' + word[-1]
    new_text = new_text + ' ' + word

print(new_text.lstrip())
