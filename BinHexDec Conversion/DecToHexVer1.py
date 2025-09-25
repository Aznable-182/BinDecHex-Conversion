hex_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
finalhex = "0x"
numtoconvert = int(input("Enter a number in base 10 between 0 and 255\n"))
if numtoconvert > 15:
    firsthex = (numtoconvert//16)
    print(firsthex)
    if firsthex > 9:
        finalhex = finalhex + hex_dict[firsthex]
    else:
        finalhex = finalhex + str(firsthex)
        
sechex = numtoconvert%16
if sechex > 9:
    finalhex = finalhex + hex_dict[sechex]
else:
    finalhex = finalhex + str(sechex)

print("The decimal number ",numtoconvert," in Hexidecimal is ",finalhex)