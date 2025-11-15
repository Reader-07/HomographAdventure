# Probably a really bad way to do this but it is what I know.
import random
        
# Introduction
print("\033c")
print("Welcome to Team Engine's Perplexing Game!")
print("Be sure to question all words!")
print("_"*40+"\n")
input("Press Enter to continue")


# Initial Field wakeup
print ("\033c")
print("You wake up in a field. You are unsure of how you got here or what exactly you are doing.")
print("As you look around, you see a large bank across a river with a bridge.")
print("On your other side, there is also a crane reaching high into the sky.")
print("_"*40)
print("1. Head to the bank.")
print("2. Head to the crane.")
# Choice
while True:
    choice = input("What will you do? (1 or 2): ")
    if choice == "1" or choice == "2":
        break
    else:
        print("Please choose either '1' or '2'.")
random = random.randint(1,2)
if choice == "1": # Bank
    print("\033c")
    if random == 1: # A river bank
        print("You approach the bank.")
        print("Now that you are closer, you can tell for sure that this river bank is large.")
        print("Being closer also reveals a faint shimmer in the water")
        print("_"*40+"\n")
        
        
        
    if random == 2: # A real bank building
        print("The bank seems to be a Respectable Bank.")
        print("Unfortunately, you can't find any money in your pockets.")
        print("_"*40+"\n")
        
        
        
if choice == "2": # Crane
    print("\033c")
    if random == 1: # Machine crane
        print("Approching this piece of machinery, it doesn't seem to have anyone in it.")
        print("Curiously though, the crane is still moving on its four wheels.")
        print("_"*40+"\n")
        print("1. Investigate the crane.")
        print("2. Let the crane pass undisturbed.")
        # Choice
        while True:
            choice = input("What will you do? (1 or 2): ")
            if choice == "1" or choice == "2":
                break
            else:
                print("Please choose either '1' or '2'.")
        random = random.randint(1,2)
        if choice == 1: # Investigate the crane
            print("\033c")
            print("As you get closer to the crane to investigate it, it also seems to notice you.")
            random = random.randint(1,2)
            if random == 1: # Friendly crane
                print("_"*40+"\n")
                
                
                
                
            if random == 2: # Aggresive crane
                print("_"*40+"\n")
                
                
                
                
        if choice == 2: # Let the crane pass
            print ("\033c")
            print("The crane continues on its journey alone.")
            print("Following it with your eyes, you sense a feeling of loneliness.")
            print("_"*40+"\n")
                
        
        
        
        
    if random == 2: # Bird crane
        print("The crane's wing is stretched as far as it can up into the sky.")
        if random == 1: # Talking crane
            print("_"*40+"\n") #Watch Wind Wind Watch
        if random == 2: # Flying crane
            print("_"*40+"\n") # Fly on a fly.
