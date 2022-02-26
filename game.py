import random


class RockPaperScissors:
    options = ["rock", "paper", "scissors"]
    commands = {'exit': "!exit", 'rating': "!rating", 'option': options}
    point = {'win': 100, 'draw': 50, 'lose': 0}
    rating = 0
    filename = "rating.txt"

    def __init__(self):
        self.player1, self.player2, self.saved_rating = None, None, None

    def read_inputs(self):
        self.player1 = input()
        self.player2 = random.choice(self.commands['option'])

    def score(self):
        win_lose = self.options[self.options.index(self.player1) + 1:] + self.options[:self.options.index(self.player1)]

        if self.player2 not in win_lose:
            result = "draw"
        elif win_lose.index(self.player2) < len(win_lose) / 2:
            result = "lose"
        else:
            result = "win"

        outputs = {'win': "Well done. The computer chose {} and failed".format(self.player2),
                   'draw': "There is a draw ({})".format(self.player2),
                   'lose': "Sorry, but the computer chose {}".format(self.player2)}
        self.rating += self.point[result]
        print(outputs[result])

    def read_rating(self):
        file = open(self.filename, 'r')
        self.saved_rating = file.read().split("\n")
        file.close()
        self.saved_rating = {x.split()[0]: int(x.split()[1]) for x in self.saved_rating[:-1]}

    def player(self):
        name = input("Enter your name: ")
        if name in self.saved_rating:
            self.rating = self.saved_rating[name]
        print("Hello,", name)
        user_input = input()
        if user_input:
            self.options = user_input.split(",")
            self.commands['option'] = self.options
        print("Okay, let's start")

    def play(self):
        self.read_rating()
        self.player()
        while True:
            self.read_inputs()
            if self.player1 == self.commands['exit']:
                print("Bye!")
                break
            elif self.player1 == self.commands['rating']:
                print("Your rating:", self.rating)
            elif self.player1 in self.commands['option']:
                self.score()
            else:
                print("Invalid input")


game = RockPaperScissors()
game.play()
