numtoconvert = int(input("Enter a number in base 10\n"))
currentnum = numtoconvert
binarystring = []
newbinarystring = []
running = True
while running == True:
    for i in range(currentnum//2):
        binarystring.append(currentnum%2)
        currentnum = currentnum//2
    running = False
    for i in range(len(binarystring)):
        newbinarystring.append(binarystring[len(binarystring)-i-1])
    for i in range(len(newbinarystring)):
        if newbinarystring[0] == 0:
            newbinarystring.remove(newbinarystring[0])
        elif newbinarystring[0] == 1:
            break
    print("The Decimal Number ", numtoconvert, " in Binary is ", newbinarystring)
        
    
