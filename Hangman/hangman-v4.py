import mysql.connector
import random

class hangman:
    def __init__(self):
        self.db_connection = mysql.connector.connect(
            host = "localhost",
            user = "srik",
            password = "srik1201",
            database = "hangman"
        )
                
        self.word = self.get_random_word()
        self.guess_list = [(char.lower(),False) for char in self.word]
        self.chances = 10
        self.check_list = []

    def get_random_word(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT words FROM places ORDER BY RAND() LIMIT 1")
        result = cursor.fetchone()
        cursor.close()

        if result:
            return result[0]
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

    def __del__(self):
        if self.db_connection.is_connected():
            self.db_connection.close()

game = hangman()
game.play_game()







            
