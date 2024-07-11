import mysql.connector
import random

class hangman:

    chances = 10
    menu_dict = {
            1: 'places',
            2: 'everyday'
        }

    
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host = "localhost",
            user = "srik",
            password = "srik1201",
            database = "hangman"
        )

        self.topic = ''
        self.word = ''
        self.username = ''
        self.guess_list = []
        self.chances = hangman.chances
        self.check_list = []
        self.score = 0
        
    @classmethod     
    def set_chances(cls, chances):
        cls.chances = chances
    @classmethod
    def set_dict(cls,menu_dict):
        cls.menu_dict = menu_dict
    
    def choose_menu(self):
        for n,t in hangman.menu_dict.items():
            print(f'Press {n} for {t}')
        choice = int(input("Choose a Topic: "))
        self.topic = hangman.menu_dict[choice]
        print()

    def get_random_word(self):
        cursor = self.db_connection.cursor()
        cursor.execute(f"SELECT words FROM {self.topic} ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        cursor.close()

        if result:
            self.word = result[0]
            self.guess_list = [(char.lower(),False) for char in self.word]
        else:
            raise ValueError("No words were found.")
    
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
        ch = ch.lower()
        
        if ch in self.check_list:
            print('Letter has already been tried.')
            print()
            self.reveal_word()
            return False
        
        self.check_list.append(ch)
        
        if ch in self.word.lower():
            print('Correct Guess!')
            print()
            self.guess_list = [(c,True) if c == ch else (c,b) for c,b in self.guess_list]
            self.reveal_word()

            if all(b for c ,b in self.guess_list if c!= ' '):
                self.score += self.chances
                print(f"Congrats, {self.username}. You have guessed the Word")
                print(f"Score: {self.score}")
                return True
        else:
            self.chances-=1
            print(f'Wrong guess. You have {self.chances} turns left.')
            print()
            self.reveal_word()
            return False    

    def play_game(self):
        print("Let's Play Hangman!")
        print()
        self.username = input("Enter your name: ")
        self.choose_menu()

        while True:
            self.chances = hangman.chances
            self.check_list = []
            self.get_random_word()
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
                print(f"Score: {self.score}")
                break

    def __del__(self):
        if self.db_connection.is_connected():
            self.db_connection.close()

game = hangman()
game.play_game()







            
