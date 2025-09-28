class hex:
    def __init__(self):
        self._hex_dict = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        self._iteration_boundaries = [1,16,256,4096,65536,1048576,16777216,268435456,4294967296]
        self._finalhex = "0x"
        self._passvalue = None

    def hexbit(self,placevalue,divnum):
        placevalue = placevalue//divnum
        difference = self._passvalue - placevalue*divnum
        self._finalhex = self._finalhex + self._hex_dict[placevalue]
        return difference

hexnum = hex()
numtoconvert = int(input("Enter a number in base 10 between 0 and 4,294,967,296\n"))


for i in range(len(hexnum._iteration_boundaries)):
    if numtoconvert >= hexnum._iteration_boundaries[i]:
        pass
    else:
        iternum = hexnum._iteration_boundaries.index(hexnum._iteration_boundaries[i])
        break

hexnum._passvalue = numtoconvert
for i in range(iternum):
    hexnum._passvalue = hexnum.hexbit(hexnum._passvalue,hexnum._iteration_boundaries[iternum - 1 - i])

print("\nThe decimal number ",numtoconvert," in Hexidecimal is ",hexnum._finalhex)