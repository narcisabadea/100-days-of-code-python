from logo import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_end = False

while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def cipher(direction, text, shift):
        encoded = ''
        for letter in text:
            position = alphabet.index(letter)
            if direction == 'encode':
                swift = alphabet[position + shift]
            else:
                swift = alphabet[position - shift]

            encoded += swift

        if direction == 'encode':
            print(f"The encoded text is {encoded}")
        else:
            print(f"The decoded text is {encoded}")

    cipher(direction, text, shift)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
