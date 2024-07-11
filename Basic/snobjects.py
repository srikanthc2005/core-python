class snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

class ladder:
    def __init__(self, foot, top):
        self.top = top
        self.foot = foot


class Game:
    def __init__(self):
        self.snakes = []
        self.ladders = []
    def add_snake(self, head, tail):
        self.snakes.append(snake(head, tail))
        print("Snake Added")

    def add_ladder(self, foot, top):
        self.ladders.append(ladder(foot, top))
        print("Ladder Added")
    def print_ob(self):
        print("Ladders: ", [(ladder.foot, ladder.top) for ladder in self.ladders])
        print("Snakes: ", [(snake.head, snake.tail) for snake in self.snakes])

        


        
        
        


        
