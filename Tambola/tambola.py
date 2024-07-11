import random

class ticket:

    def __init__(self):
        self.t = {i : [0 for j in range(9)] for i in range(3)}
        self.generate()

    def generate(self):
        nums = set()
        set.add(i for i in range(1,91))
            
        while len(self.num)!=15:
            for i in range(15 - len(self.num)):
                self.num.add(random.randint(1,90))
                self.ind.add(random.randint(0,26))
                
        n = list(self.num)
        i = list(self.ind)
        n.sort()
        i.sort()

        c = 0
        for x in i:
            ticket.c=0
            self.t[x] = n[c]
            ticket.c+=1
        self.print_ticket()
        
    def print_ticket(self):
        for i in range(0,3):
            for j in range(9*i, 9*(i+1)):
                print(self.t[j], end = ' ')
            print()
    
        

t = ticket()

        
            
            
