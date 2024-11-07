import subprocess

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


def resize_image(input_path, output_path, width, quality):
    #FFMPEG command creation loading some input image, scaling its width 
    #(because the -1 tells ffmpeg to automatically adjust the height to maintain the aspect ratio)
    # and ajusting the quality of the image.
    subprocess.run(["ffmpeg", "-i", input_path, "-vf", f"scale={width}:-1", "-q:v", str(quality), output_path])


def bw_image(input_path, output_path):
    subprocess.run(["ffmpeg", "-i", input_path, "-vf", "hue=s=0", "-q:v", "31", output_path])
    

def run_lenght_encoding(data):
    
    encoded_data = []
    first_byte = data[0]
    count = 0
    
    for i in data:
        if i == first_byte:
            count += 1
        
        else:
            encoded_data.append((first_byte, count))
            first_byte = i
            count = 1
    

    encoded_data.append((first_byte, count))
    
    return encoded_data        