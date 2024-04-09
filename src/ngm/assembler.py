"""NGM Assembler v0.3

By Garron Anderson"""

import argparse

from opcodes import opcodes
from explained import explained

"""
EXAMPLE PROGRAM

$PORTB = x6000
$PORTA = x6003

LDA 32
LDB $PORTA
CMP
JNC loop

:start
LDB 1

LDA 42
LDA d42
LDA b00101010
LDA x2A

:loop
ADD
STA $PORTB
JC start
JMP loop

>63343
'Test Program.
"""

# use argparse to get config

parser = argparse.ArgumentParser(prog = 'python assembler.py', \
                                 description = 'Assembles code for ngm', \
                                 epilog = 'By Garron Anderson (report bugs to <garronanderson4321@gmail.com>)')
parser.add_argument('filename')
parser.add_argument('-o', '--output_file', nargs = '?', default = 'asm.out', help = 'assembled output file name (default asm.out)')
parser.add_argument('-v', '--verbose', action = 'store_true', help = 'be non-technically verbose and explain during compile')
parser.add_argument('-vv', '--very_verbose', action = 'store_true', help = 'dump what is put to mem during assemble')
parser.add_argument('--version', action='version', version = 'ngm assembler 0.3')
args = parser.parse_args()

# copy config in

input_filename = args.filename
output_filename = args.output_file
DEBUG = args.verbose or args.very_verbose
verbose = args.verbose
very_verbose = args.very_verbose

# --- BEGIN HELPER FUNCTIONS ---

def convert_forms(lineno, line, mem_loc):
    """
    Convert data to decimal (from binary, hex, variable, label)
    """
    
    global labels, variables
    
    opcode, _, data = line.partition(' ') # get opcode and data
    to_convert = data[1:]
    
    if data.startswith('= '): # strip variable declarations to fully process
        data = data[2:]
        to_convert = data[1:]
    
    if not data: # ok, there's no data
        data = 0
        
    elif data.isdecimal(): # the data is explicitly decimal, don't need try-except
        data = int(data)
        
    elif data.startswith('d'): # try for explicit decimal
        try:
            data = int(to_convert)
        except ValueError:
            data = try_label(lineno, line, mem_loc)
           
    elif data.startswith('b'): # try for binary
        try:
            data = int(to_convert, 2)
        except ValueError:
            data = try_label(lineno,line, mem_loc)
            
    elif data.startswith('x'): # try for hex
        try:
            data = int(to_convert, 16)
        except ValueError:
            data = try_label(lineno,line, mem_loc)
            
    elif data.startswith('$'): # try for variables
        try:
            data = variables[to_convert]
        except KeyError:
            raise AssemblyError(f'Unrecognized variable name {to_convert} on line {lineno+1}')
        
    else: # ok, try for a label
        data = try_label(lineno, line, mem_loc)

    return data

def try_label(lineno, line, mem_loc):
    """
    Try to convert a label.
    If it fails, add to the list of labels to retry.
    """
    
    global to_retry, labels
    opcode, _, data = line.partition(' ')
    try:
        data = labels[data]
    except KeyError: # ok, retry later
        to_retry.append((lineno, line, mem_loc))
        data = "retry label later" # this is fine, we'll fix it later
    
    return data
 
def retry_lines(to_retry):
    """
    Retry missing labels.
    """
    
    global mem, labels
    for lineno, line, mem_loc in to_retry: 
        opcode, _, data = line.partition(' ') 
        
        try: # catch bad labels
            data = labels[data]
        except KeyError:
            raise AssemblyError(f'Unrecognized label {data} at line {lineno}')
        
        try: # catch bad opcodes
            opcode_int = opcodes[opcode]
        except KeyError:
            raise AssemblyError(f'Illegal opcode "{opcode}" on line {lineno+1}')
        
        if very_verbose: print(f'{int(mem_loc):6}|{hex(mem_loc):8}|{opcode:4}|{opcode_int:4}|{raw_data:10}|{data}')
        mem[mem_loc] = [opcode_int, data] # and write to memory
        
# --- END HELPER FUNCTIONS ---
         
class AssemblyError(Exception):
    """
    A class for assembly errors.
    """
    pass


# Set up mem
mem = [[0, 0]] * 65536

# get input to assemble
assembly_in = open(input_filename)
assembly = assembly_in.readlines()
assembly_in.close()
assembly = [line.strip() for line in assembly]

# set up assembler
mem_loc = 0
labels = {}
variables = {}
to_retry = []

# --- MAIN PROCESSING ----

for lineno, line in enumerate(assembly):
    if not line:  # skip empty lines
        continue

    if line.startswith("/"):  # Handle comments
        if DEBUG: print(f"Comment: {line[1:]} on line {lineno+1}")
        continue  # Ignore comments, they don't matter for output

    elif line.startswith(">"):  # Handle like .org
        mem_loc = int(line[1:])
        if verbose: print(f"Going to {mem_loc}")
        if very_verbose: print() # just for formatting
        continue
    
    elif line.startswith("'"):  # Handle like .asciiz
        text = line[1:]
        if verbose: print(f"Text <{text}> at line {lineno+1}")
        for letter in text:
            if verbose: print(f'Putting {letter} at {mem_loc}')
            if very_verbose: print(f'{int(mem_loc):6}|{hex(mem_loc):8}|    |    |{letter:10}|{ord(letter)}')
            mem[mem_loc] = [0, ord(letter)]
            mem_loc += 1
        continue
    
    elif line.startswith(":"): # label
        label_name = line[1:]
        labels.update({label_name:mem_loc})
        if verbose: print(f'Label {label_name} at location {mem_loc}')
        if very_verbose: print(f'{label_name}:')
        continue
    
    elif line.startswith("$"): # variable
        line = line[1:]
        name, _, raw_value = line.partition(" = ")
        value = convert_forms(lineno, line, mem_loc)
        variables.update({name:value})
        if verbose: print(f'Variable {name} with value {value}')
        if very_verbose: print(f'      |${name:17}|{raw_value:10}|{value}\n')
        continue

    try: # get the numerical opcode
        opcode, _, raw_data = line.partition(" ")
        opcode_int = opcodes[opcode]
    except KeyError:
        raise AssemblyError(f'Illegal Opcode "{opcode}" on line {lineno+1}')
    
    # if we're here we now have a numerical opcode
    # so process the second half of the instruction 
    data = convert_forms(lineno, line, mem_loc)
    
    if verbose: print(f'Opcode {opcode} ({explained[opcode]}) with data {data} at location {mem_loc}')
    
    # --- Okay, write to memory ---
    
    if very_verbose: print(f'{int(mem_loc):6}|{hex(mem_loc):8}|{opcode:4}|{opcode_int:4}|{raw_data:10}|{data}')
    mem[mem_loc] = [opcode_int, data]
    
    mem_loc += 1

# --- END MAIN PROCESSING ---

# retry missing labels
if very_verbose: print("\nRetrying Labels") # formatting
retry_lines(to_retry)

# convert mem to binary
processed_mem = bytearray()
for data in mem:
    processed_mem.append(data[0])
    msb, lsb = divmod(data[1], 256)
    processed_mem.append(msb)
    processed_mem.append(lsb)   
    
# --- write to file ---
output_file = open(output_filename, 'wb')
output_file.write(processed_mem)
output_file.close()