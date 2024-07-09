alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]




continuar = "yes"

def cesar(text, shift, direction):
    if direction == "encode":
        encrypt_text = ""
        for el in text:
            if el in alphabet:
                index = alphabet.index(el)
                if index + shift >= alphabet_len:
                    index = index + shift - alphabet_len
                    encrypt_text += alphabet[index]
                else:
                    encrypt_text += alphabet[index + shift]
            else:
                encrypt_text += el
        print(encrypt_text)
    elif direction == "decode":
        decrypt_text = ""
        for el in text:
            if el in alphabet:
                index = alphabet.index(el)
                decrypt_text += alphabet[index - shift]
            else:
                decrypt_text += el
        print(decrypt_text)

while continuar == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    alphabet_len = len(alphabet)
    cesar(text=text,shift=shift,direction=direction)
    continuar = input("Desea continuar yes or no ")