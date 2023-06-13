# writing this in python cuz self harm isnt good kids :)
# almost wrote this in C but then reevaluated my life choices

import re # better string split

# ! just some setup shit

jump_symbols = {
    'null': '000',
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111',
}

# this has all of a and c
comp_symbols = {
    '0':   '0101010',
    '1':   '0111111',
    '-1':  '0111010',
    'D':   '0001100',
    'A':   '0110000',
    'M':   '1110000',
    '!D':  '0001101',
    '!A':  '0110001',
    '!M':  '1110001',
    '-D':  '0001111',
    '-A':  '0110011',
    '-M':  '1110011',
    'D+1': '0011111',
    'A+1': '0110111',
    'M+1': '1110111',
    'D-1': '0001110',
    'A-1': '0110010',
    'M-1': '1110010',
    'D+A': '0000010',
    'D+M': '1000010',
    'D-A': '0010011',
    'D-M': '1010011',
    'A-D': '0000111',
    'M-D': '1000111',
    'D&A': '0000000',
    'D&M': '1000000',
    'D|A': '0010101',
    'D|M': '1010101',
    
}

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

# filename = input("path to ASM file >>>")

filename = 'C:\\Users\\agumm\\Documents\\GitHub\\nand2tetrissolutions\\projects\\06\\rect\\RectL.asm'

f = open(filename,"r")

lines = f.readlines()

f.close()

# ! Now, we run through all lines

for line in lines:
    # print(line, end='')
    # first remove whitespace
    usable_line = line.replace(' ', '').replace('\n', '').replace('\t', '')

    usable_line = line.split('//')[0] # remove comment

    print(usable_line, end='')


    # skip over blank lines (or comments)
    if usable_line == '' or usable_line.startswith('//') or usable_line == '\n':
        continue

    usable_line = usable_line.replace(' ', '').replace('\n', '') # seems redundant, idk why this is needed

    # now we can decifer the code in the line
    if '@' in line: # A instruction
        # first, check if it is only numbers
        if usable_line[1:].isdigit():
            # print("isdigit")
            # go to aforementioned digit
            address = usable_line.replace('@', '')
            # print(address)
        # now to check if it is in the symbol table
        elif usable_line[1:] in symbols.keys():
            address = symbols[usable_line[1:]]
        else:
            # not at all stolen code here, move along (https://stackoverflow.com/questions/28176866/find-the-smallest-positive-number-not-in-list)
            address = next(i for i, e in enumerate(sorted(symbols.values()) + [ None ], 1) if i != e)
            symbols[usable_line[2:]] = address
        # ! here we convert the address into binary and put it into the command starting with 0
        # so for a binary value xxx, it would be 0xxx (except this has to be 14 digits, so we need to pad left with 0s)
        command = '0'+bin(int(address))[2:].rjust(15,'0')
        output_commands.append(command)

    elif '(' in line: # JMP destination thingy
        # first parse between parentheses
        mn = usable_line.find('(') + 1
        mx = usable_line.find(')') - 1
        symbols[usable_line[mn:mx]] = lines.index(line)
        continue
    else: # C instruction
        partition = re.split('=|;', usable_line)
        jump = jump_symbols['null']
        dest_list = ['0','0','0']
        jump_part = 1
        comp_part = 0

        # * dest
        if '=' in line:
            if 'A' in partition[0]:
                dest_list[0] = '1'
            if 'D' in partition[0]:
                dest_list[1] = '1'
            if 'M' in partition[0]:
                dest_list[2] = '1'
            jump_part=2
            comp_part=1
        dest=''.join(dest_list)

        # * jump
        if ';' in line: # jump
            # print(jump_part)
            # print(partition)
            jump = jump_symbols[partition[jump_part]]

        # * comp
        comp = comp_symbols[partition[comp_part]]

        # * now to join everything together

        command = '111' + comp + dest + jump
        output_commands.append(command)

# now to output everything together
# print('\n'.join(output_commands))

resultfilename = filename.replace('.asm', '.hack')
f = open(resultfilename,"w")
f.write('\n'.join(output_commands))
f.close()