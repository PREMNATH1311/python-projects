############Basic if\else statement conditions
def height():
    print("Welcome to the rollercoster ride ")
    height=int(input("What is your height? "))
    if height >=180:
        print("you have premit to ride in rollercoster,Enjoy!")
    else:
        print("Your height does't match to our premit level sorry! \nBetter Luck Next Time !")


#odd or even number
def oddeven():
    print("Enter the number to be find out Either Odd/Even")
    num=int(input("Enter the number: "))
    if num %2==0:
        return "Its Even Number"
    else:
        return "Its an Odd Number"

#Check you height and age to determine the price
def rollercoatalcost():
    height=int(input("Enter you height in CM: "))
    if height >120:
        print("Welcome to ride, Can have permit to ride")
        age=int(input("Enter your age? "))
        if age <12:
            bill=50
            print("you should pay 50 Rs to Enjoy your Ride")
        elif age>=12 and age<=18:
            bill=70
            print("You should pay 70Rs to Enjoy your Ride")
        else:
            bill=120
            print("you should pay 120 Rs to Enjoy your Ride")
        want_photo=input("If you want photo yes for 'y' if no press 'N'")
        if want_photo=='y':
            bill+=30
            print(f"your total bill amount is {bill}")
        else:
            print(bill)
    else:
        print("You can't ride, Because You are not in our permit/required height")
#rollercoatalcost()

def BMIcalculator():
    weight=int(input("Enter Your Weight (KGs) ? "))
    height=float(input("Enter your HHeight in (m) ? "))
    output=float(weight/(height*height))
    print(output)
    if output <18.5:
        return "Your are under weight"
    elif output >=18.5 and output <=25:
        return "Normal weight.Good!"
    elif output > 25 and output <=30:
        return "OverWeight dude"
    elif output >30 and output <=35:
        return "Obese"
    else:
        return "You have Clinically Obese"
#print(BMIcalculator())

#######pizzaa ordering from customer

def pizzaordering():
    print("welcome to pizza deleviry created by prem")
    size=input("what size pizza do you want S/M/L? ").upper()
    add_extra=input("Do you want pepporine ? Y/N ! ").upper()
    extra_cheese=input("Do you need Extra Cheese? Y/N ! ").upper()
    if size=="S":
        bill=150
    elif size=="M":
        bill=200
    elif size=="L":
        bill=250
    if add_extra=="Y"and size=="S":
        bill+=20
    elif add_extra=="Y" and size=="M" or size=="L":
        bill+=30
    if extra_cheese=="Y":
        bill+=10
    return f"Total amount {bill}"

# print(pizzaordering())


def Treasureisland():
    print("welcome to Tresure Island ,Enjoy you life with adventure")
    dir=input("Enter the direction to cross the road- which you want to end up with like Right/Left").lower()
    if dir=="left":
        nextdir=input("You come to lake.There is a island in middle of a lake.type 'wait' for wait for boat or type 'swim' to swim by your own? ").lower()
        if nextdir=="wait":
            ddir=input("you arrive at the island unharmed .There is a house with 3 door .One red, one yellow and one blue. which color you want to choose? ").lower()
            if ddir=="yellow":
                print("Good you found the treasure:Good-------------")
            else:
                print("Game over")
        else:
            print("Gameover")
    else:
        print("Gameover")

Treasureisland()
