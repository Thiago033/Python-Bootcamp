
def encrypt(plainText, shiftAmount):
    cipherText = ""
    
    for letter in plainText:
        position = alphabet.index(letter)
        newPosition = position + shiftAmount
    
        cipherText += alphabet[newPosition]
        
        
        
    print(f"Encoded text is {cipherText}")

def decrypt(cypherText, shiftAmount):
    plainText = ""
    
    for letter in cypherText:
        position = alphabet.index(letter)
        newPosition = position - shiftAmount
        
        plainText += alphabet[newPosition]
        
    print(f"The decoded text is {plainText}")
        
        
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("invalid option!")

