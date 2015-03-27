import math
import sys
import os

pizza = []

def tester_part(R1, C1, R2, C2):

    jambons = 0
    cases = 0

    for i in range(R1, R2+1):
        for j in range(C1, C2+1):
            if pizza[i][j] == 'H':
                jambons += 1

            print pizza[i][j]

            cases += 1

    print jambons
    print cases

    if jambons >= 3 and cases <= 12:
        return True
    else:
        return False

def partager_pizza(R,C,H,S):

    parts = []

    for i in range(R):
        for j in range(C):
            R1 = i
            C1 = j

            for x in range(4):
                for y in range(4):
                    R2 = i + x
                    C2 = j + y

                    size = (R2-R1+1)*(C2-C1+1)

                    if size >= 3 and size <= 12:
                        if tester_part(R1, C1, R2, C2):
                            parts.append([R1, C1, R2, C2])
                            write_part(R1, C1, R2, C2)





    return parts

def write_part(R1, C1, R2, C2):
    for i in range(R1, R2+1):
        for j in range(C1, C2+1):
            pizza[i][j] = 'X'


def output(parts):
    f = open('output.txt','w')

    f.write(len(parts))
    for part in parts:
        f.write("{0} {1} {2} {3}".format(part[0], parts[1], parts[2], parts[3]))

if __name__ == '__main__':
    print "Hash code test round"

    R,C,H,S = [int(i) for i in raw_input().split()]

    print "R:%s, C:%s, H:%s, S:%s" % (R,C,H,S)

    for i in range(R):
        pizza.append(raw_input())
        print pizza[i]


    print "Parts : "

    tester_part(0, 0, 2, 1)