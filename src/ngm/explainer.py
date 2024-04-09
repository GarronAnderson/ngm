"explain opcodes"

import opcodes

explained = {}

for opcode in opcodes.opcodes:
    exp = input(f'Explain {opcode}: ')
    explained.update({opcode:exp})