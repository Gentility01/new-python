correct_number = 6

def good():
    guess = int(input(' enter a number  from 1 to 9 to guess'))
    try:
        if guess == correct_number:
            print('correct')
        elif guess < 1 or guess > 9:
            print("ou are suppose to enter only from 1 - 9")

        
        print('wrong guess')
    except:
        
        good()
    

    
good()  

    
    
    
