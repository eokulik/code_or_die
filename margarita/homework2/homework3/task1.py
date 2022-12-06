text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel.' \
       ' Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
text_list = text.split()
print(text_list)
new_text = []
for word in text_list:
    print(word + 'ing')
    if word.endswith(','):
        word = word.rstrip(',')
        word = word + 'ing,'
    elif word.endswith('.'):
        word = word.rstrip('.')
        word = word + 'ing.'
    else:
        word = word + 'ing'
    new_text.append(word)
print(' '.join(new_text))
