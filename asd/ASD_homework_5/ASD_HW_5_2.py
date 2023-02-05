## I've found the bug with combination: Encode 'z' with offset 1 return error:
## IndexError: string index out of range- I've found the issue on stackoverflow:
## https://stackoverflow.com/questions/8712659/python-error-indexerror-string-index-out-of-range
## but have no idea how to fix it

import string


def caesar_coder():
    encoded_text = ''
    text_enc_inp = input('Input a text in English to code it ')
    key = int(input('Input integer number for offset '))
    for i in text_enc_inp:
        if i in string.ascii_lowercase:
            ind = string.ascii_lowercase.index(i)
            new_ind = ind + key
            new_letter = string.ascii_lowercase[new_ind]
            encoded_text += new_letter
        elif i in string.ascii_uppercase:
            ind = string.ascii_uppercase.index(i)
            new_ind = ind + key
            new_letter = string.ascii_uppercase[new_ind]
            encoded_text += new_letter
        else:
            encoded_text += i
    print(encoded_text)


def caesar_decoder():
    decoded_text = ''
    text_dec_inp = input('Input a text in English to decode it ')
    key = int(input('Input integer number for offset '))
    for i in text_dec_inp:
        if i in string.ascii_lowercase:
            ind = string.ascii_lowercase.index(i)
            new_ind = ind - key
            new_letter = string.ascii_lowercase[new_ind]
            decoded_text += new_letter
        elif i in string.ascii_uppercase:
            ind = string.ascii_uppercase.index(i)
            new_ind = ind - key
            new_letter = string.ascii_uppercase[new_ind]
            decoded_text += new_letter
        else:
            decoded_text += i
    print(decoded_text)


def operation():
    operation_code = int(input('''
    Please select the option:
    1.Encode a text in English
    2.Decode a text in English
    '''))
    if operation_code not in range(1, 3):
        print("Incorrect option")
    else:
        if operation_code == 1:
            caesar_coder()
        elif operation_code == 2:
            caesar_decoder()


def again():
    calc_again = input('''
Would you like to try again?
If 'yes', type '+', if 'no' type '-'.
''')
    if calc_again.upper() == '+':
        operation()
    elif calc_again.upper() == '-':
        print('See you :) ')
        exit()


operation()

while True:
    again()
