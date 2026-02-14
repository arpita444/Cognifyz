import random
starting_num = int(input("Enter the starting number of the range: "))
ending_num = int(input("Enter the ending number of the range: "))
actual_num = random.randint(starting_num, ending_num)
print("Let me think of a number between ", starting_num, "and", ending_num, ".")
while True:
    guessed_num = int(input("Enter your guess: "))
    if guessed_num < actual_num:
        print("Too low!")
    elif guessed_num > actual_num:
        print("Too high!")
    else:
        print("You got it! You win!")
        break