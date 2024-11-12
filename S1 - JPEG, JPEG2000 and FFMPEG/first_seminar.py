from classes_and_methods import RGB, YCbCr, DCT, DWT, resize_image, bw_image, run_lenght_encoding, serpentine
import numpy as np

# EXERCISE 2: Creation of translator from 3 values in RGB into the 3 YUV values, plus the opposite operation
def ex2():
    # RGB to YCbCr
    YcrCb1 = RGB.RGB_to_YCbCr()
    print("The (R, G, B) selected are converted into: ", YcrCb1, "(Y, Cb, Cr) values")

    # YCbCr to RGB
    RGB1 = YCbCr.YCbCr_to_RGB()
    print("The (Y, Cb, Cr) selected are converted into: ", RGB1, "(R, G, B) values")


# EXERCISE 3: Creation of a FFMPEG command to resize image into lower quality
def ex3():
    w = int(input("Enter the width of the resized image: "))
    q = int(input("Enter the quality of the resized image: "))
    resize_image("Input images/input.jpg", "Output images/output_ex3.jpg", w, q)

# EXERCISE 4: Creation of the serpentine method to read the pixels
def ex4():
    read_pixels = serpentine("Input images/input.jpg")
    print(read_pixels[:50])
    #print(read_pixels)

# EXERCISE 5: Creation of a FFMPEG command to convert an RGB image into BW.
def ex5():
    bw_image("Input images/input.jpg", "Output images/output_ex5.jpg")

# EXERCISE 6: Creation of the run lenght encoding method
def ex6():
    data = bytes(([1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 5, 5, 5, 6, 7, 7]))
    print("The encoded data is: ", run_lenght_encoding(data))

# EXERCISE 7: 
def ex7():
    input_signal = np.array([[1, 2, 3, 4],[1, 5, 7, 8]])
    encoded_signal = DCT.dct_encoder(input_signal)
    print("Our encoded signal: ", encoded_signal)

# EXERCISE 8:
def ex8():
    input_signal = np.array([1, 2, 3])
    aprox_coef, detail_coef = DWT.encode_dwt(input_signal)
    print("Our approximation coefficients are: ", aprox_coef)
    print("Our detail coefficients are: ", detail_coef)
    
def menu():
    print("\nExercises menu:")
    print("1 - Exercise 2")
    print("2 - Exercise 3")
    print("3 - Exercise 4")
    print("4 - Exercise 5")
    print("5 - Exercise 6")
    print("6 . Exercise 7")
    print("7 - Exercise 8")
    print("0 - Exit")

while True:
    menu()
    option = input("Select an option: ")
    
    if(option == '1'):
        ex2()
        
    elif(option == '2'):
        ex3()
    
    elif(option == '3'):
        ex4()
    
    elif(option == '4'):
        ex5()
    
    elif(option == '5'):
        ex6()
    
    elif(option == '6'):
        ex7()

    elif(option == '7'):
        ex8()
    
    elif(option == '0'):
        break
    else:
        print("Invalid option. Try again.")