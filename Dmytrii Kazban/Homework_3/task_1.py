str = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,' \
      ' dignissim vitae libero'

words = str.split()
words_with_ing = [word + "ing" for word in words]
modified_sentence = " ".join(words_with_ing)
print(modified_sentence)
