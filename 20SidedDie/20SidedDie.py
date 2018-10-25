import random
min = 1
max = 20

yes = ["yes", "y", "sure", "let's do it", "yep", "true", "yes please"]
no = ["no", "n", "nope", "never", "false", "no thank you"]

roll_again = input("Would you like to roll the dice? ").lower()


while roll_again in yes:
    print ("Rolling the die...")
    print ("You Rolled A....")
    print (random.randint(min, max))
    
    roll_again = input("Would you like to roll the dice? ")
if roll_again in no:
    print("Okay bye")    
