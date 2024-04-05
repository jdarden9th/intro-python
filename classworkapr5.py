i = 0 #iterator= starting point for our loop
# keyword, all while means is: 
# 'so long as this condition is true'.
while i == 0:
    print('welcome to python') #print this on a loop 3x
    print('this is step 1')
    print('this is step 2')
    print('this is step 3')
    print('now python is going to add 1 to i')






correct_passcode = "your correct_passcode"
while passcode != correct_passcode:
    passcode = input("please enter the passcode")
    if passcode == correct_passcode:
        print("you have entered the correct passcode. you can now view the website")
    else:
        print("the passcode you entered is incorrect.please try again")