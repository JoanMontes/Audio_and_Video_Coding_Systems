import ffmpeg
from classes_and_methods import RGB, YCbCr

# EXERCISE 2: Creation of translator from 3 values in RGB into the 3 YUV values, plus the opposite operation
# RGB to YCbCr
YcrCb1 = RGB.RGB_to_YCbCr()
print("The (R, G, B) selected are converted into: ", YcrCb1, "(Y, Cb, Cr) values")

# YCbCr to RGB
RGB1 = YCbCr.YCbCr_to_RGB()
print("The (Y, Cb, Cr) selected are converted into: ", RGB1, "(R, G, B) values")


# EXERCISE 3: 



