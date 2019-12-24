import random

tuplesize = 3
H_tuple1 = []
H_tuple2 = []
H_tuple3 = []
H_tuple4 = []
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
poscount = 0
for x in range(0, tuplesize, 1):
    H_tuple1.append(0)
    H_tuple1[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(H_tuple1[x])
    poscount += 1

    H_tuple2.append(0)
    H_tuple2[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(H_tuple2[x])
    poscount += 1

    H_tuple3.append(0)
    H_tuple3[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(H_tuple3[x])
    poscount += 1

    H_tuple4.append(0)
    H_tuple4[x] = pos[random.randint(0, 11 - poscount)]
    pos.remove(H_tuple4[x])
    poscount += 1

def binarytree(tuplearr):
    if(tuplearr[0] == 0):
        if(tuplearr[1] == 0):
            if(tuplearr[2] == 0):
                return '000'
            else:
                return '001'
        else:
            if(tuplearr[2] == 0):
                return '010'
            else:
                return '011'
    else:
        if(tuplearr[1] == 0):
            if(tuplearr[2] == 0):
                return '100'
            else:
                return '101'
        else:
            if(tuplearr[2] == 0):
                return '110'
            else:
                return '111'