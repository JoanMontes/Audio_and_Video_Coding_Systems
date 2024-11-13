import subprocess
import cv2
import numpy as np

# EXERCISE 2: Creation of translator from 3 values in RGB into the 3 YUV values, plus the opposite operation
class RGB:

    def __init__(self, R, G, B): #Class Constructor
        self.R = R
        self.G = G
        self.B = B
    @classmethod
    def RGB_to_YCbCr(cls):
        #User defines R,G,B values
        R = float(input("Choose R value: ")) 
        G = float(input("Choose G value: "))
        B = float(input("Choose B value: "))
        #Apply transformation
        Y = 0.257*R + 0.504*G + 0.098*B + 16
        Cb = -0.148*R - 0.291*G + 0.439*B + 128
        Cr = 0.439*R - 0.368*G - 0.071*B + 128
        return Y, Cb, Cr
    
    
class YCbCr: 

    def __init__(self, Y, Cb, Cr):
        self.Y = Y
        self.Cb = Cb
        self.Cr = Cr
    
    @classmethod
    def YCbCr_to_RGB(cls):
        #User defines Y, Cb, Cr values
        Y = float(input("Choose Y value: "))
        Cb = float(input("Choose Cb value: "))
        Cr = float(input("Choose Cr value: "))
        #Apply transformation
        R = 1.164*(Y - 16) + 1.596*(Cb-128)
        G = 1.164*(Y-16) - 0.813*(Cr - 128) - 0.391*(Cb - 128)
        B = 1.164*(Y-16) + 2.018*(Cb - 128)
        return R, G, B


# EXERCISE 3: Creation of a FFMPEG command to resize image into lower quality
def resize_image(input_path, output_path, width, quality):
    #FFMPEG command creation loading some input image, scaling its width 
    #(because the -1 tells ffmpeg to automatically adjust the height to maintain the aspect ratio)
    # and ajusting the quality of the image.
    subprocess.run(["ffmpeg", "-i", input_path, "-vf", f"scale={width}:-1", "-q:v", str(quality), output_path])


# EXERCISE 4: Creation of the serpentine method to read the pixels
def serpentine(image_path):
    #load the image using OpenCV
    image = cv2.imread(image_path,0)
    height, width = image.shape
    
    serpentine_pixels = []

    #We append the pixels in the diagonals from left to right and right to left changing the direction in each diagonal
    #As we iterate through diagonals, we iterate until the max diagonal is reached
    for i in range(width + height - 1):
            #Left to right diagonals
            if i % 2 == 0:
                #We declare the starting points
                col = min(i, width - 1)
                row = i - col
                #We iterate until the boundaries of the image are reached
                while row < height and col >= 0:
                    serpentine_pixels.append(image[row, col])
                    row += 1
                    col -= 1
            #Right to left diagonals
            else:
                #We declare the starting points
                row = min(i, height - 1)
                col = i - row
                #We iterate until the boundaries of the image are reached
                while row >= 0 and col < width:
                    serpentine_pixels.append(image[row, col])
                    row -= 1
                    col += 1
        

    return serpentine_pixels


# EXERCISE 5: Creation of a FFMPEG command to convert an RGB image into BW.
def bw_image(input_path, output_path):
    #This command is modifying an RGB image into BW because the addition of "hue=s=0" to the command,
    #also, the statement says that we should made the hardest compression we can, the "-q:v" "31",
    #applies the lowest quality, yielding maximum compression
    subprocess.run(["ffmpeg", "-i", input_path, "-vf", "hue=s=0", "-q:v", "31", output_path])
    

# EXERCISE 6: Creation of the run lenght encoding method
def run_lenght_encoding(data):
    encoded_data = [] # We create an empty array that will be the output of the function
    first_byte = data[0] # Assign to a variable the first value of the data array
    count = 0 # Initialize a counter
    
    for i in data: # Iterate through all the data values
        if i == first_byte: # Following the run lenght encoding method, if two consecutive bytes are equal, we will count the number of equal consecutive bytes 
            count += 1
        
        else: # If the consecutive bytes are different, we add to the encoded data the byte and the number of consecutive bytes, and pas to the other byte
            encoded_data.append((first_byte, count))
            first_byte = i
            count = 1
    

    encoded_data.append((first_byte, count)) # Adding the last byte and the number of entities existing in the array of this byte
    
    return encoded_data        


# EXERCISE 7: Creation of a encoder and decoder using the DCT
class DCT:

    def __init__(self):
        pass
    
    def alpha(p, len):
        if p == 0:
             return np.sqrt(1/len)
        else:
            return np.sqrt(2/len)
      
    def dct_encoder(input_signal):
        N = len(input_signal)
        result = np.zeros_like(input_signal)
    
        for u in range(N):
            for v in range(N):
                sum = 0
                for x in range(N):
                    for y in range(N):
                        sum += input_signal[x, y] * np.cos((np.pi/N) * (x + 1/2) * u) * np.cos((np.pi/N) * (y + 1/2) * v)
                
                result[u, v] = DCT.alpha(u, N) * DCT.alpha(v, N) * sum
        
        return result
    
    def dct_decoder(encoded_signal):
        N = len(encoded_signal)
        result = np.zeros_like(encoded_signal)
        
        for x in range(N):
            for y in range(N):
                sum = 0
                for u in range(N):
                    for v in range(N):
                        sum += DCT.alpha(u, N) * DCT.alpha(v, N) * encoded_signal[u, v] * np.cos((np.pi/N) * (x + 1/2) * u) * np.cos((np.pi/N) * (y + 1/2) * v)
                        
                result[x, y] = sum
                
        return result


# EXERCISE 8: Creation of a encoder and decoder using DWT
class DWT:
    def __init__(self):
        pass
    
    #We use the first level of the transfrom
    def encode_dwt(input_signal):
        #We declare the low-pass and high-pass filter (quadrature filters)
        lp = [np.pi/2, np.pi/2]
        hp = [np.pi/2, -np.pi/2]
        #We convolve the signal with the filters
        ylow = np.convolve(input_signal, lp)
        yhigh = np.convolve(input_signal, hp)
        #We downsample the outputs
        aprox_coef = ylow[::2]
        detail_coef = yhigh[::2]

        return aprox_coef, detail_coef    