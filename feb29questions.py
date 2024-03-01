#the statement checks a codition. if the condition evulates to true the code block inside the if statment is executed. if the condition is false the code bnlock is skipped
#if condition: #code block to execute if condtiton is true 
#the else statement is used to conjiunction with the if statment. it provides an altrernative code block to execute when the condition in the if statment is False
#else: #code block execute of condition is false
#in addition to if and else python also provides the else if statment to check multiple conditions sequentially. it follows an if statment and precedes an optional else statment if the condition in the elif statment is true the corresponding code block is executed and the subsequent elif or else statments are skipped

 





#question 2
def check_highscore():
    
    userscore= int(input("enter your game score"))
    if userscore > 3000:
        print('congratulations! you achived the high score!')
    else:
        print("sorry you have not reached the high score. keep playing")

check_highscore()