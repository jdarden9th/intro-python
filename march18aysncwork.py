# Async work Monday March 18th, 2024.

#1. Create a function that will count the number of characters in a string
# that is passed in by a user. The string value can be passed in either as 
# a paramter or by using the input function.
def count_characters(input_string):
     if len(input_string)
     user_input=input("enter a string")
     print("number of characters",count characters(user_input)) 
# You must be write down and explain how your program 
# works in complete sentences in order to get full credit. 

# 2. Use your notes, W3schools, and what we have learned in class to develop
# a simple rock, paper, scissors game. Your game should allow the user to enter a letter
# that will represent the values rock, paper, and scissors (ex. r = rock, p = paper, s= scissors).
 def winner(Computer_Move,Player_Move):
    if Computer_Move == Player_Move:
        print('Tie')
    elif Player_Move == 'Rock' and Computer_Move == 'paper':
        winner = 'computer'
    elif Player_Move == 'paper' and Computer_Move == 'Scissor':
        winner = 'Computer'
    elif Player_Move == 'Scissor' and Computer_Move == 'Rock':
        winner = 'Computer'
    elif Player_Move == 'paper' and Computer_Move == 'Rock':
        winner = 'Player'
    else:
        print('Computer Win.')
winner('paper','Rock')
