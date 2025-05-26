import EncDecDemo

enc_key= None
dec_key = None
plaintext = None
cyphertext = None
decryptedtext = None
enc_key_file = ""
dec_key_file = ""

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
        case "load":                
                enc_key = EncDecDemo.save_load("enc_key.json","Load")
                dec_key = EncDecDemo.save_load("dec_key.json","Load")
                if (enc_key == None or dec_key == None):
                    print("Please verify saved key files (enc_key.json & dec_key.json) exist in the application directory")
                else:
                     print("Encryption Key Loaded:\n", enc_key)
                     print("Decryption Key Loaded:\n", dec_key)

        case "save":
                EncDecDemo.save_load("enc_key.json","Save",enc_key)                
                EncDecDemo.save_load("dec_key.json","Save",dec_key)
                
        case "exit":
            print ("Till next time...")
            break
        case _:
                print("Unknown command. Try one of: make enc_key, make dec_key, encrypt, decrypt, exit")

