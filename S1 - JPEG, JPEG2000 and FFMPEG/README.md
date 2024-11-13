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


By looking at the image we realised that the diagonals go from right to left and left to right once every time, that is to say, the first diagonal goes from right to lef, the second from left to right, the third from right to left... So our code creates an array and it appends the pixels read the way we mentioned before. To do so we first append the first pixel of the image, then we create two loops, one to read the diagonals from right to left and the other from left to right. To read the diagonals from left to right, we declare as the starting points the column as its minimum between the iteration and the width.  and the iteration minus the column for the rows. Then we iterate until row reaches its maximum value (height) or the column reach its minimum value (0). In the loop, we simply append the pixel in the each position in which the loop is. The loop for reading from right to left we follow the same process, but we declare the columns as we declared the rows previously and the rows the way we declared the columns. Finally, we simply return the array with the serpentine pixels.


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
To ensure that each individual method and classes of the code work correctly we use Artificial Inteligence (CHATGPT) to create different Unit Tests. These tests are crucial for validating the behaviour of our code, we use controlled inputs and known expected outputs in order to validate the code.

For the first exercise, a class called `TestColorConversion` has been created to verify the accuracy of color conversion. Specifically, we obtained two tests, one for the RGB to YCbCr and the other for the YCbCr to RGB. In the first test the AI simulates an user input for RGB values and compares the output Y, Cb, and Cr components agains expected values calculated using the RGB to YCbCr conversion formula.

The second text makes the same simulation but comparing the resulting RGB values to the expected values derived from the YCbCr to RGB.

For the second exercise, a class called `TestResizeImage` has been created to verify that the `resize_image` function correctly calls the ffmpeg command. 

For the third exercise, a class called `TestSerpentineFunction` has been created to verify the correct functionality of the `serpentine` function. The AI create a 3x3 matrix used as input for the function. The test defines an expected output for a 3x3 image processed in serpentine order, which involves traversing the image in a zigzag pattern across diagonals. Then, the test asserts that the actual output from the `serpentine` function matches the expected result, ensuring that the gunction processes the image correctly.

The purpose of the unit test `TestBWImageFunction` is to verify that the `bw_image`function correctly calls the ffmpeg command to convert a color image to a black and white image. 

For the next exercise, the unit test `TestRunLengthEncoding` is used to verify the correct functionality of the `run_length_encoding` function, which encodes a list of values by compressing consecutive identival values into a tuple.
In this unit test the AI creates four different tests. The `test_basic_encoding` creates a general case with mixed values in the input list, and checks if the function correctly encodes the input into this expected format. The `test_single_values` test when the input list consists of a single repeating calue, and checks if the function handles sequences with only one unique value correctly.
The `test_alternating_values` tests a sequence of alternating values, and check if the function handles alternating values correctly. And finally `test_large_sequence` create a large sequence of identical values (a list of 100 occurrences of the value 4), this test ensures that the function can handle larger input sequences and produce the correct encoding.

The purpose of the unit test `TestDCT` is to verify the correct functionality of the DCT encoder and decoder in the `DCT` module.
In this unit test the AI creates three different tests. The `test_dct_inverse`checks the correctness of the DCT encoding and decoding process by ensuring that the original input signal is approximately recovered after encoding and decoding, generates a random 4x4 matrix as the input signal and applies the `dct_encoder` to encode the signal and the `dct_decoder` to decode it. And finally the test asserts that the decoded signal is very close to the original signal.
The `test_dct_zero_input` checks how the DCT encoder and decoder handle an input signal that is all zeros.
And the `test_output_shape` verifies that the shapes of the encoded and decoded signals match the shape of the input signal, ensuring that the DCT operations preserve the dimensionality of the input signal.

Finally, the purpose of the unit test `TestDWT` is to verify the correct functionality of the DWT encoder. In this unit test the AI creates four different tests. The `test_dwt_known_signal` validates correct calculations for a simple, known input, ensuring the transform logic is accurate. The `test_dwt_zero_input` confirms that the function can handle an all-zero input without introducing artifacts. The `test_dwt_single_value` tests boundary behavious for minimal input, ensuring robustness with edge cases. Finally, the `test_output_length` ensures the function correctly downscales the output length, confirming the accuracy of the downsampling process.

After the execution of the tests, we can observe that all the results obtained with the checks are correct.


## Menu Integration
We created an interactive menu that asks the user which exercise wants to execute, and each exercise has an example to see how the code works. Exercise 2 and 3 also have interaction with the user in the exercise itself. In the 2nd exercise we ask the user the RGB values that he or she wants to transfrom, and the same with the Y Cb Cr values. And in the 3rd exercise, we ask the user to enter the width of the resized image and the quality of the resized image. This integration gives a more user-friendly experience to execute the exercises.
