# S1 - JPEG, JPEG2000 and FFMPEG REPORT
## Introduction
This project contains a collection of Python utilities for performing various image processing and signal transformation tasks. It provides functions for color space conversion, image resizing, pixel serpentine pattern reading, RGB to BW transformation, run-lenght encoding method, and discrete signal transformations using DCT and DWT.
In order to create the tasks we should install some libraries as FFMPEG, NUMPY, SUBPROCESS and CV2.
For an easy execution and experimentation, we create a menu in order to execute each exercise individually and observe the results clearly.

In this report we will create a resume of how we create the different exercise and a review of the results obtained.

### Exercise 1: 
In this exercise we are asekd to install ffmpeg. To do so we followed the following [tutorial](https://es.wikihow.com/instalar-FFmpeg-en-Windows). Once installed, we obtain the following line: 

![image](https://github.com/user-attachments/assets/47c56109-5f6a-4b05-b819-8f2b56ffc344)


### Exercise 2:
This exercise is created in order to convert between RGB and YCbCr color spaces. For this, we create two different classes, one for convert RGB values to YUV values and the other for the inverse proces, from YUV to RGB values.
In order to create these transformations we apply the formulas according to each transformation.
First, from RGB to YUV:

![image](https://github.com/user-attachments/assets/f6b43927-46c0-4d9c-9784-eb29910b11b9)

And consequently, from YUV to RGB:

![image](https://github.com/user-attachments/assets/f7564eae-5236-4b52-a265-13509d512816)


### Exercise 3:
In this exercise we are asked to use the FFMPEG to resize images into lower quality ones. The FFMPEG command created is the following:

"ffmpeg", "-i", input_path, "-vf", f"scale={width}:-1", "-q:v", str(quality), output_path

First, the -i followed by the input_path specifies the input image file, then the `-vf, f"scale={width}:-1"` resizes the image to a resolution of a width introduced by the user and the -1 tells ffmpeg to automatically adjust the height to maintain the aspect ratio.
Finally, the `"-q:v", str(quality)` asks the user to set the quality level for thhe output image. The scale ranges from 2 (high quality) to 31 (lowest quality).

To try the command we are going to use the next image, and the subprocess function run in order to run the FFMPEG command.

![image](https://github.com/user-attachments/assets/a124ffa3-5213-4057-be45-68a20a666aab)


After the command execution, the user should provide the width and the quality of the resized image. For a width of 640 and a quality value of 30, we obtain the next resized image:

![image](https://github.com/user-attachments/assets/58e0b380-a7fb-4f31-8964-141ea4240430)


### Exercise 4: 
In this exercise we are asekd to create a method called serpentine. To do so we followed the image given in theory: 

![image](https://github.com/user-attachments/assets/4d7fd3b8-1c99-4969-916f-5dd5efe3c210)


By looking at the image we realised that the diagonals go from right to left and left to right once every time, that is to say, the first diagonal goes from right to lef, the second from left to right, the third from right to left... So our code creates an array and it appends the pixels read the way we mentioned before. To do so we first append the first pixel of the image, then we create two loops, one to read the diagonals from right to left and the other from left to right. To read the diagonals from left to right, we declare as the starting points the row as its mínimum value (0) and the máximum value for column (width), and then we iterate until row reaches its maximum value (height) or the column reach its minimum value (0). In the loop, we simply append the pixel in the each position in which the loop is. The loop for reading from right to left we follow the same process, but we declare the columns as 0 and the rows as its maximum value (height). Finally, we simply return the array with the serpentine pixels.


### Exercise 5:
Again, in this exercise, we are asked to use the FFMPEG to convert an RGB image into a BW one, doing the hardest compression we can, that is, with the lower quality available. The FFMPEG command created is the following:

"ffmpeg", "-i", input_path, "-vf", "hue=s=0", "-q:v", "31", output_path

First, as in the previous exercise, the -i followed by the input_path specifies the input image file, then the `"-vf", "hue=s=0"` in order to change the RGB image to BW image, because the hue and the saturation are stablished to 0. On the other hand, the `"-q:v", "31"`, as we saw in the previous exercise, this part of the command is used to modify the quality of the image, as we want to do the hardest compression, we should apply the high value that is 31.

As well as the previous exercise, the input image used is the next:

![image](https://github.com/user-attachments/assets/f4bbf712-01ba-4a10-8a05-dd98dd9cdb73)

And after executing the command using the function run of the subprocess library, we obtain the next BW image with the hardest compression,

![image](https://github.com/user-attachments/assets/79be12e5-1b53-41f4-a53b-459ee806b2a7)


### Exercise 6:
In this exercise we create a method that applies run-length encoding, a common method to compress even more a file. To do this method we create an array in which we will append the bytes. Then we create a variable  with the first value of the input and we initialize a counter. Then we iterate through the input data, and if two or more consecutive bytes are equal, we count the number of equal consecutive bytes and we append it to the signal together with the value of the byte itslef. Then we declare the next byte as the byte with which we will be comparing and we start the process again until we have read all the input data.


### Exercise 7:
In this exercise we are asked to create a class which can encode and decode an input using the Discrete Cosine Transform (DCT). The class is structured in 3 methods, one for the normalization constants (alpha), the encoder function using DCT (dct_encoder) and the decoder function using DCT (dct_decoder).
Therefore, in order to create the encoder we should apply the DCT formula seen in class. As the formula have two unknown variables (x, y) and is a 2 dimension formula (u, v), we create 4 for's in order to iterate through all the values of the function. After that, we multiply the previous result by the normalization constants depending on the size of the input signal.
For the decoder function we apply the inverse process, that is change the order of the for's considering the u and v as the unknown variables.

The results obtained are almost correct, after encode and decode the input signal, we observe that the recovered signal have some differences compared with the input, but only with few values.


### Exercise 8 
In this exercise we are asked to create a DWT encoder. To do so we applied the first level of the transfrom, as it is the most straight forward method. To do this we first create a low-pass and high-pass filters, which are related to each other and they are known quadrature filters. Then, we apply the both filters to the input signal using convolution and then we downsample by a factor of 2 the results of both convolutions. The downsampled result of the convolution of the signal with the low-pass filter gives us the aproximation coefficients, and the downsampled result of the convolution of the signal with the high-pass filter gives us the detail coefficients. These coefficients is what we return in this method. 
We are not sure if this function works correctly, but we did not know how to make it work correctly.


## Unit Tests
To create tests to see if our functions work correclty, we created an interactive menu that asks the user which exercise wants to execute, and each exercise has an example to see how the code works. Exercise 2 and 3 also have interaction with the user in the exercise itself. In the 2nd exercise we ask the user the RGB values that he or she wants to transfrom, and the same with the Y Cb Cr values. And in the 3rd exercise, we ask the user to enter the width of the resized image and the quality of the resized image. 
By doing these unit test we can see that most of our code works correctly. However, we are not sure if the exercise 4 works correctly as it prints an extremly large quantity of pixels and we are not able to see if these are printed the serpentine way. We compared by printing 50 pixels of the image printed normal and 50 printed in the serpentine way and we see that these are different, but we can not affirm that it Works correctly. Also, in exercise 7 we see some losses in the decoder, as the input given to the encoder, is not equal to the output of the encoder. Finally, as we mentioned before, we are not sure if the code in exercise 8 is correct.
