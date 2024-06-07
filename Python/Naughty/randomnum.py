import random

def game():
    number_to_guess = random.randint(1, 100)
    guess = None
    while guess != number_to_guess:
        guess = int(input("Hãy đoán một số từ 1 đến 100: "))
        if guess < number_to_guess:
            print("Số bạn đoán quá thấp!")
        elif guess > number_to_guess:
            print("Số bạn đoán quá cao!")
    print("Chúc mừng! Bạn đã đoán đúng số!")

game()