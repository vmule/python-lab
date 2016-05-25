import random

def getChar():
    char = chr(random.randint(97, 122))
    return char

def getNumber():
    num = str(random.randint(0,9))
    return num

def getSpecialChar():
    special_char  = chr(random.randint(33, 47))
    return special_char

symbol_num = 0
upper_char_number = 0
lower_char_number = 0
number = 0

password_string = ''

while len(password_string) < 15:
    iterator = random.randint(0,2) + 1

    if iterator == 1 and (upper_char_number < 3 or lower_char_number < 3):
        char = getChar()
        if  lower_char_number < 3:
            password_string = password_string + char
            lower_char_number += 1
            #print 'lower_char_number', lower_char_number
        else:
            char_up = char.upper()
            #print char_up
            password_string = password_string + char_up
            upper_char_number += 1
            #print 'upper_char_number', upper_char_number
    elif iterator == 2 and number < 3:
        number += 1
        num_str = str(getNumber())
        password_string = password_string + num_str
    elif iterator == 3 and symbol_num < 6:
        special_char = getSpecialChar()
        symbol_num += 1
        password_string = password_string + special_char

print password_string
