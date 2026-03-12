# Caesar Cipher Tools (Decoder + Caesar Cipher Plus)

This repo contains two small Python scripts in one file:

1) **Caesar Cipher Decoder (Brute Force)**  
   Tries all 26 shifts and prints every possible plaintext (useful when you don't know the shift).

2) **Caesar Cipher Plus Encoder**  
   A variant where **each letter can have a different shift**, controlled by a numeric "password" like:
   - `22 4 13 2`
   - `22,4,13,2`

Spaces in the plaintext are preserved and **do not consume shifts**.

---

## Features

### Caesar Cipher Decoder
- Brute-forces all 26 rotations
- Keeps spaces
- Small delay between outputs (`time.sleep(0.2)`) so it’s easier to read

### Caesar Cipher Plus Encoder
- Different shift per character (Vigenère-like idea, but with explicit numeric shifts)
- Password input supports spaces or commas
- Checks that the number of shifts matches the number of letters (excluding spaces)
- Preserves spaces

---

## Requirements
- Python 3.x

---

## How to Run

Clone the repo and run:

```bash
python your_file_name.py

You will be prompted for inputs.

Usage Examples
1) Caesar Cipher Decoder

When asked:

Enter ciphertext:

Type something like:

khoor zruog

You will see 26 candidate outputs (one per shift). One of them should read:

hello world
2) Caesar Cipher Plus Encoder

When asked:

Enter plaintext:

Example:

hola amigo

Then enter a password with one number per letter (excluding spaces).

Plaintext hola amigo has 8 letters + 1 space → you need 8 numbers.

Example password:

Space-separated:

1 4 2 3 1 1 0 2

Comma-separated:

1,4,2,3,1,1,0,2

Output will be the encoded text with per-letter shifting.

Notes / Limitations

Only designed for lowercase a–z letters and spaces.

Punctuation (.,!? etc.) is not handled specially.

This is an educational toy cipher (not secure for real cryptography).
