import random
sample_image_H0 = \
    [1, 0, 1,
     1, 1, 1,
     1, 0, 1,
     1, 0, 1]
sample_image_H1 = \
    [1, 0, 1,
     1, 1, 1,
     1, 1, 1,
     1, 0, 1]
sample_image_H2 = \
    [1, 0, 1,
     1, 0, 1,
     1, 1, 1,
     1, 0, 1]
sample_image_L0 = \
    [1, 0, 0,
     1, 0, 0,
     1, 0, 0,
     1, 1, 1]
sample_image_L1 = \
    [1, 0, 0,
     1, 0, 0,
     1, 0, 0,
     1, 1, 0]
sample_image_L2 = \
    [0, 0, 0,
     1, 0, 0,
     1, 0, 0,
     1, 1, 0]
sample_image_H_List = [sample_image_H0, sample_image_H1, sample_image_H2]
sample_image_L_List = [sample_image_L0, sample_image_L1, sample_image_L2]
# seeding
random.seed()
# noisyarray
def noisyarray(geneImage,letter):
    # generating noise in 2-3 spots
    noise2 = [random.randint(0, 11), random.randint(0, 11)]
    # noise3 = [random.randint(0, 11), random.randint(0, 11), random.randint(0, 11)]
    for x in noise2:
        if geneImage[x] == 0:
            geneImage[x] = 1
        else:
            geneImage[x] = 0
    if (letter == 'L') :
        imagefile = open("L_images.txt", "a+")
    elif (letter == 'H') :
        imagefile = open("H_images.txt", "a+")
    for x in range(0, 12, 3):
        print(geneImage[x], " ", geneImage[x + 1], " ", geneImage[x + 2])
    confirm = str(input("Is this valid? Y/N: "))
    if confirm == 'Y' or confirm == 'y' :
        #formats it into image (only use for testing)
        #imagefile.write("=====\n")
        #for z in range(0, 12, 3):
        #    imageline = "" + str(geneImage[z]) + " " + str(geneImage[z + 1]) + " " + str(geneImage[z + 2]) + "\n"
        #    imagefile.writelines(imageline)
        imagefile.writelines("[" + str(geneImage[0]) + ", " + str(geneImage[1]) + ", " + str(geneImage[2]) + ", "
                             + str(geneImage[3]) + ", " + str(geneImage[4]) + ", " + str(geneImage[5]) + ", "
                             + str(geneImage[6]) + ", " + str(geneImage[7]) + ", " + str(geneImage[8]) + ", "
                             + str(geneImage[9]) + ", " + str(geneImage[10]) + ", " + str(geneImage[11]) + "]")
    imagefile.close()



# image selection
imageinput = str(input("Enter L or H: "))
selected_image = []
if imageinput == 'L' or imageinput == 'l' :
    noisyarray(sample_image_L_List[random.randint(0, 2)], "L")
elif imageinput == 'H' or imageinput == 'h' :
    noisyarray(sample_image_H_List[random.randint(0, 2)], "H")