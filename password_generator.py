#!/usr/bin/python3


def password_generator(length=12):
    from random import shuffle
    from time import sleep
    import string

    letters = string.ascii_lowercase + string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    characters = list(letters + digits + punctuation)
    shuffle(characters)

    password = ''
    
    password = ''.join(characters[:length])
   
    return password

print(password_generator())
