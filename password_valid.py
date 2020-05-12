from password_corrector import passwd_correct
print("""Password must contain atleast 8 characters including uppercase,lowercase,special character 
and number""")
passwd_length = int(input('Enter length of password: '))
password = input("Enter Password: ")
print(password)


def passwd_valid(passwords):
    alphabets = ["a", "b", "c", "d", "e", "f", "g", "h",
                 "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    special = [".", "!", "@", "$", "#", "%", "&", "-", "+", "=", "_", "|", "/", ",", "?", ">", "<", "^", "*", "~"]
    upper = []
    lower = []
    spec = []
    nos = []
    count = 0
    for ch in passwords:
        if len(passwords) < passwd_length or len(passwords) > passwd_length:
            break
        if ch.isalnum():
            if ch.isupper():
                upper.append(ch)
                continue
            if ch.islower():
                lower.append(ch)
                continue
            if ch in numbers:
                nos.append(ch)
                continue
        if ch in special:
            spec.append(ch)
            continue
    # When password is less than passwd_length/greater than passwd_length,then upper,lower,spec and nos list are empty
    if (len(upper) == 0) and (len(spec) == 0) and (len(lower) == 0) and (len(nos) == 0):
        if len(password) < passwd_length:
            print('No of characters less than {passwd_length}!!! Enter Password Again')
        else:
            print('No of characters greater than {passwd_length}!!! Enter Password Again')
    elif (len(upper) != 0) and (len(lower) != 0) and (len(spec) != 0) and (len(nos) != 0):
        print("Valid Password")
    else:
        print("Invalid Password!!!")
        passwd_correct(upper, lower, spec, nos, alphabets, special, numbers, count)


passwd_valid(password)