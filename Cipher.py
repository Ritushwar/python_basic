text = "Hello World"
custom_key = 'python'
def cipher(message,key,direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char #append any non letter tp f_m
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message
def encrypt(message,key):
    return cipher(message,key)
def decrypt(message,key):
    return cipher(message,key,-1)
encrypt_text = encrypt(text,custom_key)
print(f'Encrypt message is {encrypt_text}')
decrypt_text = decrypt(encrypt_text,custom_key)
print(f'Decrypt message is {decrypt_text}')