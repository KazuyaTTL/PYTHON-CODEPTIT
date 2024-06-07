import random

class PikachuGame:
    def __init__(self):
        self.pikachu_location = random.randint(1, 10)
        self.guesses_left = 3

    def guess(self, location):
        if location == self.pikachu_location:
            print("Chúc mừng! Bạn đã tìm thấy Pikachu!")
            return True
        else:
            self.guesses_left -= 1
            if self.guesses_left > 0:
                print("Xin lỗi, Pikachu không ở đó. Bạn còn {} lượt đoán.".format(self.guesses_left))
            else:
                print("Xin lỗi, bạn đã hết lượt đoán. Pikachu đang ở vị trí {}.".format(self.pikachu_location))
            return False

game = PikachuGame()
while game.guesses_left > 0:
    guess = int(input("Hãy đoán vị trí của Pikachu (từ 1 đến 10): "))
    if game.guess(guess):
        break