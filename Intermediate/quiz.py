import time

class astronomy:
    
    ans_list = []
    ques_dict = {
        1: ['What is the nearest star outside the solar system?', 'alpha centauri'],
        2: ['What is the largest planet in the solar system?', 'jupiter'],
        3: ['What is the name of our galaxy?', 'milky way'],
        4: ['Which planet is known as the "Red Planet?', 'mars'],
        5: ['What is a shooting star technically called?', 'meteor'],
        6: ['What is the name of the brightest star in the night sky?', 'sirius'],
        7: ['What force keeps planets in orbit around the Sun?', 'gravity'],
        8: ['What is the largest moon in our solar system?', 'ganymede'],
        9: ['What is the hottest planet in our solar system?', 'venus'],
        10: ['What is the name of the spacecraft that visited Pluto in 2015?', 'new horizons']
        }
    def start_quiz(self):
        score = 0

        for i in range(1,len(astronomy.ques_dict)+1):
            q = (self.ques_dict[i])[0]
            print(f'Question {i}: {q}')
            ians = input("Answer: ").lower()
            self.ans_list.append(ians)
            print()
            
        for i in range(0,10):
            if self.ans_list[i] == (self.ques_dict[i+1])[1]:
                score+=1

        percent = (score/10)*100
        print(f'Score = {score}')
        print(f'Percentage = {percent}')

        if percent > 39:
            print("You Passed the Test")
        else:
            print("You failed the test")



#for running
quiz = astronomy()
quiz.start_quiz()
            
            
                  
            
            

        

            

        
        
