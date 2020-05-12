import random


def passwd_correct(upper, lower, spec, nos, alphabets, special, numbers, count):
    for char_type in [upper, lower, spec, nos]:
        # 'count' is used to count the no of lists(upper, lower, spec, nos) which are empty
        if len(char_type) == 0:
            count += 1
        if len(char_type) == 0 and char_type == upper:
            char_type.append((random.choice(alphabets).upper()))
        elif len(char_type) == 0 and char_type == lower:
            char_type.append(random.choice(alphabets))
        elif len(char_type) == 0 and char_type == spec:
            char_type.append(random.choice(special))
        elif len(char_type) == 0 and char_type == nos:
            char_type.append(random.choice(numbers))
    for i in range(count):
        if len(upper) > 1:
            upper.pop()
        elif len(lower) > 1:
            lower.pop()
        elif len(spec) > 1:
            spec.pop()
        elif len(nos) > 1:
            nos.pop()
    new_password = ''
    for char_type in [upper, lower, spec, nos]:
        for char in char_type:
            new_password += char
    print(f"Corrected Password:{new_password}")