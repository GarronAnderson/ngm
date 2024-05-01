"""
Original assembler/virtual computer from Sebastian Miller.

Unchanged from original source.
"""

import math
import sys
import pygame
import os
from pygame.locals import QUIT


# 	memory 24 bit    8 16

mem = [[0, 0]] * 65536


#   load program into memory ( load.txt is where you can write assymbly for the code to compile for the virtual computer )

file = open("load.txt", "r")
data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].replace("\n", "")

place = 0
fileR = 0
print("\n\n")
while True:
    item = data[fileR]
    if len(item) > 0:
        if item[0] != "/":
            if item[0] == ">":
                place = int(item[1:]) - 1
            elif item == "<<":
                break
            elif item[0] == "'":
                item = item[1:]
                k = ""
                for let in item:

                    mem[place][1] = ord(let)
                    k += str(ord(let)) + " , "
                    place += 1
                print("END", " ", place, "    ", item, "    ", k)
            else:

                # load register commands

                if item[:1].upper() == ";":
                    mem[place][0] = 0
                    mem[place][1] = int(item[1:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "LDA":
                    mem[place][0] = 30
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "LDB":
                    mem[place][0] = 31
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "LDX":
                    mem[place][0] = 32
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "LDY":
                    mem[place][0] = 33
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "LDZ":
                    mem[place][0] = 34
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "LDQ":
                    mem[place][0] = 35
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 	increment command

                if item[:3].upper() == "INA":
                    mem[place][0] = 40
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "INB":
                    mem[place][0] = 41
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "INX":
                    mem[place][0] = 42
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "INY":
                    mem[place][0] = 43
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "INZ":
                    mem[place][0] = 44
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "INQ":
                    mem[place][0] = 45
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 	decrement command

                if item[:3].upper() == "DCA":
                    mem[place][0] = 50
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "DCB":
                    mem[place][0] = 51
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "DCX":
                    mem[place][0] = 52
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "DCY":
                    mem[place][0] = 53
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "DCZ":
                    mem[place][0] = 54
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "DCQ":
                    mem[place][0] = 55
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 	math // only effects the z register

                if item[:3].upper() == "ADD":
                    mem[place][0] = 60
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "SUB":
                    mem[place][0] = 61
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "FSZ":
                    mem[place][0] = 62
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "BSZ":
                    mem[place][0] = 63
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 	move (register) ---> (memory location)

                if item[:3].upper() == "MVA":
                    mem[place][0] = 70
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MVB":
                    mem[place][0] = 71
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MVX":
                    mem[place][0] = 72
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MVY":
                    mem[place][0] = 73
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MVZ":
                    mem[place][0] = 74
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 			branching

                if item[:3].upper() == "JMP":
                    mem[place][0] = 80
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "JMZ":
                    mem[place][0] = 81
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "JNZ":
                    mem[place][0] = 82
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "JSR":
                    mem[place][0] = 83
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "RET":
                    mem[place][0] = 84
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "JMN":
                    mem[place][0] = 85
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 			Write memory location to register

                if item[:3].upper() == "MLA":
                    mem[place][0] = 90
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )
                if item[:3].upper() == "MLB":
                    mem[place][0] = 91
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )
                if item[:3].upper() == "MLX":
                    mem[place][0] = 92
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )
                if item[:3].upper() == "MLY":
                    mem[place][0] = 93
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )
                if item[:3].upper() == "MLZ":
                    mem[place][0] = 94
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )
                if item[:3].upper() == "MLQ":
                    mem[place][0] = 95
                    mem[place][1] = int(item[3:])
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 			reg ---> loc[q-reg]

                if item[:3].upper() == "MQA":
                    mem[place][0] = 100
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MQB":
                    mem[place][0] = 101
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MQX":
                    mem[place][0] = 102
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MQY":
                    mem[place][0] = 103
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MQZ":
                    mem[place][0] = 104
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # MOVE Z --- > REG

                if item[:3].upper() == "MZA":
                    mem[place][0] = 200
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MZB":
                    mem[place][0] = 201
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MZQ":
                    mem[place][0] = 202
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "MZX":
                    mem[place][0] = 203
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # MOVE Q --- > REG

                if item[:3].upper() == "QTA":
                    mem[place][0] = 300
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "QTB":
                    mem[place][0] = 301
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "QTZ":
                    mem[place][0] = 302
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "QTX":
                    mem[place][0] = 303
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                # 		memory[location[q]] --> reg

                if item[:3].upper() == "FQA":
                    mem[place][0] = 400
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "FQB":
                    mem[place][0] = 401
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "FQX":
                    mem[place][0] = 402
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "FQY":
                    mem[place][0] = 403
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

                if item[:3].upper() == "FQZ":
                    mem[place][0] = 404
                    mem[place][1] = 0
                    print(
                        place,
                        "    ",
                        item,
                        "    ",
                        str(mem[place][0]) + "-" + str(mem[place][1]),
                    )

    place += 1
    fileR += 1

pygame.init()
screen = pygame.display.set_mode((500, 500))

#   vram start location  63343


def readv():

    j = 63343
    v = ""
    list = []
    for k in range(43):
        v = ""
        for i in range(51):
            v += letters[mem[j][1]]
            j += 1
        list.append(v)

    return list


def draw():
    screen.fill((100, 100, 100))

    s = readv()

    letter = pygame.font.Font("bit.ttf", 30)

    # 	line length is 50

    for i in range(39):
        text_surface = letter.render(s[i], False, (200, 200, 200))
        screen.blit(text_surface, (5, i * 24))


#   ASCII

letters = [
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    '"',
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "[",
    " ",
    "]",
    "^",
    "_",
    "`",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    ",",
    "{",
    "}",
    "~",
    "~",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]


# 	key input stored at 63340


def execute(p):

    if z[0] == 0:
        Z_F[0] = True
    else:
        Z_F[0] = False

    if mem[p][1] + mem[p][0] != 0:

        cmd = mem[p][0]
        num = mem[p][1]

        # 		load registers

        # 	load a

        if cmd == 30:
            a[0] = num

        # 	load b

        if cmd == 31:
            b[0] = num

        # 	load x

        if cmd == 32:
            x[0] = num

        # 	load y

        if cmd == 33:
            y[0] = num

        # 	load z

        if cmd == 34:
            z[0] = num

        # 	load q

        if cmd == 35:
            q[0] = num

        # 			increment

        # 	inc a

        if cmd == 40:
            a[0] += 1

        # 	inc b

        if cmd == 41:
            b[0] += 1

        # 	inc x

        if cmd == 42:
            x[0] += 1

        # 	inc y

        if cmd == 43:
            y[0] += 1

        # 	inc z

        if cmd == 44:
            z[0] += 1

        # 	inc z

        if cmd == 45:
            q[0] += 1

        # 			decrement

        # 	ad a

        if cmd == 50:
            a[0] -= 1

        # 	ad b

        if cmd == 51:
            b[0] -= 1

        # 	dec x

        if cmd == 52:
            x[0] -= 1

        # 	dec y

        if cmd == 53:
            y[0] -= 1

        # 	dec z

        if cmd == 54:
            z[0] -= 1

        if cmd == 55:
            q[0] -= 1

        # 			math

        # 	a + b

        if cmd == 60:
            z[0] = a[0] + b[0]

        # 	b - a

        if cmd == 61:
            z[0] = b[0] - a[0]

        # 	z <<

        if cmd == 62:
            z[0] = (z[0] << 1) % 255

        # 	z >>

        if cmd == 63:
            z[0] = (z[0] >> 1) % 255

        # 			move

        # 	mov a

        if cmd == 70:
            mem[num][1] = a[0]
        # 	mov b

        if cmd == 71:
            mem[num][1] = b[0]

        # 	mov x

        if cmd == 72:
            mem[num][1] = x[0]

        # 	mov y

        if cmd == 73:
            mem[num][1] = y[0]

        # 	mov z

        if cmd == 74:
            mem[num][1] = z[0]

        # 			JUMP

        # 	JUMP non bool operated

        if cmd == 80:
            pointer[0] = num - 1

        # 	JUMP IF ZERO

        if cmd == 81:
            if Z_F[0]:
                pointer[0] = num - 1

        # 	JUMP IF NOT ZERO

        if cmd == 82:
            if not Z_F[0]:
                pointer[0] = num - 1

        # 	JUMP TO SUBROUTINE

        if cmd == 83:
            ret[0] = pointer[0]
            pointer[0] = num - 1

        # 	RETURN

        if cmd == 84:
            pointer[0] = ret[0]

        # 	JUMP IF NOT NEGITIVE

        if cmd == 85:
            if z[0] < 0:
                pointer[0] = num - 1

        # 			move (memory location) ---> (register)

        # mem > a

        if cmd == 90:
            a[0] = mem[num][1]

        # mem > b

        if cmd == 91:
            b[0] = mem[num][1]

        # mem > x

        if cmd == 92:
            z[0] = mem[num][1]

        # mem > y

        if cmd == 93:
            y[0] = mem[num][1]

        # mem > z

        if cmd == 94:
            z[0] = mem[num][1]

        # mem > q

        if cmd == 95:
            q[0] = mem[num][1]

        # 			write reg > mem[reg-q]

        # a > ql

        if cmd == 100:
            mem[q[0]][1] = a[0]

        # b > ql

        if cmd == 101:
            mem[q[0]][1] = b[0]

        # x > ql

        if cmd == 102:
            mem[q[0]][1] = x[0]

        # y > ql

        if cmd == 103:
            mem[q[0]][1] = y[0]

        # z > ql

        if cmd == 104:
            mem[q[0]][1] = z[0]

        mem[63340][1] = 0
        # 	Z ----> REG

        # z > a

        if cmd == 200:
            a[0] = z[0]

        # z > b

        if cmd == 201:
            b[0] = z[0]

        # z > q

        if cmd == 202:
            q[0] = z[0]

        # z > x

        if cmd == 203:
            x[0] = z[0]

        # 	Q ----> REG

        # q > a

        if cmd == 300:
            a[0] = q[0]

        # q > b

        if cmd == 301:
            b[0] = q[0]

        # q > z

        if cmd == 302:
            z[0] = q[0]

        # q > z

        if cmd == 303:
            x[0] = q[0]

        # mem[q] --> reg

        if cmd == 400:
            mem[q[0]] = a[0]

        if cmd == 401:
            mem[q[0]] = b[0]

        if cmd == 402:
            mem[q[0]] = x[0]

        if cmd == 403:
            mem[q[0]] = y[0]

        if cmd == 404:
            mem[q[0]] = z[0]


def sleep(x):
    for i in range(x * 2000):
        i = i


#   registers

q = [0]

ret = [0]

a = [0]
b = [0]
x = [0]
y = [0]
z = [0]
Z_F = [False]


pointer = [0]
lc = 0
while True:

    execute(pointer[0])
    pointer[0] += 1
    key = 0

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    for i in range(len(keys)):
        if keys[i]:
            key = i

    if key != "":
        mem[63340][1] = key

    draw()
    pygame.display.flip()
    pygame.display.set_caption(
        "a: "
        + str(a)
        + "    b: "
        + str(b)
        + "    x: "
        + str(x)
        + "    y: "
        + str(y)
        + "    z: "
        + str(z)
        + "    q: "
        + str(q)
        + " last key : "
        + str(lc)
    )
