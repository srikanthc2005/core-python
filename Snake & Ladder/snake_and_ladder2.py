from random import randint
import time
import snobjects

class dice:
    def __init__(self):
        self.top = 0

    def roll(self):
        self.top = randint(1, 6)
        return self.top

class player:
    def __init__(self, name):
        self.name = name
        self.pos = 0

    def move(self, step):
        self.pos += step
        if self.pos>100:
            self.pos -= step
        return self.pos

class game(snobjects.Game):
    def __init__(self):
        super().__init__()
        self.players = []

    def check_encounter(self, player):
        for snake in self.snakes:
            if player.pos == snake.head:
                print(f"Oops! You encountered a snake, you slide to {snake.tail}")
                player.pos = snake.tail
        for ladder in self.ladders:
            if player.pos == ladder.foot:
                print(f"You got a ladder! You climb to {ladder.top}")
                player.pos = ladder.top
        
    def play_game(self):
        num = int(input("Enter number of players(2-6): "))

        while(num<2 or num>6):
            num = int(input("Invalid Number! Enter number of players(2-6): "))

        self.players = [player(input(f"Enter name for P{i}: ")) for i in range(num)]

        d = dice()
        end = False

        while not end:
            for person in self.players:
                input(f"{person.name}'s Turn: ")
                while True:
                    roll = d.roll()
                    print(f'You rolled {roll}')
                    person.move(roll)
                    print(f"{person.name} is at {person.pos}")
                    self.check_encounter(person)
                    print()

                    if person.pos == 100:
                        print(f"{person.name} is the winner!")
                        end = True
                        break

                    if roll != 6:
                        break

                    time.sleep(1)

                if end:
                    break


game = game()

game.add_snake(99,24)
game.add_snake(41,20)
game.add_snake(82,61)
game.add_snake(59,37)
game.add_snake(67,50)
game.add_snake(31,14)
game.add_snake(92,76)
game.add_snake(7,4)

game.add_ladder(2, 23)
game.add_ladder(39, 80)
game.add_ladder(70, 89)
game.add_ladder(75, 96)
game.add_ladder(17, 93)
game.add_ladder(29, 54)
game.add_ladder(32, 51)
game.add_ladder(8, 12)

game.play_game()

