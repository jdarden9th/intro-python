# Midterm quiz. 
# Create a new python document called midtermquiz.py
# Complete the following questions.
# Once you have comepleted your quiz, commit and sync your work to your GitHub. 

#RULES
# This quiz is open book; you may use your notes, google (only if you are viewing arcticles about python), W3schools only. Any other website
# is prohibitied.
# No phones are allowed during the quiz. refusal to put away a phone will result in failure.
# There is no talking during the quiz. If you complete the quiz, notify the instructor that you
# have finished. Once that is done, you are free to use your device and browse the web quitely. 

# Good Luck

# 1. In your own words, describe what the difference
# between a function arguement and a function parameter.
# Write your response using complete sentences.
#awnser:a function arguement is where you setting an arguement for whatever your trying to code but it has to be a argument the computer can understand a parameter argument is a argument where your trying to make your code run so the way you can run it is by setting one.
# 2. In your own words, describe what each of the following errors means.
# Write your response using complete sentences.

# syntax error: where the computer is not understanding your launguge or your missing something
# type error it happens when you use the wrong data type
# name errorit happenes when the program uses a varible that has not been defined

# 3. What function would I use if I wanted to convert an integer data type into 
# a string data type? i would be writing out a response instead of a number

# 4. What function would I use if I wanted to change a float data type into a 
# an integer data type? you  would take away the decimal from the float so if i have x = 30.5 i would change it to just x = 30

# 5. Describe three (3) Variable naming rules. Write your response in complete sentences. 
#casting: x = int(3)
#type():print(type(x))
#double quotes: x = "john"
# 6. Name the operator family each of these symbols are a part of 
# and describe how each of these sybmols are used. Write your response
# useing complete sentences. 

#symbols
# = equal
# == equal
# =! not equal

# 7. You have been hired as an engineer to develop a car speed detection system.
# the car company would like to create a function where if the user goes over a certain
# speed it will notify them to change gears. The client has provided you with the following
# guidelines on how they would like the gear system to work:
# if the driver is going over 20mph, alert the driver to shift to gear 1
# if the the driver is going over 30mph, alert the driver to shift to gear 2
# if the driver is going over 40mph, alert the driver to shift to gear 3
# if the driver is going over 70mph, alert the driver to shift back to gear 1.
# the client would like you to pass in the speed that the user is going as an argument. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
def driver(driver_switchgear)
        if driver goes over 20mph == switch to gear 1
        if driver goes over 30mph == switch to gear 2 
        if driver goes over 40mph == switch to gear 3
        if driver goes over 70mph == switch back to gear 1
            print(driver_switchgear)
# 8. You have been hired as an engineer to develop a fitness meal plan program. 
# your function should take in two (2) arguements; the day of the week, and the time of the day.
# depending on the time of the day; either morning or afternoon, the meal plan will change. 
# the client has provided you with the following meal plan information
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
def FitnessmealPlan(DayOfTheWeek, TimeOfTheDay):
    if DayOfTheWeek == 'monday' and TimeOfTheDay == 'morning':
        print('2 eggs and a apple')
    elif DayOfTheWeek == 'monday' and TimeOfTheDay == 'afternoon':
        print('bbg grilled chicken and broccoli')
    elif DayOfTheWeek == 'tuesday' and TimeOfTheDay == 'morning':
        print('oatmeal with strawberries and blueberries')
    elif DayOfTheWeek == 'tuesday' and TimeOfTheDay == 'afternoon':
        print('baked chicken with kale')
    elif DayOfTheWeek == 'wednesday' and TimeOfTheDay == 'morning':
        print('fruit salad')
    elif DayOfTheWeek == 'wednesday' and TimeOfTheDay == 'afternoon':
        print('curry goat with rice and cabbage')
    elif DayOfTheWeek == 'thursday' and TimeOfTheDay == 'morning':
        print('pankcakes and turkey sausage')
    elif DayOfTheWeek == 'thursday' and TimeOfTheDay == 'afternoon':
        print('eggplant pasta')
    elif DayOfTheWeek == 'friday' and TimeOfTheDay == 'morning':
        print('steak and eggs')
    elif DayOfTheWeek == 'friday' and TimeOfTheDay == 'afternoon':
        print('cheeseburger and fries')
    elif DayOfTheWeek == 'saturday' and TimeOfTheDay == 'morning':
        print('oatmeal')
    elif DayOfTheWeek == 'saturday' and TimeOfTheDay == 'afternoon':
        print('baked chicken with string beans')
    elif DayOfTheWeek == 'sunday' and TimeOfTheDay == 'morning':
        print('oatmeal')
    elif DayOfTheWeek == 'sunday' and TimeOfTheDay == 'afternoon':
        print('steak and spinach')
FitnessmealPlan('wednesday', 'afternoon')


# 9. You have been hired as an enineer to develop a school to develop an academic honors system.
# the client would like to check if the user has gotten above an 85% overall grade or has
# has accomplished passing the SAT. The client would like you to pass this information in as
# arguements. If either of these situations are true the student has made the academic honors list
# if only passing the SAT is true, congratulate the user but inform them they did not make the list.
# if they only scored above 85%, congratulate the user but inform them they did not make the list.
# if none of the conditions are met, inform them to continue studying and try again next semester. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
def achive over 85%_ you passed SAT

    studentgrade int(input("if you have gotten above 85% overallgrade you passed SAT"))

    if  student has gotten over 85% == they have accomplished passing the sat
    if  student has gotten below 85% == they have faild sat
    if  usergrade > 85%:
        print('congratulations you have passed the SAT')
    else:
        print("sorry you did not pass the SAT")



# 10. Create a function that will check the temperature outside. If the user enters
# a number above 60 degrees it is warm outside, if the enter a number above 80 degrees it is hot outside.
# if the user enters a number below 50 degrees it is cold outside. and if the tempeature is above 50 degrees,
# tell the user it's not warm but it's also not too cold. 
# Please provide three (3) clues/ keywords and explain why you chose them to get full credit.
        def temerature(temerature_outside)
             
             usertemp= int(input("enter temperature"))
             if the number is above 60 == it is warm outside
             if the number is above 80 == it is hot outside
             if the number is below 50 == it is cold 
             if the number is above 50 == it is not warm but it is also not to cold