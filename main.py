# rot-13 cyper function
# rotation of each alphabet to 13 places ahead of the alphabet.
encryption = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', 
   'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')

# a fucntion to translate the text into a cypher
def encrypt(text): 
   return text.translate(encryption)


if __name__== "__main__":
    text_to_encrypt = input()
    print (encrypt(text_to_encrypt))