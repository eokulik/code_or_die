import string
import math

text_to_encode = input('Enter text to encode (supports just English). ')
value_of_shift = input('Enter integer number for shift. ')

try:
    value_of_shift = int(value_of_shift)
except ValueError:
    print('Please, enter integer number!')
    quit()


def caesar_cipher(text: str, shift_value: int):
    """
    This function uses a Caesar cipher method
    with a given stride to encrypt the data
    """
    encoded_text = ''
    list_from_text = list(text)
    for letter in list_from_text:
        if letter in string.ascii_lowercase:
            """
            Because of register dependency there was a
            need to work through letters firstly in
            lowercase and then in uppercase
            """
            ind = string.ascii_lowercase.index(letter)
            new_index = ind + shift_value
            ascii_len = len(string.ascii_lowercase)
            """
            Here we need to think about situations when program works
            through last letters of the alphabet or too big shift value
            """
            if new_index > ascii_len:
                new_index = new_index - (math.trunc(new_index / ascii_len)
                                         * ascii_len)
            letter = string.ascii_lowercase[new_index]
        elif letter in string.ascii_uppercase:
            ind = string.ascii_uppercase.index(letter)
            new_index = ind + shift_value
            ascii_len = len(string.ascii_uppercase)
            if new_index > ascii_len:
                new_index = new_index - (math.trunc(new_index / ascii_len)
                                         * ascii_len)
            letter = string.ascii_uppercase[new_index]
        encoded_text += letter
    return encoded_text


def caesar_decipher(text: str, shift_value: int):
    """
    This function uses a Caesar cipher method
    with a given step to decrypt the data.
    There was a possibility to use description or encryption in one
    function with extra param that is True or False,
    but decision was made not to have too complicated function
    """
    encoded_text = ''
    list_from_text = list(text)
    for letter in list_from_text:
        if letter in string.ascii_lowercase:
            """
            Because of register dependency there was a
            need to work through letters firstly in
            lowercase and then in uppercase
            """
            ind = string.ascii_lowercase.index(letter)
            ascii_len = len(string.ascii_lowercase)
            """
            Here we need to think about situations when program works
            through last letters of the alphabet or too big shift value
            """
            if shift_value > ascii_len:
                shift_value = shift_value - (math.trunc
                                             (shift_value / ascii_len)
                                             * ascii_len)
            new_index = ind - shift_value
            letter = string.ascii_lowercase[new_index]
        elif letter in string.ascii_uppercase:
            ind = string.ascii_uppercase.index(letter)
            ascii_len = len(string.ascii_uppercase)
            if shift_value > ascii_len:
                shift_value = shift_value - (math.trunc
                                             (shift_value / ascii_len)
                                             * ascii_len)
            new_index = ind - shift_value
            letter = string.ascii_uppercase[new_index]
        encoded_text += letter
    return encoded_text


print(caesar_cipher(text_to_encode, value_of_shift))
text_to_decode = input('Enter text to decode (supports just English). ')
print(caesar_decipher(text_to_decode, value_of_shift))
