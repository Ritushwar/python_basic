def generate_password(length=8,nums=1,special_char=1,lower_case=1,upper_case=1):
    import re
    import string
    import secrets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_char = letters + digits + symbols
    number = 0
    while True:
        number += 1
        password = ''
        for _ in range(length):
            password += secrets.choice(all_char)
        constraints = [
            (nums,r'\d'),
            (special_char,fr'[{symbols}]'),
            (lower_case,r'[a-z]'),
            (upper_case,r'[A-Z]')
        ]
        #checking all constraints
        if all(
            constraint <= len(re.findall(pattern,password))
            for constraint, pattern in constraints
        ):
            break
    return password,number

new_password ,number= generate_password()
print(f"Password: {new_password}")
print(f"Number: {number}")