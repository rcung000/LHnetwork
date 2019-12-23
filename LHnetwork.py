import random

tuplesize = 3
MSet = 4
J1 = []
J2 = []
J3 = []
J4 = []
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
poscount = 0
for x in range(0, tuplesize, 1):
    J1.append(0)
    J1[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(J1[x])
    poscount += 1

    J2.append(0)
    J2[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(J2[x])
    poscount += 1

    J3.append(0)
    J3[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(J3[x])
    poscount += 1

    J4.append(0)
    J4[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(J4[x])
    poscount += 1
print(J1)
print(J2)
print(J3)
print(J4)