/Assemble me to test the assembler.

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

>256
'Test