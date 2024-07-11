t = 'sri kanth'
gl = [(char, False) for char in t if char != ' ']

def print_char():
    global gl,t
    for ch in t:
        if ch == ' ':
            print(' ', end = ' ')
        else:
            for c,b in gl:
                if c == ch and b:
                    print(c, end = ' ')
            else:
                print('_', end = ' ')
    print()
            
print("Guess the word ")
ch = 5

while ch!=0:
    char = input("Enter a letter: ").lower()
    if char in t:
        print('Correct Guess.')
        gl = [(c,True) if c == char else (c,b) for c,b in gl]
        print_char()
        
        if all (b for c,b in gl):
            print("Congrats. Guessed the Word")
            break
    else:
        ch-=1
        print(f"Wrong guess. You have {ch} chances left.")
        print_char()
else:
    print("Sorry, you've run out of chances. The word was:", t)


        
