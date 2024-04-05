correct_passcode = "your correct_passcode"
while passcode != correct_passcode:
    passcode = input("please enter the passcode")
    if passcode == correct_passcode:
        print("you have entered the correct passcode. you can now view the website")
    else:
        print("the passcode you entered is incorrect.please try again")