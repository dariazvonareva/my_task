import numpy as np

number = np.random.randint(1, 101) #makes a number

count = 0 #number of attempts
mim = 1
max = 100
while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    if predict_number > number:
        print("The number must be less!")
    elif predict_number < number:
        print("The number must be greater!")
    else:
        print(f" You guessed the number! This number is {number} in {count} attempts")
        break # The game is over. Exit from the loop
