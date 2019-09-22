#
#
## CMPT 120
## Assignment 1
## By: Vera Yang


import random


########## PART A
## Welcome message
print("======================================= STAGE A =======================================\n")
print("Welcome to COCOMAKER Chocolate Factory!")
print("Our chocolate bonbons are made with top cocoa beans, Madagascan vanilla, and local almonds and peanuts!")
print()


## Ask name
print("Please provide your name")
nameFirst = input("First name: ")
nameLast = input("Last name: ")

print("Thank you ", nameFirst, " !\n\n")


## Asks users if they accept default costs

cost_a = 2
cost_b = 1.5
cost_oval = 5
cost_round = 5.5

print("===> The default costs for the chocolates are:")  
print("Bonbon A (Almond) = $", cost_a, "\nBonbon B (Peanut Butter) = $", cost_b, "\nOval box = $", cost_oval, "\nRound box = $", cost_round)
print("\nDo you agree to use the default costs?")
cost = input("Please type yes/no: ")

user_said = len(cost)

if (user_said == 3):  ## If they accept default costs
    print("===> Great! The default costs will be used.")
    print("\nTRACE** The costs will be:")
    print("TRACE** A:2 B:1.5 Oval:5 Round:5.5")
else:
    print("\n===> Okay, please provide the costs for:")  ## If they DON'T accept default costs
    cost_a = float(input("a Bonbon A (Almond) = $"))
    cost_b = float(input("a Bonbon B (Peanut Butter) = $"))
    cost_oval = float(input("an Oval Box = $"))
    cost_round = float(input("a Round Box = $"))
    print("\nTRACE** The costs will be:")
    print("TRACE** A:" + str(cost_a) + " B:" + str(cost_b) + " Oval:" + str(cost_oval) + " Round:" + str(cost_round))


########## PART B
## Asks users if they want to provide number of boxes
print("\n======================================= STAGE B =======================================")
print("================================ FROM BOXES TO BONBONS ================================\n")
print("Would you like to provide the number of boxes of chocolates you want to produce?")
box = input("Please type yes/no: ")

run_stage_b = len(box)

if (run_stage_b == 3):  ## If they want to provide number of boxes
    print("\n===> Okay, please provide the amount of:")
    desired_oval = int(input("Number of Oval boxes to be produced = "))
    desired_round = int(input("Number of Round boxes to be produced = "))
    
    print("\nTo produce", desired_oval, "Oval box(s), we need to produce",
          desired_oval*11, "Bonbon A and", desired_oval*4, "Bonbon B.")
    print("To produce", desired_round, "Round box(s), we need to produce",
          desired_round*7, "Bonbon A and", desired_round*4, "Bonbon B.")
    print()   
else:
    print("===> Great! We can skip this part.")  ## CASE 1: If they DON'T want to provide number of boxes 


## CASE 2: If they WANT to provide the number of boxes and DON'T accept the default costs
if (run_stage_b == 3 and user_said < 3):
    
    total_cost_oval = desired_oval*11*cost_a + desired_oval*4*cost_b + desired_oval*cost_oval
    total_cost_round = desired_round*7*cost_a + desired_round*4*cost_b + desired_round*cost_round

    print("TRACE** RECALL the costs will be:")
    print("TRACE** A:" + str(cost_a) + " B:" + str(cost_b) + " Oval:" + str(cost_oval) + " Round:" + str(cost_round) + "\n")

    ## Show total costs of Oval and Round
    print("Total cost for the Oval box = $", total_cost_oval)
    print("Total cost for the Round box = $", total_cost_round)
    print("Total cost altogether = $", total_cost_oval + total_cost_round)


## CASE 3: If they WANT to provide the number of boxes and ACCEPT the default costs 
if (run_stage_b == 3 and user_said == 3):

    total_cost_oval = desired_oval*11*cost_a + desired_oval*4*cost_b+ desired_oval*cost_oval
    total_cost_round = desired_round*7*cost_a + desired_round*4*cost_b + desired_round*cost_round

    print("\nTRACE** RECALL the costs will be:")
    print("TRACE** A:2 B:1.5 Oval:5 Round:5.5\n")

    ## Show total costs of Oval and Round
    print("Total cost of Oval box = $", total_cost_oval)
    print("Total cost of Round box = $", total_cost_round)
    print("Total cost altogether = $", total_cost_oval + total_cost_round)


########## PART C
## Asks users how many bonbons they want
print("\n==================================== STAGE C - I ======================================")
print("================================ FROM BONBONS TO BOXES ================================\n")
print("===> How many would you like for each type of bonbon?")
desired_a = int(input("Bonbon A (Almond) = "))
desired_b = int(input("Bonbon B (Peanut Butter) = "))

print("\nTRACE** 1 Oval box can have 11 Bonbon A and 4 Bonbon B")

## Tells users how many oval boxes can be produced
## Recall 1 oval box = 11A + 4B
calc_a_o = desired_a//11
calc_b_o = desired_b//4
print()

if (calc_a_o > calc_b_o):
    print("===> The number of Oval boxes that can be produced is", calc_b_o)
    unused_a_o = desired_a - calc_b_o*11
    unused_b_o = desired_b - calc_b_o*4

else:
    print("===> The number of Oval boxes that can be produced is", calc_a_o)
    unused_a_o = desired_a - calc_a_o*11
    unused_b_o = desired_b - calc_a_o*4
   

print("\nNumber of unused bonbons:")
print("Bonbon A =", unused_a_o, "\nBonbon B =", unused_b_o)


########## BONUS POINTS
## Tells users how many round boxes can be produced
## Recall 1 oval box = 7A + 4B
print("\n================================== STAGE C - II =======================================")
print("=============================== BONUS CALCULATIONS ====================================\n")
print("Do you want to do the bonus calculations?")
bonus = (input("Please type yes/no: "))

run_bonus = len(bonus)

## Tells users how many round boxes can be produced
## Recall 1 oval box = 7A + 4B
if (run_bonus == 3):
    print("\nTRACE** 1 Round box can have 7 Bonbon A and 4 Bonbon B\n")
    calc_a_r = desired_a//7
    calc_b_r = desired_b//4

    if (calc_a_r > calc_b_r):
        print("===> The number of Round boxes that can be produced is", calc_b_r)
        unused_a_r = desired_a - calc_b_r*7
        unused_b_r = desired_b - calc_b_r*4

    else:
        print("===> The number of Round boxes that can be produced is", calc_a_r)
        unused_a_r = desired_a - calc_a_r*7
        unused_b_r = desired_b - calc_a_r*4   

    print("\nNumber of unused bonbons:")
    print("Bonbon A =", unused_a_r, "\nBonbon B =", unused_b_r)
    print("\n")


    ## Calculates which box has minimum loss and is the best option

    ## CASE 1: If the user accepts the default cost, then calculate the loss using default cost
    if (user_said == 3):
        if (unused_a_o*cost_a + unused_b_o*cost_b < unused_a_r*cost_a + unused_b_r*cost_b):  ## If loss of oval < loss of round
            print("You should produce the bonbons in Oval boxes!")
            print("The loss of unused bonbons produced with Oval boxes ($", unused_a_o*cost_a + unused_b_o*cost_b,
                  ") is less than the loss with Round boxes ($", unused_a_r*cost_a + unused_b_r*cost_b, ")")

        elif (unused_a_o*cost_a + unused_b_o*cost_b > unused_a_r*cost_a + unused_b_r*cost_b): ## If loss of oval > loss of round
            print("You should produce the bonbons in Round boxes!")
            print("The loss of unused bonbons produced with Round boxes ($", unused_a_r*cost_a + unused_b_r*cost_b,
                  ") is less than the loss with Oval boxes ($", unused_a_o*cost_a + unused_b_o*cost_b, ")")

        else:
            print("You can produced with either Oval boxes or Round boxes!") ## If loss of oval = loss of round
            print("The loss of unused bonbons produced with Round boxes ($", unused_a_r*cost_a + unused_b_r*cost_b,
                  ") is the same as the loss with Oval boxes ($", unused_a_o*cost_a + unused_b_o*cost_b, ")")

    ## CASE 2: If the user provides cost, then calculate the loss using the cost provided
    if (user_said < 3):
        if (unused_a_o*cost_a + unused_b_o*cost_b < unused_a_r*cost_a + unused_b_r*cost_b): ## If loss of oval < loss of round
            print("You should produce the bonbons in Oval boxes!")
            print("The loss of unused bonbons produced with Oval boxes ($", unused_a_o*cost_a + unused_b_o*cost_b,
                  ") is less than the loss with Round boxes ($", unused_a_r*cost_a + unused_b_r*cost_b, ")")
            
        elif (unused_a_o*cost_a + unused_b_o*cost_b > unused_a_r*cost_a + unused_b_r*cost_b): ## If loss of oval > loss of round
            print("You should produce the bonbons in Round boxes!")
            print("The loss of unused bonbons produced with Round boxes ($", unused_a_r*cost_a + unused_b_r*cost_b,
                  ") is less than the loss with Oval boxes ($", unused_a_o*cost_a + unused_b_o*cost_b, ")")

        else:
            print("You can produced with either Oval boxes or Round boxes!") ## If loss of oval = loss of round
            print("The loss of unused bonbons produced with Round boxes ($", unused_a_r*cost_a + unused_b_r*cost_b, 
                  ") is the same as the loss with Oval boxes ($", unused_a_o*cost_a + unused_b_o*cost_b, ")")

else:
    print("===> Great! We can skip the bonus calculations.")



########## SECRET CODE
print("\n===================================== STAGE D =========================================")
print("=================================== SECRET CODE =======================================\n")

## 1
s1 = nameFirst[0].lower() + nameLast[-1].upper()

trace_secret = "TRACE** RECALL the number of Oval boxes that can be produced is"

print("\nTRACE** RECALL the name is " + nameFirst + " " + nameLast)

## 2-11

## If using default cost
if (user_said == 3):
    print("TRACE** RECALL the costs will be:")
    print("TRACE** A:2 B:1.5 Oval:5 Round:5.5")

    if (calc_a_o > calc_b_o):
        print(trace_secret, calc_b_o, "\n")
        s2 = s1 + "**A2**B1.5**" + str(calc_b_o) + "**" + str(random.randint(0, int(calc_b_o))) + "**"
        s2_count = len(s2)
        if (s2_count%2 == 0):
            print(s2 + "Even")
        else:
            print(s2 + "Odd")

    elif (calc_a_o < calc_b_o):
        print(trace_secret, calc_a_o, "\n")
        s3 = s1 + "**A2**B1.5**" + str(calc_a_o) + "**" + str(random.randint(0, int(calc_a_o))) + "**"
        s3_count = len(s3)
        if (s3_count%2 == 0):
            print(s3 + "Even")
        else:
            print(s3 + "Odd")

    else:
        print(trace_secret, calc_a_o, "\n")
        s4 = s1 + "**A2**B1.5**" + str(calc_b_o) + "**" + str(random.randint(0, int(calc_b_o))) + "**"
        s4_count = len(s4)
        if (s4_count%2 == 0):
            print(s4 + "Even")
        else:
            print(s4 + "Odd")
            
## If using provided cost
else:
    print("TRACE** RECALL the costs will be:")
    print("TRACE** A:" + str(cost_a) + " B:" + str(cost_b) + " Oval:" + str(cost_oval) + " Round:" + str(cost_round))

    if (calc_a_o > calc_b_o):
        print(trace_secret, calc_b_o, "\n")
        s5 = s1 + "**A" + str(cost_a) + "**B" + str(cost_b) + "**" + str(calc_b_o) + "**" + str(random.randint(0, int(calc_b_o))) + "**"
        s5_count = len(s5)
        if (s5_count%2 == 0):
            print(s5 + "Even")
        else:
            print(s5 + "Odd")
        
    elif (calc_a_o < calc_b_o):
        print(trace_secret, calc_a_o, "\n")
        s6 = s1 + "**A" + str(cost_a) + "**B" + str(cost_b) + "**" + str(calc_a_o) + "**" + str(random.randint(0, int(calc_a_o))) + "**"
        s6_count = len(s6)
        if (s6_count%2 == 0):
            print(s6 + "Even")
        else:
            print(s6 + "Odd")

    else:
        print(trace_secret, calc_a_o, "\n")
        s7 = s1 + "**A" + str(cost_a) + "**B" + str(cost_b) + "**" + str(calc_b_o) + "**" + str(random.randint(0, int(calc_b_o))) + "**"
        s7_count = len(s7)
        if (s7_count%2 == 0):
            print(s7 + "Even")
        else:
            print(s7 + "Odd")

    

########## END OF PROGRAM
print("\n================================ END OF THE PROGRAM! ==================================")

