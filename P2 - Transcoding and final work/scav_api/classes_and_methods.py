import subprocess
import cv2
import numpy as np
import os
import json

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


### S2 – MPEG4 and more endpoints

# EXERCISE 1:
def video_resolution(input_path, output_path, resolution):
    ffmpeg_command = ["ffmpeg","-i", input_path, "-vf", f"scale={resolution}:-1", "-c:a", "copy", output_path]
    subprocess.run(ffmpeg_command)

# EXERCISE 2:
def chroma_subsampling(input_path, output_path, format):
    ffmpeg_command = ["ffmpeg", "-i", input_path, "-pix_fmt",format, output_path]
    subprocess.run(ffmpeg_command)

# EXERCISE 3:
def extract_rellevant_data(input_path):
    ffmpeg_command = ["ffmpeg", "-i", input_path]
    result = subprocess.run(ffmpeg_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    return result.stderr

# EXERCISE 4:
def extract_bbb(input_path, output_path):
    video_cut_path = "temp/BBBContainer/bbb_cut.mp4"
    aac_audio_path = "temp/BBBContainer/bbb_audio_aac.m4a"
    mp3_audio_path = "temp/BBBContainer/bbb_audio_mp3.mp3"
    ac3_audio_path = "temp/BBBContainer/bbb_audio_ac3.ac3"
    
    video_cut = ["ffmpeg", "-i", input_path, "-t", "20", "-c:v", "copy", "-c:a", "copy", video_cut_path]
    subprocess.run(video_cut)

    aac_mono_path =  ["ffmpeg", "-i", video_cut_path, "-vn", "-ac", "1", "-c:a", "aac", aac_audio_path]
    subprocess.run(aac_mono_path)

    mp3_path = ["ffmpeg", "-i", video_cut_path, "-vn", "-ac", "2", "-b:a", "128k", "-c:a", "mp3", mp3_audio_path]
    subprocess.run(mp3_path)

    ac3_path = ["ffmpeg", "-i", video_cut_path, "-vn", "-c:a", "ac3", ac3_audio_path]
    subprocess.run(ac3_path)

    ffmpeg_command = ["ffmpeg", "-i", video_cut_path,"-i", aac_audio_path, "-i", mp3_audio_path, "-i", ac3_audio_path,"-map", "0:v", "-map", "1:a", "-map", "2:a", "-map", "3:a","-c:v", "copy", "-c:a", "copy", output_path]
    subprocess.run(ffmpeg_command)

# EXERCISE 5:
def get_audio_tracks(input_path, output_path):
    ffmpeg_command = ["ffmpeg", "-i", input_path]
    result = subprocess.run(ffmpeg_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    
    output_lines = result.stderr.splitlines()
    audio_tracks = []

    for line in output_lines:
        if "Audio:" in line:
            parts = line.split(",")
            codec = parts[0].split("Audio:")[1].strip()

            audio_tracks.append({
                "codec": codec,
            })
    
    result_data = {"total_audio_tracks": len(audio_tracks), "audio_tracks": audio_tracks}
    
    with open(output_path, "w") as f:
        f.write(json.dumps(result_data, indent=4))
    
    return result_data

# EXERCISE 6:
def get_macroblocks_motionvectors(input_path, output_path):
    ffmpeg_command = ["ffmpeg","-flags2", "+export_mvs","-i", input_path,"-vf", "codecview=mv=pf+bf+bb",output_path]
    subprocess.run(ffmpeg_command)
    
# EXERCISE 7:
def get_yuv_histogram(input_path, output_path):
    ffmpeg_command = ["ffmpeg","-i", input_path,"-vf", "split=2[a][b],[b]histogram,format=yuva420p[hh],[a][hh]overlay",output_path]
    subprocess.run(ffmpeg_command)
    

### P2 - TRANSCODING AND FINAL WORK

def vp8_conversor(input_path, output_path):
    ffmpeg_command = ["ffmpeg", "-i", input_path, "-c:v", "libvpx", "-b:v", "1M", "-c:a", "libvorbis", output_path]
    subprocess.run(ffmpeg_command)
    
def vp9_conversor(input_path, output_path):
    ffmpeg_command = ["ffmpeg", "-i", input_path, "-c:v", "libvpx-vp9", "-b:v", "2M", "-c:a", "libopus", output_path]
    subprocess.run(ffmpeg_command)

def h265_conversor(input_path, output_path):
    ffmpeg_command = ["ffmpeg", "-i", input_path, "-c:v", "libx265", "-preset", "medium", "-b:v", "1M", "-c:a", "aac", output_path]
    subprocess.run(ffmpeg_command)
    
def av1_conversor(input_path, output_path):
    ffmpeg_command = ["ffmpeg", "-i", input_path, "-c:v", "libaom-av1", "-b:v", "2M", "-pass", "-2", "-c:a", "libopus", output_path]
    subprocess.run(ffmpeg_command)
