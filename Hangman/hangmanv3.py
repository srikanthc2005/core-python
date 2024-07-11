class hangman:
    def __init__(self, word):
        self.word = word
        self.guess_list = [(char,False) for char in word]
        self.chances = 10
        self.check_list = []

    def reveal_word(self):
        for ch,b in self.guess_list:
            if ch == ' ':
                print(' ', end = ' ')
            elif b:
                print(ch, end = ' ')
            else:
                print('_', end = ' ')                        
        print()

    def guess(self, ch):
        if ch in self.check_list:
            print('Letter has already been tried.')
            print()
            self.reveal_word()
            return False
        
        self.check_list.append(ch)
        
        if ch in self.word:
            print('Correct Guess!')
            print()
            self.guess_list = [(c,True) if c == ch else (c,b) for c,b in self.guess_list]
            self.reveal_word()

            if all(b for c ,b in self.guess_list if c!= ' '):
                print("Congrats. You have guessed the Word")
                return True
        else:
            self.chances-=1
            print(f'Wrong guess. You have {self.chances} turns left.')
            print()
            self.reveal_word()
            return False

    def play_game(self):
        print("Guess the word ")
        self.reveal_word()

        count = sum(1 for ch in self.word if ch.isalpha())
        print(f'{count} letters.')
        print()
        while self.chances > 0:
            ch = input("Enter a letter: ").lower()
            
            if not ch.isalpha() or len(ch) != 1:
                print('Please enter an Alphabet')
                print()
                self.reveal_word()
                continue
            
            if self.guess(ch):
                break
        else:
            print("Sorry, you've run out of chances. The word was:", self.word)

word = 'zimbambwe'
game = hangman(word)
game.play_game()







            
