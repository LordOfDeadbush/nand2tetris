# writing this in python cuz self harm isnt good kids :)
# almost wrote this in C but then reevaluated my life choices


# ! First, open a file

# idk how argc and argv work in python, dont want to learn so we doin input bois

filename = input("path to ASM file >>>")

f = open(filename,"r")

lines = f.readlines()

f.close()

# ! Now, we run through all lines

for line in lines:

    # first, skip over blank lines (or comments)
    if line == '' or line.startswith('//'):
        continue

    # now we can decifer the code in the line
    if line.startswith('@'): # A instruction
        # TODO
    else: # C instruction
        # Check what type of instruction
        if line.count('='): # Write to something
            # TODO
        elif line.count(';'): # JMP
            # TODO