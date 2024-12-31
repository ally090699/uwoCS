# Developed by: Allison So
# Date: January 31, 2023
# Desc: Program to determine meals and total cost of a dinner party
# Inputs: Invitee information
# Output: Bill total for dinner party

# Defining variables
NUMBER_INVITEES = (int(input("Please enter the number of invitees:")))

inviteeNumber = range(1, NUMBER_INVITEES + 1)
countFalafel = 0
countPizza = 0
countPasta = 0
countSteak = 0
countBevy = 0

# Determining invitees dietary restrictions
y = 0
while y <= (NUMBER_INVITEES-1):
    print("Please enter the order details for invitee Number", inviteeNumber[y], "/", NUMBER_INVITEES)
    keto = input("Do you want a keto friendly meal?")
    vegan = input("Do you want a vegan meal?")
    gf = input("Do you want a Gluten-free meal?")
    if (keto == "y" or "yes") and (vegan == "y" or "yes") and (gf == "y" or "yes"):
        countFalafel += 1
        y += 1
    elif (keto == "y" or "yes") and (vegan == "y" or "yes") and (gf == "n" or "nothing" or "no"):
        countPizza += 1
        y += 1
    elif (keto == "n" or "nothing" or "no") and (vegan == "y" or "yes") and (gf == "n" or "nothing" or "no"):
        countPasta += 1
        y += 1
    elif (keto == "y" or "yes") and (vegan == "n" or "nothing" or "no") and (gf == "y" or "yes"):
        countSteak += 1
        y += 1
    else:
        countBevy += 1
        y += 1
    print("-" * 10)

# Order Details
tip = int((input("How much do you want to tip your server (% percent)?")))
COST_PIZZA = 44.50
COST_PASTA = 48.99
COST_FALAFEL = 52.99
COST_STEAK = 49.60
COST_BEVY = 5.99
totalPizza = round(countPizza * COST_PIZZA, 2)
totalPasta = round(countPasta * COST_PASTA, 2)
totalFalafel = round(countFalafel * COST_FALAFEL, 2)
totalSteak = round(countSteak * COST_STEAK, 2)
totalBevy = round(countBevy * COST_BEVY, 2)
print("You have %d invitees with the following orders:" % NUMBER_INVITEES)
print("%d invitees ordered Pizza. The cost is: $%.2f." % (countPizza, totalPizza))
print("%d invitees ordered Pasta. The cost is: $%.2f." % (countPasta, totalPasta))
print("%d invitees ordered Falafel. The cost is: $%.2f." % (countFalafel, totalFalafel))
print("%d invitees ordered Steak. The cost is: $%.2f." % (countSteak, totalSteak))
print("%d invitees ordered only Beverage. The cost is: $%.2f." % (countBevy, totalBevy))

# Bill
totalCost = totalPizza + totalPasta + totalFalafel + totalSteak + totalBevy
totalAFTax = round(totalCost*1.13, 2)
totalAFTaxTip = int(round(totalAFTax*((100+tip)/100), 0))
print("The total cost before tax is $%.2f." % totalCost)
print("The total cost after tax is $%.2f." % totalAFTax)
print("The total cost after %d%% tip is $%d." % (tip, totalAFTaxTip))
