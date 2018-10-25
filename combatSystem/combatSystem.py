#Eric Wright
#10/18
#combatSystem
import random
   
win = 0
mHealth = 100
pHealth = 100

choice = input("attack or run ")

if choice != "attack" or choice != "run":
    print("i'm not sure what that is")
    choice = input("attack or run ")
    
while choice == "attack":
    pDamage = random.randrange(0, 25)
    mDamage = random.randrange(0, 50)
    print("you attack the monster for", pDamage, "health")
    mHealth -= pDamage
    if mHealth > 0:
        pHealth -= mDamage
        print("the monster attacks you for", mDamage, "health")
    if pHealth <= 0:
        win = 0
        print("you died")
        break
    elif mHealth <= 0:
        win = 1
        print("you have killed the monster")
        break
    elif pHealth >= 0 and mHealth >= 0:
        print("you have", pHealth, "health")
        print("the monster has", mHealth, "health")
        choice = input("attack or run ")
    if choice == "run":
        win = 0
        print("you are a coward")
    # if choice != "attack" or choice != "run":
    #     print("i'm not sure what that is")
    #     choice = input("attack or run ")
    if win == 0:
        input("Game Over")
    elif win == 1:
        input("You Won")
    else:
        continue
            
input("\npress enter to exit")
    

        