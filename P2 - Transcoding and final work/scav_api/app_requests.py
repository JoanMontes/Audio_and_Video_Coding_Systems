from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

FASTAPI_URL = "http://127.0.0.1:8000"  # FastAPI backend URL

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")


# Exercise 2: RGB to YCbCr and vice versa
@app.route("/exercise2/rgb-to-ycbcr/", methods=["GET", "POST"])
def rgb_to_ycbcr():
    if request.method == "POST":
        r = float(request.form["r"])
        g = float(request.form["g"])
        b = float(request.form["b"])

        response = requests.post(f"{FASTAPI_URL}/exercise2/rgb-to-ycbcr/", params={"r": r, "g": g, "b": b})

        if response.status_code == 200:
            result = response.json()
            
            formatted_result = {
                "Luminance (Y)": f"{result['Y']:.2f}",
                "Blue-Difference Chroma (Cb)": f"{result['Cb']:.2f}",
                "Red-Difference Chroma (Cr)": f"{result['Cr']:.2f}",
            }
            return jsonify(formatted_result)
        else:
            return f"Error: {response.status_code}", 500

    return render_template("rgb_to_ycbcr.html")


@app.route("/exercise2/ycbcr-to-rgb/", methods=["GET", "POST"])
def ycbcr_to_rgb():
    if request.method == "POST":
        y = float(request.form["y"])
        cb = float(request.form["cb"])
        cr = float(request.form["cr"])

        response = requests.post(f"{FASTAPI_URL}/exercise2/ycbcr-to-rgb/", params={"y": y, "cb": cb, "cr": cr})

        if response.status_code == 200:
            result = response.json()
            
            formatted_result = {
                "Red (R)": f"{result['R']:.2f}",
                "Green (G)": f"{result['G']:.2f}",
                "Blue (B)": f"{result['B']:.2f}",
            }
            return jsonify(formatted_result)
        else:
            return f"Error: {response.status_code}", 500
    return render_template("ycbcr_to_rgb.html")


# Exercise 3: Resize image
@app.route("/exercise3/resize/", methods=["GET", "POST"])
def resize_image():
    if request.method == "POST":
        width = int(request.form["width"])
        quality = int(request.form["quality"])

        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            data = {"width": width, "quality": quality}
            response = requests.post(f"{FASTAPI_URL}/exercise3/resize/", files=files, data=data)

        if response.status_code == 200:
            result = response.json()
            resized_path = result.get("output_path")

            return jsonify({"message": "Image resized successfully", "resized_path": resized_path})
        else:
            return jsonify({"error": f"Failed to resize image: {response.status_code}"}), 500

    return render_template("resize.html")


# Exercise 5: Convert image to black and white
@app.route("/exercise5/bw/", methods=["GET", "POST"])
def bw_convert():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            response = requests.post(f"{FASTAPI_URL}/exercise5/bw/", files=files)

        if response.status_code == 200:
            result = response.json()
            bw_path = result.get("output_path")

            return jsonify({"message": "Image converted to BW successfully", "bw_path": bw_path})
        else:
            return jsonify({"error": f"Failed to convert image: {response.status_code}"}), 500

    return render_template("bw.html")


# Exercise 6: Run-length encoding
@app.route("/exercise6/rle/", methods=["GET", "POST"])
def run_length_view():
    if request.method == "POST":
        data = str(request.form["data"])
        response = requests.post(f"{FASTAPI_URL}/exercise6/rle/", data={"data": data})

        if response.status_code == 200:
            result = response.json()
            encoded_data = result.get("encoded_data")

            return jsonify({"message": "Run-length encoding successful", "encoded_data": encoded_data})
        else:
            return jsonify({"error": f"Failed to encode data: {response.status_code}"}), 500

    return render_template("run_length.html")


# Exercise 7: Video Resolution
@app.route("/exercise7/video-resolution/", methods=["GET", "POST"])
def change_video_resolution():
    if request.method == "POST":
        resolution = int(request.form["resolution"])

        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            data = {"resolution": resolution}
            response = requests.post(f"{FASTAPI_URL}/Change video resolution/", files=files, data=data)

        if response.status_code == 200:
            result = response.json()
            rescaled_video_path = result.get("output_path")

            return jsonify({"message": "Video resolution changed successfully", "rescaled_video_path": rescaled_video_path})
        else:
            return jsonify({"error": f"Failed to change video resolution: {response.status_code}"}), 500

    return render_template("video_resolution.html")


# Exercise 8: Chroma Subsampling
@app.route("/exercise8/chroma-subsampling/", methods=["GET", "POST"])
def chroma_subsampling():
    if request.method == "POST":
        format = request.form["format"]

        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            data = {"format": format}
            response = requests.post(f"{FASTAPI_URL}/Change video chroma subsampling/", files=files, data=data)

        if response.status_code == 200:
            result = response.json()
            subsampled_path = result.get("output_path")

            return jsonify({"message": "Chroma subsampling applied successfully", "subsampled_path": subsampled_path})
        else:
            return jsonify({"error": f"Failed to apply chroma subsampling: {response.status_code}"}), 500

    return render_template("chroma_subsampling.html")



# Exercise 9: Extract video information
@app.route("/exercise9/extract-rellevant-data/", methods=["GET", "POST"])
def extract_rellevant_data():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            response = requests.post(f"{FASTAPI_URL}/Extract video information/", files=files)

        if response.status_code == 200:
            result = response.json()
            metadata_file_path = result.get("metadata_file_path")

            return jsonify({"message": "Metadata extracted successfully", "metadata_file_path": metadata_file_path})
        else:
            return jsonify({"error": f"Failed to extract metadata: {response.status_code}"}), 500

    return render_template("extract_rellevant_data.html")


# Exercise 10: Extract BBB Container Information
@app.route("/exercise10/bbb-container/", methods=["GET", "POST"])
def bbb_container():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            response = requests.post(f"{FASTAPI_URL}/BBB Container/", files=files)

        if response.status_code == 200:
            result = response.json()
            output_file_path = result.get("output_path")

            return jsonify({"message": "BBB container extracted successfully", "output_file_path": output_file_path})
        else:
            return jsonify({"error": f"Failed to extract BBB container: {response.status_code}"}), 500

    return render_template("extract_bbb.html")


# Exercise 11: Extract Audio Tracks
@app.route("/exercise11/extract-audio-tracks/", methods=["GET", "POST"])
def audio_tracks():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            response = requests.post(f"{FASTAPI_URL}/Extract audio tracks/", files=files)

        if response.status_code == 200:
            result = response.json()
            output_file_path = result.get("output_path")

            return jsonify({"message": "Audio tracks extracted successfully", "output_file_path": output_file_path})
        else:
            return jsonify({"error": f"Failed to extract audio tracks: {response.status_code}"}), 500

    return render_template("get_audio_tracks.html")


# Exercise 12: Generate Video with Macroblocks and Motion Vectors
@app.route("/exercise12/macroblocks-motionvectors/", methods=["GET", "POST"])
def macroblocks_motionvectors():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            response = requests.post(
                f"{FASTAPI_URL}/Generate video with macroblocks and motion vectors/",files=files)

        if response.status_code == 200:
            result = response.json()
            output_video_path = result.get("output_path")

            return jsonify({"message": "Video generated successfully", "output_video_path": output_video_path})
        else:
            return jsonify({"error": f"Failed to generate video: {response.status_code}"}), 500

    return render_template("get_macroblocks_motionvectors.html")


# Exercise 13: Generate Video with YUV Histogram Overlayed
@app.route("/exercise13/yuv-histogram/", methods=["GET", "POST"])
def yuv_histogram():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            response = requests.post(
                f"{FASTAPI_URL}/Generate video with YUV histogram overlayed/",files=files,)

        if response.status_code == 200:
            result = response.json()
            output_video_path = result.get("output_path")

            return jsonify({"message": "Video generated successfully", "output_video_path": output_video_path})
        else:
            return jsonify({"error": f"Failed to generate video: {response.status_code}"}), 500

    return render_template("get_yuv_histogram.html")


# Exercise 14: Compress Video with VP8, VP9, H265, and AV1
@app.route("/exercise14/video-conversor/", methods=["GET", "POST"])
def compress_video():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            response = requests.post(
                f"{FASTAPI_URL}/Compress video with VP8, VP9, H265 and AV1/",files=files)

        if response.status_code == 200:
            result = response.json()
            compressed_videos_info = result.get("compressed_videos", {})

            return jsonify({"message": "Video compressed successfully", "compressed_videos": compressed_videos_info})
        else:
            return jsonify({"error": f"Failed to compress video: {response.status_code}"}), 500

    return render_template("video_conversor.html")


@app.route("/exercise15/encoding-ladder/", methods=["GET", "POST"])
def encoding_ladder():
    if request.method == "POST":
        if "input_file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        input_file = request.files["input_file"]
        ladder = int(request.form.get("ladder", 0))

        file_path = os.path.join(app.config["UPLOAD_FOLDER"], input_file.filename)
        input_file.save(file_path)

        with open(file_path, "rb") as file:
            files = {"input_file": file}
            data = {"ladder": ladder}
            response = requests.post(
                f"{FASTAPI_URL}/Encoding Ladder/",files=files,data=data)

        if response.status_code == 200:
            result = response.json()
            output_path = result.get("output_path")

            return jsonify({"message": "Encoding ladder applied successfully", "output_path": output_path})
        else:
            return jsonify({"error": f"Failed to apply encoding ladder: {response.status_code}"}), 500

    return render_template("encoding_ladder.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)