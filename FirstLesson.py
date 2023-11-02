#print("Hello")
#num = 2+2
#print(num)

import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()

def add_numbers():
    number1 = random.randint(5,25) 
    number2 = random.randint(50, 67)  
    print(number1 + number2) 


if __name__=="__main__":
    add_numbers()
