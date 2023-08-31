import random
def generator():
    print("Welcome to Number Guessing Game")
    print("Enter the range where you want me to guess")
    low=int(input("Enter a lower value of the range:-"))
    high=int(input("Enter the higher value of the range:-"))
    number=random.randint(low,high)
    guess=None
    attempt=0
    while guess!=number:
        try:
            guess=int(input("Guess the number :- "))
            attempt+=1
            if number>guess:
                print("Higher")
            elif number<guess:
                print("Lower")
        except ValueError:
            print("Enter a valid number:- ")
    print(f"Congratulations! You've guessed the number {number} in {attempt} attempts.")
if __name__=="__main__":
    generator()
