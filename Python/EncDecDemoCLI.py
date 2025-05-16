import EncDecDemo

enc_key= None
dec_key = None
plaintext = None
cyphertext = None
decryptedtext = None

NoEncKeyMsg = "First Create an encryption key (make enc_key)"
NoDecKeyMsg = "Remember to (re?)create decyption key (make enc_key)"

while True:
    cmdtxt = input("enc> ")
    match cmdtxt:
        case "make enc_key":
            enc_key= EncDecDemo.make_enc_key()
            print("Encryption Key Created:\n", enc_key)
            if(dec_key):
                print(NoDecKeyMsg)
        case "make dec_key":
            if(enc_key):
                dec_key = EncDecDemo.compute_dec_key(enc_key)
                print("Decryption Key Created:\n", dec_key)
            else:
                print(NoEncKeyMsg)
        case "encrypt":
            if(enc_key == None):
                print(NoEncKeyMsg)
            else:
                print("Enter text to encrypt")
                plaintext = input()
                cyphertext = EncDecDemo.encrypt_text(plaintext,enc_key)
                print("Encrypted text is:\n",cyphertext)
        case "decrypt":
            if(dec_key == None):
                print(NoDecKeyMsg)
            else:
                print("Enter text to decrypt")
                cyphertext = input()
                decryptedtext = EncDecDemo.decrypt_text(cyphertext,dec_key)
                print("Decrypted text is:\n",decryptedtext)
        case "exit":
            print ("Till next time...")
            break
        case _:
                print("Unknown command. Try one of: make enc_key, make dec_key, encrypt, decrypt, exit")

