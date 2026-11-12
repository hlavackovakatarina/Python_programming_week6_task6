LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def writeFile(Filename: str, Content: str):
    with open(Filename, "w") as file:
        file.write(Content)


def askRows():
    print("Collecting plain text rows for ciphering.")

    rows = ""
    row = input("Insert row(empty stops): ")

    while row != "":
        rows += row + "\n"
        row = input("Insert row(empty stops): ")

    return rows.rstrip("\n")


def shiftCharacter(Character: str, Alphabets: str, Shift: int = 13):

    for i in range(len(Alphabets)):
        if Character == Alphabets[i]:
            newPosition = i + Shift

            if newPosition >= 26:
                newPosition = newPosition - 26

            return Alphabets[newPosition]

    return Character


def rot13(Content: str):
    cipher = ""

    for character in Content:
        if character in LOWER_ALPHABETS:
            cipher += shiftCharacter(character, LOWER_ALPHABETS)

        elif character in UPPER_ALPHABETS:
            cipher += shiftCharacter(character, UPPER_ALPHABETS)

        else:
            cipher += character

    return cipher


def main():
    print("Program starting.\n")

    rows = askRows()

    cipher = rot13(rows)

    print("\n#### Ciphered text ####")
    print(cipher)
    print("\n#### Ciphered text ####")

    filename = input("Insert filename to save: ")

    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        writeFile(filename, cipher)
        print("Ciphered text saved!")

    print("Program ending.")


main()
