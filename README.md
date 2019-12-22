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
```
We will randomly change it with noise in 2 or 3 locations. (See ArrayGenerator.py)
