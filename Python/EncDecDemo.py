import string
import random
import json
import os

# A function that creates a and return a key (randomally created)
def make_enc_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet.copy()
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))

# A function that accepts an enc_key and returns a dec key
def compute_dec_key(enc_key):
    alphabet, shuffled = map(list, zip(*list(enc_key.items())))
    return dict(zip(shuffled,alphabet))

# A Function that accepts some clear text and an enc_key, and returns encrypted text
def encrypt_text(text, enc_key):
    cyphertext = ""
    for char in text:
        upper_char = char.upper()
        if upper_char in enc_key:
            cyphertext += enc_key[upper_char] if char.isupper() else enc_key[upper_char].lower()
        else:
            cyphertext += char
    return cyphertext

# A function that accepts some encrypted text and a dec_key and returns clear text
def decrypt_text(text,dec_key):
    return encrypt_text(text, dec_key)

# a function to save or load a dictionary to a json file
def save_load(filename,op,dictvar=None):
    match op:
        case "Load":
            if os.path.exists(filename):
                with open(filename, 'r',) as f:
                    return json.load(f)
            else:
                return None
        case "Save":
            with open(filename, 'w',) as f:
                json.dump(dictvar,f,indent=4)                

# A function that demonstrates it all
def test_all():
    enc_key = make_enc_key()
    dec_key = compute_dec_key(enc_key)

    print("Encryption key is:\n", enc_key)
    print("Decryption key is:\n",dec_key)

    plaintext = "Max was here"
    cyphetext = encrypt_text(plaintext,enc_key)
    dectext = decrypt_text(cyphetext,dec_key)

    print("Cyphher text is:\n", cyphetext)
    print("Decrypted text is:\n", dectext)

#test_all()