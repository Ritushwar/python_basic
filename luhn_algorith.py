def main():
    card_number = '4111-1111-4555-1142'
    translation_table = str.maketrans({'-':'',' ':''})   #translation table
    translated_card_number = card_number.translate(translation_table)
    if verify(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')
def verify(card_number):
    reversed_card_number = card_number[::-1]     #making the card number reversed
    odd_digits = reversed_card_number[::2]       #taking first odd space number
    sum_of_odd_digits = 0
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    even_digits = reversed_card_number[1::2]    #taking the even space number
    sum_of_even_digits = 0
    for digit in even_digits:
        number = int(digit)*2
        if number >= 10:
            number = (number//10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0
main()