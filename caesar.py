import string

def alphabet_position(letter):

    alphabet = string.ascii_lowercase
    letter = letter.lower()

    return alphabet.index(letter)

def rotate_character(char,rot):

    if char not in string.ascii_letters:
        return char

    alphabet = string.ascii_lowercase
    pos = alphabet_position(char)
    newPos = (int(pos) + int(rot)) % 26
    newChar = alphabet[newPos]

    if char in string.ascii_uppercase:
        return newChar.upper()

    return newChar
    
def encrypt(text,rot):
    newText = ''


    for char in text:
        newText = newText + str(rotate_character(char,rot))

    return newText
