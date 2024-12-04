from fastapi import FastAPI, HTTPException, UploadFile, File
from classes_and_methods import RGB, YCbCr, DCT, DWT, resize_image, bw_image, run_lenght_encoding, serpentine, video_resolution, chroma_subsampling, extract_rellevant_data, extract_bbb, get_audio_tracks, get_macroblocks_motionvectors, get_yuv_histogram, video_conversor, encoding_ladder
import numpy as np
import shutil
import os

app = FastAPI()

# Helper function to save uploaded files
def save_uploaded_file(file: UploadFile, destination: str):
    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return destination

@app.get("/")
def read_root():
    return {"message": "Welcome to the SCAV API!"}

# Exercise 2: RGB to YCbCr and vice versa
@app.post("/exercise2/rgb-to-ycbcr/")
def rgb_to_ycbcr(r: float, g: float, b: float):
    Y = 0.257 * r + 0.504 * g + 0.098 * b + 16
    Cb = -0.148 * r - 0.291 * g + 0.439 * b + 128
    Cr = 0.439 * r - 0.368 * g - 0.071 * b + 128
    return {"Y": Y, "Cb": Cb, "Cr": Cr}

@app.post("/exercise2/ycbcr-to-rgb/")
def ycbcr_to_rgb(y: float, cb: float, cr: float):
    R = 1.164 * (y - 16) + 1.596 * (cr - 128)
    G = 1.164 * (y - 16) - 0.813 * (cr - 128) - 0.391 * (cb - 128)
    B = 1.164 * (y - 16) + 2.018 * (cb - 128)
    return {"R": R, "G": G, "B": B}

# Exercise 3: Resize image
@app.post("/exercise3/resize/")
def resize(input_file: UploadFile = File(...), width: int = 100, quality: int = 2):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/resized_{input_file.filename}"
    os.makedirs("temp", exist_ok=True)
    save_uploaded_file(input_file, input_path)

    try:
        resize_image(input_path, output_path, width, quality)
        return {"message": "Image resized successfully", "output_path": output_path}
    finally:
        os.remove(input_path)

# Exercise 5: Convert image to black and white
@app.post("/exercise5/bw/")
def bw_convert(input_file: UploadFile = File(...)):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/bw_{input_file.filename}"
    save_uploaded_file(input_file, input_path)
    try:
        bw_image(input_path, output_path)
        return {"message": "Image converted to BW", "output_path": output_path}
    finally:
        os.remove(input_path)

# Exercise 6: Run-length encoding
@app.post("/exercise6/rle/")
def run_length(data: str):
    bytes_data = bytes([int(i) for i in data.split(",")])
    encoded = run_lenght_encoding(bytes_data)
    return {"encoded_data": encoded}



### S2 – MPEG4 and more endpoints
# Exercise 1:
@app.post("/Change video resolution/")
def resolution(input_file: UploadFile = File(...), resolution: int = 100):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/rescaled_{input_file.filename}"
    os.makedirs("temp", exist_ok=True)
    save_uploaded_file(input_file, input_path)
    try:
        video_resolution(input_path, output_path, resolution)
        
    finally:
        os.remove(input_path)

# Exercise 2:
@app.post("/Change video chroma subsampling/")
def chroma_sub(input_file: UploadFile = File(...), format: str = "yuv444p"):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/chroma_subsampled_{input_file.filename}"
    os.makedirs("temp", exist_ok=True)
    save_uploaded_file(input_file, input_path)
    try:
        chroma_subsampling(input_path, output_path, format)
        
    finally:
        os.remove(input_path)

# Exercise 3:
@app.post("/Extract video information/")
def rellevant_data(input_file: UploadFile = File(...)):
    input_path = f"temp/{input_file.filename}"
    save_uploaded_file(input_file, input_path)
    try:
        metadata = extract_rellevant_data(input_path)
        metadata_file_path = f"temp/{os.path.splitext(input_file.filename)[0]}_metadata.txt"
        with open(metadata_file_path, "w") as metadata_file:
            metadata_file.write(metadata)
    
    finally:
        os.remove(input_path)

# Exercise 4:
@app.post("/BBB Container/")
def bbb_container(input_file: UploadFile = File(...)):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/container_output_{input_file.filename}"
    save_uploaded_file(input_file, input_path)
    try:
        extract_bbb(input_path, output_path)
        
    finally:
        os.remove(input_path)       

# Exercise 5:
@app.post("/Extract audio tracks/")
def audio_tracks(input_file: UploadFile = File(...)):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/{input_file.filename}_audio_tracks.txt"
    save_uploaded_file(input_file, input_path)
    try:
        data = get_audio_tracks(input_path, output_path)
        
    finally:
        os.remove(input_path)

# Exercise 6:
@app.post("/Generate video with macroblocks and motion vectors/")
def macroblocks_motionvectors_video(input_file: UploadFile = File(...)):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/macroblocks_motionvectors_video.mp4"
    save_uploaded_file(input_file, input_path)
    try:
        get_macroblocks_motionvectors(input_path, output_path)
        
    finally:
        os.remove(input_path)
        
# Exercise 7:
@app.post("/Generate video with YUV histogram overlayed/")
def yuv_histogram_video(input_file: UploadFile = File(...)):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/yuv_histogram_video.mp4"
    save_uploaded_file(input_file, input_path)
    try:
        get_yuv_histogram(input_path, output_path)
        
    finally:
        os.remove(input_path)
        


### P2 - TRANSCODING AND FINAL WORK
# Exercise 1:
@app.post("/Compress video with VP8, VP9, H265 and AV1/")
def compressed_videos(input_file: UploadFile = File(...)):
    input_path = f"temp/{input_file.filename}"
    save_uploaded_file(input_file, input_path)
    try:
        video_conversor(input_path)
        
    finally:
        os.remove(input_path)

# Exercise 2:
@app.post("/Encoding Ladder/")
def encoding_ladder_endpoint(input_file: UploadFile = File(...), ladder: int=0):
    input_path = f"temp/{input_file.filename}"
    output_path = f"temp/encoding_ladder.mp4"
    save_uploaded_file(input_file, input_path)
    try:
        encoding_ladder(input_path, output_path, ladder)
        
    finally:
        os.remove(input_path)