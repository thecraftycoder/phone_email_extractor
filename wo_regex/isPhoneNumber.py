'''
Goal: Finding a US phone number in a string

Pattern: three numbers, a hyphen, three numbers, a hyphen, and four numbers

Ex: 415-555-4242

Returns: True or False
'''

def isPhoneNumber(text):
    # is the string exactly 12 characters?
    if len(text) != 12:
        return False
    # Checking area code: are the first 3 characters integers?
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    # Checking the rest of the pattern: is the 4th character a hyphen?
    if text[3] != '-':
        return False
    # Do three more numbers follow the first hyphen (index 4, 5, 6)
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    # is the 8th character a hyphen?
    if text[7] != '-':
        return False
    # Do four numbers follow the second hyphen (index 8, 9, 10, 11)
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    # If the string passes all the checks, return True
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]

    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)

print('Done.')