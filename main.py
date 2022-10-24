from random import randint

print("Welcome to password generator. Please specify your requirement")
print("uppercase | lowercase | numbers | special characters")
requirement = input()
length = (requirement.split())[0]
print("Creating a password with " + length + " length!")

upperCase = False
lowerCase = False
numbersCase = False
specialCase = False

if requirement.lower().__contains__("uppercase"):
    upperCase = True
if requirement.lower().__contains__("lowercase"):
    lowerCase = True
if requirement.lower().__contains__("numbers"):
    numbersCase = True
if requirement.lower().__contains__("special character"):
    specialCase = True


def number():
    case_index = randint(1, 4)
    if case_index == 1 and upperCase is True:
        return randint(65, 90)
    elif case_index == 2 and lowerCase is True:
        return randint(97, 122)
    elif case_index == 3 and numbersCase is True:
        return randint(0, 9)
    elif case_index == 4 and specialCase is True:
        special_index = randint(1, 4)
        if special_index == 1:
            return randint(33, 47)
        elif special_index == 2:
            return randint(58, 64)
        elif special_index == 3:
            return randint(91, 96)
        elif special_index == 4:
            return randint(123, 126)


password = ""

while len(password) < int(length):
    character = number()
    if character is not None:
        if 0 <= character <= 9:
            password += str(character)
        else:
            password += chr(character)
print(password)
