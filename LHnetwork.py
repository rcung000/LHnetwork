import random

tuplesize = 3

def tupleassign(tuplesize):
    """assigns a set randomly generated tuple position"""
    pos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    poscount = 0
    cookie = [[], [], [], []]
    for x in range(0, tuplesize, 1):
        cookie[0].append(0)
        cookie[0][x] = pos[random.randint(0, 11 - poscount)]
        pos.remove(cookie[0][x])
        poscount += 1

        cookie[1].append(0)
        cookie[1][x] = pos[random.randint(0, 11 - poscount)]
        pos.remove(cookie[1][x])
        poscount += 1

        cookie[2].append(0)
        cookie[2][x] = pos[random.randint(0, 11 - poscount)]
        pos.remove(cookie[2][x])
        poscount += 1

        cookie[3].append(0)
        cookie[3][x] = pos[random.randint(0, 11 - poscount)]
        pos.remove(cookie[3][x])
        poscount += 1
    return cookie


def binarytree(tuplearr):
    """used to read and determine values"""
    if(tuplearr[0] == 0 or tuplearr[0] == '0'):
        if(tuplearr[1] == 0 or tuplearr[1] == '0'):
            if(tuplearr[2] == 0 or tuplearr[2] == '0'):
                return '000'
            else:
                return '001'
        else:
            if(tuplearr[2] == 0 or tuplearr[2] == '0'):
                return '010'
            else:
                return '011'
    else:
        if(tuplearr[1] == 0 or tuplearr[1] == '0'):
            if(tuplearr[2] == 0 or tuplearr[2] == '0'):
                return '100'
            else:
                return '101'
        else:
            if(tuplearr[2] == 0 or tuplearr[2] == '0'):
                return '110'
            else:
                return '111'