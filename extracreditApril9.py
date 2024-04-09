# Prompt #1. 
#Create a function that will count the number of characters in a string
# that is passed in by a user. The string value can be passed in either as 
# a paramter or by using the input function.
def count_chars(string):
    len(string)

# Prompt #2.
# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# user must be atleast 5.2 or taller and atleast 14 years old or older 
# in order to ride roller coaster 1. 

# if the user is shorter than 5.2 but at least 14 years of age or older,
# they can ride the roller coaster 2.

# if the user is shorter than 5.2 and also younger than 14 years of age,
# they can ride roller coaster 3. 

# if the user enters information incorrectly, give them an error message
# and tell them that they entered their information incorrectly. 

def rollar_coaster_access(height,age):
    if height >= 5.2 and age >= 14:
        rollar_coaster = 1
    elif height < 5.2 and age >= 14: 
        rollar_coaster = 3
    else:
        print("error you enterd your information inccorectly.")
        return
    return rollar_coaster 
# Prompt # 3.
# You have been hired as an engineer to develop a checkout scanner system.
# when a user puts in a name of an item and the price of the item it gets added to their cart.
# your function to loop/ repeat and ask the user if they are done shopping or would like to continue
# if the enter 'y' for yes, continue the loop and allow the user to put in another
# item name and item price. If they enter 'n' for no, calculate the total price of items as
# well as print the all the item names.
def checkout_scanner(): items = []
total_price = 0 
while true:
    item_name = input ("enter the name of the item:")
    item_price = float(input("enter the price of the item:"))
    items.append({"name": item_name, "price": item_price})
    total_price += item_price
    print("Do you want to countinue shopping?(enter 'y' for yes or 'n' for no):")
    choice == input()
    if choice =='y':
        continue
    elif choice == 'n':
        break
    if not choice:
        print("you have not entered avalid choice.please enter 'y' for yes or 'n' for no.")
        continue
    print("the total price of the items is:", total_price)
    
    print("the items you have purchased are:")
    for item in items:
        print(item['name'], item['price'])
        checkout_scanner





# bonus for prompt # 3.
# create a discount system where, when the user enters 'y' for being done shopping,
# ask the user if they have a discount code. Depending on the code they enter they will
# recieve 10%, 25%, or 50% off of their total purchase. 


#ask the user if they have a discount code have_code = input("do you have a discount code?")
#if the user has a code, ask them to enter it

    code = input("enter your discount code:")
    if code == "10":
        discount_percentage = 0.10
    elif code == "25":
        discount_percentage = 0.25
    elif code == "50":
        discount_percentage = 0.50
    else:
        discount_percentage = 0.00
 