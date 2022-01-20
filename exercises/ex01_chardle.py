"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730427941

a: int = 0

word: str = (input("Enter a 5-character word: "))

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = (input("Enter a single character: "))

if len(character) != 1:
    print("Error: Character must be a single character")
    exit()

print("searching for " + character + " in " + word)

if character == word[0]:
    print(character + " found at index 0")
    a = a + 1


if character == word[1]:
    print(character + " found at index 1")
    a = a + 1


if character == word[2]:
    print(character + " found at index 2")
    a = a + 1

if character == word[3]:
    print(character + " found at index 3")
    a = a + 1

if character == word[4]:
    print(character + " found at index 4")
    a = a + 1

if a == 0:
    print("No instances of " + character + "found in " + word)
else:
    print(a, "instances of " + character + " found in " + word)