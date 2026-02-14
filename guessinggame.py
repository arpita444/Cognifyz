import random
actual_num = random.randint(1, 100)
print("Let me think of a number between 1 and 100.")
while True:
    guessed_num = int(input("Enter your guess: "))
    if guessed_num < actual_num:
        print("Too low!")
    elif guessed_num > actual_num:
        print("Too high!")
    else:
        print("You got it! You win!")
        break
    