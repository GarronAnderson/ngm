A-REGISTER \| A INPUT FOR ALU \| B-REGISTER \| B INPUT FOR ALU \|
X-REGISTER \| GENERAL PURPOSE \| Y-REGISTER \| GENERAL PURPOSE \|
Z-REGISTER \| ALU OUPUT \| Q-REGISTER \| 2nd MEMORY POINTER \|
\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\|
\~HEX\~\~ \|\~DEC\~ \|A REGISTER instructions \| 0x0000 \|00000 \|NULL
\| 0x0001 \|00001 \|LOAD A IMDIATE \| 0x0002 \|00002 \|LOAD A ADRESS \|
0x0003 \|00003 \|LOAD A ADRESSED BY Q \| 0x0004 \|00004 \|LOAD A
B-REGISTER \| 0x0005 \|00005 \|LOAD A X-REGISTER \| 0x0006 \|00006
\|LOAD A Y-REGISTER \| 0x0007 \|00007 \|LOAD A Z-REGISTER \| 0x0008
\|00008 \|INCREMENT A-REGISTER \| 0x0009 \|00009 \|DECREMENT A-REGISTER
\| \~\~\~\~\~\~ \|\~\~\~\~\~ \|B REGISTER instructions \| 0x000A \|00010
\|NULL \| 0x000B \|00011 \|LOAD B IMDIATE \| 0x000C \|00012 \|LOAD B
ADRESS \| 0x000D \|00013 \|LOAD B ADRESSED BY Q \| 0x000E \|00014 \|LOAD
B A-REGISTER \| 0x000F \|00015 \|LOAD B X-REGISTER \| 0x0010 \|00016
\|LOAD B Y-REGISTER \| 0x0011 \|00017 \|LOAD B Z-REGISTER \| 0x0012
\|00018 \|INCREMENT B-REGISTER \| 0x0013 \|00019 \|DECREMENT B-REGISTER
\| \~\~\~\~\~\~ \|\~\~\~\~\~ \|X REGISTER instructions \| 0x0014 \|00020
\|NULL \| 0x0015 \|00021 \|LOAD X IMDIATE \| 0x0016 \|00022 \|LOAD X
ADRESS \| 0x0017 \|00023 \|LOAD X ADRESSED BY Q \| 0x0018 \|00024 \|LOAD
X A-REGISTER \| 0x0019 \|00025 \|LOAD X B-REGISTER \| 0x001A \|00026
\|LOAD X Y-REGISTER \| 0x001B \|00027 \|LOAD X Z-REGISTER \| 0x001C
\|00028 \|INCREMENT X-REGISTER \| 0x001D \|00029 \|DECREMENT X-REGISTER
\| \~\~\~\~\~\~ \|\~\~\~\~\~ \|Y REGISTER instructions \| 0x001E \|00030
\|NULL \| 0x001F \|00031 \|LOAD Y IMDIATE \| 0x0020 \|00032 \|LOAD Y
ADRESS \| 0x0021 \|00033 \|LOAD Y ADRESSED BY Q \| 0x0022 \|00034 \|LOAD
Y A-REGISTER \| 0x0023 \|00035 \|LOAD Y B-REGISTER \| 0x0024 \|00036
\|LOAD Y X-REGISTER \| 0x0025 \|00037 \|LOAD Y Z-REGISTER \| 0x0026
\|00038 \|INCREMENT X-REGISTER \| 0x0027 \|00039 \|DECREMENT X-REGISTER
\| \~\~\~\~\~\~ \|\~\~\~\~\~ \|Z REGISTER instructions \| 0x0028 \|00040
\|NULL \| 0x0029 \|00041 \|L-SHIFT Z-REGISTER \| 0x002A \|00042
\|R-SHIFT Z-REGISTER \| 0x002B \|00043 \|ADD A+B \| 0x002C \|00044 \|SUB
A-B \| 0x002D \|00045 \|COMPARE A+B (Sub A-B and don\'t change A)\|
0x002E \|00046 \|NULL \| 0x002F \|00047 \|NULL \| 0x0030 \|00048
\|INCREMENT Z-REGISTER \| 0x0031 \|00049 \|DECREMENT Z-REGISTER \|
\~\~\~\~\~\~ \|\~\~\~\~\~ \|BRANCH instructions \| 0x0032 \|00050
\|BRANCH \| 0x0033 \|00051 \|BRANCH IF 0 \| 0x0034 \|00052 \|BRANCH IF
!0 \| 0x0035 \|00053 \|BRANCH IF CARRY \| 0x0036 \|00054 \|BRANCH IF
!CARRY \| 0x0037 \|00055 \|GOSUB (CSB) \| 0x0038 \|00056 \|RETURN FROM
SUB \| 0x0039 \|00057 \| \| 0x003A \|00058 \| \| 0x003B \|00059 \|HALT
\| \~\~\~\~\~\~ \|\~\~\~\~\~ \|MEMORY instructions \| 0x003C \|00060
\|MOVE A TO ADRESS \| 0x003E \|00061 \|MOVE B TO ADRESS \| 0x003F
\|00062 \|MOVE X TO ADRESS \| 0x0040 \|00063 \|MOVE Y TO ADRESS \|
0x0041 \|00064 \|MOVE Z TO ADRESS \| 0x0042 \|00065 \|MOVE A TO Q ADRESS
\| 0x0043 \|00066 \|MOVE B TO Q ADRESS \| 0x0044 \|00067 \|MOVE X TO Q
ADRESS \| 0x0045 \|00068 \|MOVE Y TO Q ADRESS \| 0x0046 \|00069 \|MOVE Z
TO Q ADRESS \| 0x0047 \|00070 \|NULL \| 0x0048 \|00071 \|NULL \| 0x0049
\|00072 \|NULL \|

73 NULL 74 INQ 75 DCQ 76 TAQ 77 TBQ 78 TXQ 79 TYQ 80 TZQ 81 TQA 82 TQB
83 TQX 84 TQY 85 TQZ 86