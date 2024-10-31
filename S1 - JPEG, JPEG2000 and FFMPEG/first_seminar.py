import ffmpeg

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
       
YcrCb1 = RGB.RGB_to_YCbCr()
print(YcrCb1)

RGB1 = YCbCr.YCbCr_to_RGB()
print(RGB1)







