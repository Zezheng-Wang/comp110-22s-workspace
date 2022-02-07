"""A formal wordle game."""

__author__ = "730427941"

secret: str = "codes"


def contains_char(a: str, b: str) -> bool:
    """Find b in a."""
    assert len(b) == 1
    same: bool = False
    check: int = 0
    while same is not True and check < len(a): 
        if b == a[check]:
            same = True
            return(same)
        else:
            check += 1
    return(same)


def emojified(c: str, d: str) -> str:
    """Emojified the result of find c in d."""
    assert len(c) == len(d)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    x: int = 0
    while x < len(d):
        if d[x] == c[x]:
            emoji += GREEN_BOX
        elif contains_char(d, c[x]):
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        x += 1
    return(emoji)


def input_guess(e: int) -> str:
    """Make sure the length of the word is correct."""
    guess: str = input(f"Enter a {e} character word: ")
    while len(guess) != e:
        guess = input(f"That wasn't {e} chars! Try again:  ")
    else: 
        return(guess)


def main() -> None:
    """The entrypoint of the program and main game loop."""
    y: int = 1
    Check: bool = False
    guess: str = ""
    while y <= 6 and Check is False:
        print(f"=== Turn {y}/6 ===")
        guess = input_guess(len(secret))
        if guess != secret:    
            print(emojified(guess, secret))
            y += 1 
            if y == 7:
                print("X/6 - Sorry, try again tomorrow!")     
        elif guess == secret: 
            print(emojified(guess, secret))
            print(f"You won in {y}/6 turns!")
            Check = True


if __name__ == "__main__":
    main()