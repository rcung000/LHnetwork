# LHnetwork
A neural network to recognize L and H letters.

# Generating the Training Set
We need to generate the training set.
300 of each letter L & H, resulting in 600 altogether. 400 of which will be used as the training set, and 200 will be used as the testing set.
# Sample Images that we will change with noise.
```
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
sample_image_L3 = \
    [0, 1, 0,
     0, 1, 0,
     0, 1, 0,
     0, 1, 0]
sample_image_L4 = \
    [0, 1, 0,
     0, 1, 0,
     0, 1, 0,
     0, 1, 1]
sample_image_L5 = \
    [0, 0, 0,
     0, 0, 0,
     1, 0, 0,
     1, 1, 0]
```
ArrayGenerator will write out the arrays to it's respective txt file.
See the below sample output:
```
Enter L or H: H
1   0   1
1   0   1
0   1   1
1   0   1
Is this valid? Y/N: y
```
H_images.txt:
```
[1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1]
```
# LHnetwork
Reads through L_images and H_images and stores it into memory.

Reads through a 3rd text file T_images with a mix of H and L images
Sample Return:
```
532 H hits
94 L hits
[['1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '0', '1', 'H'], 'Actual Class: H', 'Predicted Class: H', True]
93.0% Accuracy

Process finished with exit code 0
```

# How to use
Run ArrayGenerator if you'd like to use your own arrays. (Remember to delete H_images.txt, L_images.txt)
Select 200 to put into T_images.txt
Run LHnetwork and it'll run as long as you have H_images.txt, L_images.txt, and T_images.txt in the same directory.
