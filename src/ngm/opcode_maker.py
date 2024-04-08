import pprint

opcodes = {}

while True:
    opcode_str = input("opcode name: ")
    if opcode_str == "DONE":
        break
    
    opcode_int = int(input("opcode code: "))
    opcodes.update({opcode_str:opcode_int})
    
pprint.pformat(opcodes)
    