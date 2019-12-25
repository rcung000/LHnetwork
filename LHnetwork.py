import random

tuplesize = 3

def tupleassign(tuplesize):
    """assigns a set randomly generated tuple position"""
    pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
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
                return 0
            else:
                return 1
        else:
            if(tuplearr[2] == 0 or tuplearr[2] == '0'):
                return 2
            else:
                return 3
    else:
        if(tuplearr[1] == 0 or tuplearr[1] == '0'):
            if(tuplearr[2] == 0 or tuplearr[2] == '0'):
                return 4
            else:
                return 5
        else:
            if(tuplearr[2] == 0 or tuplearr[2] == '0'):
                return 6
            else:
                return 7


# RANDOMLY GENERATED ONLY ONCE (J sets)
placements = tupleassign(tuplesize)
print(placements)
# Corresponding J sets
L_1 = []
L_2 = []
L_3 = []
L_4 = []
# TRAINING MEMORY
H_tuple1 = [0, 0, 0, 0, 0, 0, 0, 0]
H_tuple2 = [0, 0, 0, 0, 0, 0, 0, 0]
H_tuple3 = [0, 0, 0, 0, 0, 0, 0, 0]
H_tuple4 = [0, 0, 0, 0, 0, 0, 0, 0]
L_tuple1 = [0, 0, 0, 0, 0, 0, 0, 0]
L_tuple2 = [0, 0, 0, 0, 0, 0, 0, 0]
L_tuple3 = [0, 0, 0, 0, 0, 0, 0, 0]
L_tuple4 = [0, 0, 0, 0, 0, 0, 0, 0]

# Begin reading from Datasets
L_dataset = "L_images.txt"
H_dataset = "H_images.txt"
H_open = open(H_dataset)
for a in range(0, 199, 1):
    H_data = H_open.readline()
    #Strip off [ , ] and isolate
    step0 = H_data.split('[')
    step1 = step0[1]
    step2 = step1.split(']')
    step3 = step2[0]
    step4 = step3.split(', ')
    H_arr = []
    # Corresponding J sets
    H_1 = []
    H_2 = []
    H_3 = []
    H_4 = []
    for x in range(0, 12, 1):
        H_arr.append(step4[x])
    print(H_arr)
    #Split into tuples
    for a in range(0, tuplesize, 1) :
        H_1.append(H_arr[placements[0][a]])
        H_2.append(H_arr[placements[1][a]])
        H_3.append(H_arr[placements[2][a]])
        H_4.append(H_arr[placements[3][a]])
    print (H_1)
    print (H_2)
    print (H_3)
    print (H_4)
    #Count into memory
    H_tuple1[binarytree(H_1)] += 1
    H_tuple2[binarytree(H_2)] += 1
    H_tuple3[binarytree(H_3)] += 1
    H_tuple4[binarytree(H_4)] += 1
print (H_tuple1)
print (H_tuple2)
print (H_tuple3)
print (H_tuple4)
H_open.close()

L_open = open(L_dataset)
for b in range(0, 199, 1):
    L_data = L_open.readline()
    #Strip off [ , ] and isolate
    step0 = L_data.split('[')
    step1 = step0[1]
    step2 = step1.split(']')
    step3 = step2[0]
    step4 = step3.split(', ')
    L_arr = []
    # Corresponding J sets
    L_1 = []
    L_2 = []
    L_3 = []
    L_4 = []
    for x in range(0, 12, 1):
        L_arr.append(step4[x])
    #Split into tuples
    for a in range(0, tuplesize, 1) :
        L_1.append(L_arr[placements[0][a]])
        L_2.append(L_arr[placements[1][a]])
        L_3.append(L_arr[placements[2][a]])
        L_4.append(L_arr[placements[3][a]])
    #Count into memory
    L_tuple1[binarytree(L_1)] += 1
    L_tuple2[binarytree(L_2)] += 1
    L_tuple3[binarytree(L_3)] += 1
    L_tuple4[binarytree(L_4)] += 1
print (L_tuple1)
print (L_tuple2)
print (L_tuple3)
print (L_tuple4)
L_open.close()

# TESTING
T_open = open("T_images.txt")
#numofTest = int(input("Enter an integer, greater than 1 but no bigger than 299"))
correct_hits = 0
total_hits = 0
#if numofTest < 1 or numofTest > 100:
#    print("invalid entry")
#    sys.exit()
# RUNNING
for e in range(0, 200, 1):
    total_hits += 1
    actual_class = ""
    predicted_class = ""
    flag = False
    # Split and isolate
    T_data = T_open.readline()
    step0 = T_data.split('[')
    step1 = step0[1]
    step2 = step1.split(']')
    step3 = step2[0]
    step4 = step3.split(', ')
    T_arr = []
    print(T_arr)
    # Corresponding J sets
    T_1 = []
    T_2 = []
    T_3 = []
    T_4 = []
    for x in range(0, 13, 1) :
        T_arr.append(step4[x])
    print(T_arr)
    if(T_arr[12] == 'H'):
        actual_class = "Actual Class: H"
    elif(T_arr[12] == 'L'):
        actual_class = "Actual Class: L"
    # Split into tuples
    for a in range(0, tuplesize, 1) :
        T_1.append(T_arr[placements[0][a]])
        T_2.append(T_arr[placements[1][a]])
        T_3.append(T_arr[placements[2][a]])
        T_4.append(T_arr[placements[3][a]])
    # Filter through binary tree and add up hits from H memory and L memory.
    L_hits = 0
    H_hits = 0
    L_hits += L_tuple1[binarytree(T_1)]
    L_hits += L_tuple2[binarytree(T_2)]
    L_hits += L_tuple3[binarytree(T_3)]
    L_hits += L_tuple4[binarytree(T_4)]
    H_hits += H_tuple1[binarytree(T_1)]
    H_hits += H_tuple2[binarytree(T_2)]
    H_hits += H_tuple3[binarytree(T_3)]
    H_hits += H_tuple4[binarytree(T_4)]
    if(H_hits > L_hits):
        predicted_class = "Predicted Class: H"
        if "H" in actual_class:
            flag = True
    elif(L_hits > H_hits):
        predicted_class = "Predicted Class: L"
        if "L" in actual_class:
            flag = True
    else:
        predicted_class = "Predicted Class: ?"
        flag = False
        # On the off-chance it's somehow equal or if an error occurs.
    print(str(H_hits)+" H hits")
    print(str(L_hits)+" L hits")
    output = [T_arr, actual_class, predicted_class, flag]
    print(output)
    if(flag):
        correct_hits += 1
    print(str(correct_hits/total_hits*100)+"% Accuracy")
T_open.close()