# S1 - JPEG, JPEG2000 and FFMPEG REPORT
## Introduction
This project contains a collection of Python utilities for performing various image processing and signal transformation tasks. It provides functions for color space conversion, image resizing, pixel serpentine pattern reading, RGB to BW transformation, run-lenght encoding method, and discrete signal transformations using DCT and DWT.
In order to create the tasks we should install some libraries as FFMPEG, NUMPY, SUBPROCESS and CV2.
For an easy execution and experimentation, we create a menu in order to execute each exercise individually and observe the results clearly.

In this report we will create a resume of how we create the different exercise and a review of the results obtained.

### Exercise 1:
This exercise is created in order to convert between RGB and YCbCr color spaces. For this, we create two different classes, one for convert RGB values to YUV values and the other for the inverse proces, from YUV to RGB values.
In order to create these transformations we apply the formulas according to each transformation.
First, from RGB to YUV:
![image](![image](https://github.com/user-attachments/assets/345f0ac0-1680-4d65-8362-bb671af7494f))

And consequently, from YUV to RGB:
![image](https://github.com/user-attachments/assets/f7564eae-5236-4b52-a265-13509d512816)



### Exercise 2:

