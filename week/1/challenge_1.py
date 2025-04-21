def reversed_password(password):
    reversed_password = ''
    count = -1
    for i in password:
        reversed_password += password[count]
        count -= 1
    return reversed_password


def uppercase_password(password):
    return password.upper()


def no_vowel_password(password):
    vowel = ['a', 'e', 'i', 'o', 'u']
    new_password = ''
    for i in password:
        if i in vowel:
            i = ''
        new_password += i
    return new_password


def encrypted_password(password):
    import random
    simbols_and_numbers = ['!', '@', '#', '$', '%', '&', '*',
                           '0', '1', '2', '3', '4', '5', '6',
                           '7', '8', '9',
                           ]
    vowel = ['a', 'e', 'i', 'o', 'u']
    new_password = ''
    for i in password:
        if i in vowel:
            i = random.choice(simbols_and_numbers)
        new_password += i
    return new_password


original_password = input("Enter a password: ")

print(
    f"Original password: {original_password}\n"
    f"Reversed passowrd: {reversed_password(original_password)}\n"
    f"Uppercase passord: {uppercase_password(original_password)}\n"
    f"No vowels passoword: {no_vowel_password(original_password)}\n"
    f"Encrypted password: {encrypted_password(original_password)}\n"
)
