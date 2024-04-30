# 3. Create a function that uses a loop over the alphabet and print every 5th letter. 

def print_every_5th_letter():
    for i in range(o,26,5):
        if i & 5 != 0:
            print(chr(i))
print_every_5th_letter()