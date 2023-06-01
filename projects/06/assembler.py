# writing this in python cuz self harm isnt good kids :)
# almost wrote this in C but then reevaluated my life choices


# ! just some setup shit

symbols = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "R15": 15,
    "SCREEN": 16384,
    "KBD": 24576
}

output_commands = []

# ! First, open a file

# idk how argc and argv work in python, dont want to learn so we doin input bois

filename = input("path to ASM file >>>")

f = open(filename,"r")

lines = f.readlines()

f.close()

# ! Now, we run through all lines

for line in lines:
    # first remove whitespace
    usable_line = line.replace(' ', '')

    # skip over blank lines (or comments)
    if usable_line == '' or usable_line.startswith('//'):
        continue

    # now we can decifer the code in the line
    if usable_line.count('@'): # A instruction
        # first, check if it is only numbers
        if usable_line[1:].isdigit():
            # go to aforementioned digit
            address = usable_line
        # now to check if it is in the symbol table
        elif usable_line[1:] in symbols.keys():
            address = symbols[usable_line[1:]]
        else:
            # not at all stolen code here, move along (https://stackoverflow.com/questions/28176866/find-the-smallest-positive-number-not-in-list)
            address = next(i for i, e in enumerate(sorted(symbols.values()) + [ None ], 1) if i != e)
            symbols[usable_line[1:]] = address
        # ! here we convert the address into binary and put it into the command starting with 0
        # so for a binary value xxx, it would be 0xxx (except this has to be 14 digits, so we need to pad left with 0s)
        command = '0'+bin(address)[3:].rjust(14,'0')
        output_commands.append(command)

    else: # C instruction
        # Check what type of c instruction
        if line.count('='): # Write to something
            partition = line.split('=')
            destination = partition[0]
            content=partition[1]
            # TODO this would be a normal ALU instruction, will save in data (see fig. 6.2 on pg 107)
        elif line.count('('): # JMP destination thingy
            # first parse between parentheses
            mn = usable_line.find('(') + 1
            mx = usable_line.find(')') - 1
            symbols[usable_line[mn:mx]] = lines.index(line)
        elif line.count(';'): # JMP
            # ! types of jumps
            # TODO jumping (see fig. 6.2 on pg 107)
