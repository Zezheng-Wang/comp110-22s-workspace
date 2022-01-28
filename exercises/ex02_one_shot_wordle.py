"""Wordle Exercise 02."""

__author__ = "730427941"

secret = str("python")

guess = str(input(f"what is your {len(secret)}-character guess?"))


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

emoji: str = ""
x: int = 0
same: bool = False 
check: int = 0

while len(guess) != len(secret):
    guess = str(input(f"That was not {len(secret)} letters! Try again: "))
else:
    if len(guess) == len(secret) and guess == secret:
        print(GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX + GREEN_BOX)
        print("Woo! You got it!")
        exit()
    elif len(guess) == len(secret) and guess != secret:
        while x < len(secret):
            if guess[x] == secret[x]:
                emoji += GREEN_BOX      
            
            else:
                while same is not True and check < len(secret): 
                    if guess[x] == secret[check]:
                        same = True
                    else:
                        check += 1    
                if same:
                    emoji += YELLOW_BOX
                    
                else:
                    emoji += WHITE_BOX  
                check = 0     
                same = False   
            x += 1 
        print(emoji)
        print("Not quite! Play again soon!")
        exit()

   