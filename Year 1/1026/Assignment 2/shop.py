# Developed by: Allison So
# Date: February 21, 2023
# Desc: Program to collect orders until checkout
# Inputs: User selections (orders)
# Output: List of individual item totals

def pickItems():
# walks user through their order using print statements and collecting user input
# ultimately returns a list with the prices of each PC a user has purchased (built or pre-built)

## inner list structure: [component ID (string), produce name (string), product price (float)]
# static inventory
    invNtry=[
            [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]],  # SSD
            [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]],  # HDD
            [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]],  # CPU
            [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]],  # Motherboard
            [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]],  # RAM
            [['1', 'MSI GeForce RTX 3060 12GB', 539.99]],  # GP Card
            [['1', 'Corsair RM750', 164.99]],  # PSU
            [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]],  # Case
            [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2', 'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC', 1099.99]]  # Prebuilts
    ]
### NOTE INCOMPATIBILITIES: Intel Core CPU + MSI B550 motherboard, AMD Ryzen CPU + MSI Z490 motherboard
    
# CODE
    print("Welcome to my PC Shop!\n")  # prints greeting!
    
    # declaring variables 
    check=0  # initializes check before loop begins so loop ends once the user checks out
    itemsArr=[]  # initializes an empty list/array (itemsArr) where all item totals (mach1Total and mach2Total) will be stored
    
    # making helper functions for each step
    def mach11_211_1_():
        print("\nFinally, let's pick your graphics card (or X to not get a graphics card).\n%s : %s, $%.2f" %(invNtry[5][0][0],invNtry[5][0][1],invNtry[5][0][2]))
        loop11_211_1_=0
        while loop11_211_1_==0:  # Loop gets graphic card choice (1,X,x), asks until valid answer recieved
            gpcardPickOp=str(input("Choose the number that corresponds with the part you want: "))
            nonlocal mach1Total
            if gpcardPickOp=="1":
                mach1Total+=invNtry[5][0][2]
                loop11_211_1_=-1
            elif gpcardPickOp=="x" or gpcardPickOp=="X":
                mach1Total+=0
                loop11_211_1_=-1
            else:
                loop11_211_1_+=1

    def mach11_211_2():
        print("\nNow let's pick an HDD (optional, but you must have at least one SSD or HDD).\n%s : %s, $%.2f\n%s : %s, $%.2f" %(invNtry[1][0][0],invNtry[1][0][1],invNtry[1][0][2],invNtry[1][1][0],invNtry[1][1][1],invNtry[1][1][2]))
        loop11_211_2=0
        while loop11_211_2!=-1:  # Loop forces user to choose an HDD option, as no SSD was chosen
            hddPickOp=str(input("Choose the number that corresponds with the part you want (or X to not get an HDD): "))
            nonlocal mach1Total
            if hddPickOp=="1":
                mach1Total+=invNtry[1][0][2]
                mach11_211_1_()
                loop11_211_2=-1
            elif hddPickOp=="2":
                mach1Total+=invNtry[1][1][2]
                mach11_211_1_()
                loop11_211_2=-1
            else:
                loop11_211_2+=1
    
    def mach11_211_1():
        print("\nNow let's pick an HDD (optional, but you must have at least one SSD or HDD).\n%s : %s, $%.2f\n%s : %s, $%.2f" %(invNtry[1][0][0],invNtry[1][0][1],invNtry[1][0][2],invNtry[1][1][0],invNtry[1][1][1],invNtry[1][1][2]))
        loop11_211_1=0
        while loop11_211_1!=-1:  # Loop gets HDD choice (1,2,X,x), asks until valid answer recieved
            hddPickOp=str(input("Choose the number that corresponds with the part you want (or X to not get an HDD): "))
            nonlocal mach1Total
            if hddPickOp=="1":
                mach1Total+=invNtry[1][0][2]
                mach11_211_1_()
                loop11_211_1=-1
            elif hddPickOp=="2":
                mach1Total+=invNtry[1][1][2]
                mach11_211_1_()
                loop11_211_1=-1
            elif hddPickOp=="X" or hddPickOp=="x":
                mach1Total+=0
                mach11_211_1_()
                loop11_211_1=-1
            else:
                loop11_211_1+=1

    def mach11_211_():    
        print("\nNext, let's pick an SSD (optional, but you must have at least one SSD or HDD).\n%s : %s, $%.2f\n%s : %s, $%.2f\n%s : %s, $%.2f" %(invNtry[0][0][0],invNtry[0][0][1],invNtry[0][0][2],invNtry[0][1][0],invNtry[0][1][1],invNtry[0][1][2],invNtry[0][2][0],invNtry[0][2][1],invNtry[0][2][2]))
        loop11_211_=0
        while loop11_211_!=-1:  # Loop gets SSD choice (1,2,3,X,x), asks until valid answer recieved
            ssdPickOp=str(input("Choose the number that corresponds with the part you want (or X to not get an SSD): "))
            nonlocal mach1Total
            if ssdPickOp=="1":
                mach1Total+=invNtry[0][0][2]
                mach11_211_1()
                loop11_211_=-1
            elif ssdPickOp=="2":
                mach1Total+=invNtry[0][1][2]
                mach11_211_1()
                loop11_211_=-1
            elif ssdPickOp=="3":
                mach1Total+=invNtry[0][2][2]
                mach11_211_1()
                loop11_211_=-1
            elif ssdPickOp=="X" or ssdPickOp=="x":
                mach1Total+=0
                mach11_211_2()
                loop11_211_=-1
            else:
                loop11_211_+=1
            
    def mach11_211():    
        print("\nNext, let's pick your case.\n%s : %s, $%.2f\n%s : %s, $%.2f" %(invNtry[7][0][0],invNtry[7][0][1],invNtry[7][0][2],invNtry[7][1][0],invNtry[7][1][1],invNtry[7][1][2]))
        loop11_211=0
        while loop11_211!=-1:  # Loop gets Case choice (1,2), asks until valid answer recieved
            casePick=str(input("Choose the number that corresponds with the part you want: "))
            nonlocal mach1Total
            if casePick=="1" or casePick=="2":
                mach1Total+=invNtry[7][0][2]
                mach11_211_()
                loop11_211=-1
            else:
                loop11_211+=1
                
    def mach11_21():
        print("\nNext, let's pick your PSU.\n%s : %s, $%.2f" %(invNtry[6][0][0],invNtry[6][0][1],invNtry[6][0][2]))
        loop11_21=0
        while loop11_21!=-1:  # Loop gets PSU choice (1), asks until valid answer recieved
            psuPick=str(input("Choose the number that corresponds with the part you want: "))
            nonlocal mach1Total
            if psuPick=="1":
                mach1Total+=invNtry[6][0][2]
                mach11_211()
                loop11_21=-1
            else:
                loop11_21+=1

    
    def mach11_2():            
        print("\nNext, let's pick your RAM.\n%s : %s, $%.2f\n%s : %s, $%.2f" %(invNtry[4][0][0],invNtry[4][0][1],invNtry[4][0][2],invNtry[4][1][0],invNtry[4][1][1],invNtry[4][1][2]))
        loop11_2=0
        while loop11_2!=-1:  # Loop gets RAM choice (1,2), asks until valid answer recieved
            ramPick=str(input("Choose the number that corresponds with the part you want: "))
            nonlocal mach1Total
            if ramPick=="1":
                mach1Total+=invNtry[4][0][2]
                mach11_21()
                loop11_2=-1
            elif ramPick=="2":
                mach1Total+=invNtry[4][1][2]
                mach11_21()
                loop11_2=-1
            else:
                loop11_2+=1

    def mach111():
        print("\nNext, let's pick a compatible motherboard.\n%s : %s, $%.2f" %(invNtry[3][1][0],invNtry[3][1][1],invNtry[3][1][2]))
        loop111=0
        while loop111!=-1:  # Loop gets motherboard choice (2) for Intel Core, asks until valid answer recieved
            motherPick=str(input("Choose the number that corresponds with the part you want: "))
            nonlocal mach1Total
            if motherPick=="2":
                mach1Total+=invNtry[3][1][2]
                mach11_2()
                loop111=-1
            else:
                loop111+=1

    def mach112():
        print("\nNext, let's pick a compatible motherboard.\n%s : %s, $%.2f" %(invNtry[3][0][0],invNtry[3][0][1],invNtry[3][0][2]))
        loop112=0
        while loop112!=-1:  # Loop gets motherboard choice (1) for AMD Ryzen, asks until valid answer recieved
            motherPick=str(input("Choose the number that corresponds with the part you want: "))
            nonlocal mach1Total
            if motherPick=="1":
                mach1Total+=invNtry[3][0][2]
                mach11_2()
                loop112=-1
            else:
                loop112+=1

    def mach11():
        print("\nGreat! Let's start building your PC!\n")
        print("First, let's pick a CPU.\n%s : %s, $%.2f\n%s : %s, $%.2f" %(invNtry[2][0][0],invNtry[2][0][1],invNtry[2][0][2],invNtry[2][1][0],invNtry[2][1][1],invNtry[2][1][2]))
        loop11=0
        while loop11!=-1:  # Loop gets CPU choice (1,2), asks until valid answer recieved
            cpuPick=str(input("Choose the number that corresponds with the part you want: "))
            nonlocal mach1Total
            if cpuPick=="1":
                mach1Total+=invNtry[2][0][2]
                mach111()
                loop11=-1
            elif cpuPick=="2":
                mach1Total+=invNtry[2][1][2]
                mach112()
                loop11=-1
            else:
                loop11+=1
     
    while check!=-1:  # Loop gets machineType (1,2,3), asks until valid answer recieved
        machineType = str(input("\nWould you like to build a custom PC (1), purchase a pre-built PC (2), or would you like to checkout (3)? ")) 
        mach1Total=0  # initializes total price of the user selected custom PC
        mach2Total=0  # initializes total price of the user selected pre-built PC
        if machineType=="1":
            mach11()
            print("\nYou have selected all of the required parts! Your total for this PC is $%.2f\n" %mach1Total)
            itemsArr.append(round(mach1Total,2))  # adds total price for current selection to checkout list
            check+=1
        elif machineType=="2":
            print("\nGreat! Let's pick a pre-built PC!\n")
            print("Which prebuilt would you like to order?\n%s : %s, $%.2f\n%s : %s, $%.2f\n%s : %s, $%.2f" %(invNtry[8][0][0],invNtry[8][0][1],invNtry[8][0][2],invNtry[8][1][0],invNtry[8][1][1],invNtry[8][1][2], invNtry[8][2][0],invNtry[8][2][1],invNtry[8][2][2]))
            loop2_=0
            while loop2_!=-1:  # Loop gets user prebuilt choice (1,2,3), asks until valid answer recieved
                preBuilt=str(input("Choose the number that corresponds with the part you want: "))
                if preBuilt=="1":
                    mach2Total+=invNtry[8][0][2]
                    print("\nYour total price for this prebuilt is $%.2f\n" %mach2Total)
                    loop2_=-1
                elif preBuilt=="2":
                    mach2Total+=invNtry[8][1][2]
                    print("\nYour total price for this prebuilt is $%.2f\n" %mach2Total)
                    loop2_=-1
                elif preBuilt=="3":
                    mach2Total+=invNtry[8][2][2]
                    print("\nYour total price for this prebuilt is $%.2f\n" %mach2Total)
                    loop2_=-1
                else:
                    loop2_+=1
            itemsArr.append(round(mach2Total,2))  # adds total price for machine 2 user selections
            check+=1
        elif machineType=="3":
            print(itemsArr)  # prints list of item totals in order of selection
            check=-1  # stops loop
        else:
            check+=1  # loop continues until checkout selected
        
# TESTING CODE
pickItems()