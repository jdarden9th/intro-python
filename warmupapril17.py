# a python is used to repeat a specific code for a known number of times a while loop is when we would want to ask for a number between 1 through 10

numbers = [5,10,15,20,25]
for num in numbers: result = num * 3


def guessing_game():
    randomNumber = random_number = (1,10)
    print("random number value is: ", randomNumber)
    while true:
        guess = int(input("guess a number between 1 and 10"))
        if guess == randomNumber:
            print("congratulations! you guessed the number correctly")
            break
        else:
            print("wrong guess. try again")
            continue
        guessing_game