text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' \
       'Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'

split_text = text.split()
text1 = []

for word in split_text:
    if word.endswith('.'):
        word = word.replace('.', 'ing,')
    elif word.endswith(','):
        word = word.replace(',', 'ing.')
    else:
        word = word + 'ing'
    text1.append(word)
text2 = ' '.join(text1)

print(text2)
