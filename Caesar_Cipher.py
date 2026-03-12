# Caesar Cipher Decoder
import time

cipher_text = list(input("Enter ciphertext: ").lower().strip())
for i in range(26):
    combination = []
    for character in cipher_text:
        if character != " ":
            pos = ord(character) - 97
            posi = (pos + i) % 26
            combination += chr(posi + 97)
        else:
            combination += " "

    print("".join(combination))
    time.sleep(0.2)



# Caesar Cipher Plus Encoder
plaintext = input("Enter plaintext: ").lower().strip()
print(len(plaintext.replace(" ", "")))

password = input("Enter password(It has to be the same lenght as the plaintext), e.g. 22 4 13 2 or 22,4,13,2: ").strip()
tokens = password.replace(",", " ").split()
shifts = [int(t) for t in tokens]

combination = []
letter_index = 0

if len(shifts) != len(plaintext.replace(" ", "")):
    print("Password must match the number of letters(excluding spaces): ")
    password = input("Enter password(It has to be the same lenght as the plaintext), e.g. 22 4 13 2 or 22,4,13,2: ").strip()

letters_only = [l for l in plaintext if l != " "]
combination = []
for character in plaintext:
    if character == " ":
        combination.append(" ")
        continue

    shift = shifts[letter_index]
    letter_index += 1

    pos = ord(character) - 97
    new_pos = (pos + shift) % 26
    combination.append(chr(new_pos + 97))

print("".join(combination))
