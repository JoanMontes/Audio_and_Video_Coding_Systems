# P2 - TRANSCODING AND FINAL WORK REPORT

## Introduction

The aim of this project is to extend the API we created using FastAPI we created in the previous labs with two more endpoints, and also creating a Graphical User Interface (GUI) to make the interaction with the API more user friendly. To create the user interface we used html together with Flask so that the GUI is visually appealing and can interact with the FastAPI app we created during the course. 

## Endpoints

### Exercise 1: 

In this exercise we are asked to create a new endpoint in the API that can convert any input video into the following video codecs: VP8, VP8, h265 & AV1. To do so, we used the corresponding ffmpeg commands that convert a video input to the desired video codec. To convert the input video into VP8, used the ffmpeg command: 

```
"ffmpeg", "-i", input_path, "-c:v", "libvpx", "-b:v", "1M", "-c:a", "libvorbis", output_path
```

To convert into VP9: 

```
"ffmpeg", "-i", input_path, "-c:v", "libvpx-vp9", "-b:v", "2M", "-c:a", "libopus", output_path
```

Into h265: 

```
"ffmpeg", "-i", input_path, "-c:v", "libx265", "-preset", "medium", "-b:v", "1M", "-c:a", "aac", output_path

```

Into AV1: 

```
"ffmpeg", "-i", input_path, "-c:v", "libaom-av1","-crf", "30", output_path
```

Then, we create a video file in order to store each of the videos encoded with the desired codecs so we can use these output files in the function and we can overwrite the files when using the function multiple times. 

This code is implemented in the `classes_and_methods.py` file, which is later used in the `main.py` to create the endpoint, and as we will explain later, the endpoint will be used in the `app_requests.py` file in order to be able to execute the endpoint in the GUI. 

### Exercise 2

In this exercise we are asked to create an endpoint that is able to do an encoding ladder. In order to create this endpoint we followed Apple's encoding ladder from the HLS Authoring Specification. The different ladders are given in the following picture:  

(foto)

To create this endpoint, we first defined the different resolutions and the different bitrates given by the Apple's ladder in an array. Then, we simply used the video_resolution function created in the previous labs to change the video resolution given the ladder we are in. The output file is then used in the following ffmpeg command that changes the bitrate to the one corresponding to the ladder: 

```
"ffmpeg", "-i", video_resolution_path, "-b:v", bitrate_ladder[ladder], video_bitrate_path
```

Finally, we created a condition that if the ladder we are in is higher than 4, we use the following command in order to change the frame rate, just as it is specified in the Apple's encoding ladder. The command to change the bitrate is: 

```
"ffmpeg", "-i", video_bitrate_path, "-filter:v", "fps=30",output_path
```
As we can see, we are changing the frame rate to 30 fps. 

If we are not above the 4th ladder, we simply print the information with the output path of the video with the resolution, the bitrate and the frame rate corresponding to the chosen ladder. 

As well as the previous exercise, we implement this exercise in the `classes_and_methods.py` file and we use it in the `main.py` to create the endpoint and then in the `app_requests.py` to be able to use the endpoint in the GUI.

## GUI

## AI
The last step of this lab is to use an AI tool in order to improve the code. We mainly used AI for two purposes: To adapt the HTML template to the desired design we wanted for the GUI of our API, and in order to imporve the app_requests.py, as we were not used to working with Flask and our code needed improvement. 

The main changes in the HTML files was in the index.html, which creates the distribution of the first page of the GUI, where all the endpoints appear and we can choose which one we want to execute. For this file AI was useful to explain which part of the code corresponded to each part of the output and help us create the index part of the GUI to our taste. 

Moreover, AI helped us to create a clean code for the app_requests.py file, by giving us a pattern on how to create call the functions of the API and make them interactive and in GUI and showing the result in the GUI itself, making the GUI selfsuficient. 


## How to execute the API?
To execute the API after downloading it from GitHub, follow these steps:

1. The first step is, obviously, downloading all the resources in the GitHub repository. 

2. Then, we must open a terminal and change the directory to the folder with the name of the practice `(P2 – Transcoding and final work)`, and once we are inside the folder, execute the following command: `docker-compose up --build`.
To execute this command, we must ensure that the following libraries are installed: uvicorn, fastapi, opencv and python-multipart. If these are not installed, an error will come up and we simply have to install the library `(pip install <library>)` and execute the previous command again. 

3. Once the project is created, we change the directory to `scav_api/`, where the `main.py` is located, and we execute the following command:
`python -m uvicorn main:app --reload`. This will launch the application. 

4. Then we have to open another terminal and change the directory to `scav_api/` and execute the comand 
`python app_requests.py`

Finally, to see the GUI and use it to execute the endpoints, we go to the browser and go to http://localhost:5000. 

