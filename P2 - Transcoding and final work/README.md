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

![image](https://github.com/user-attachments/assets/b7bf1f20-3949-4e06-90dd-d41ae0e37c04)


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
In this part of the practice, we are tasked with developing the GUI for our API. As we know, it is divided into a backend (the program's infrastructure) and a frontend (what users see). For the backend development, we will use `Flask`, a framework written in Python that allows for creating web applications. For the frontend, we will use `HTML` and `CSS`.

### app_requests.py creation
To create the application, it is necessary to build an interface capable of interacting with the backend implemented in the `main.py` file. This means that as the application is used, it sends requests to the backend created with `FastAPI` to ensure proper functionality.

The general structure of the file starts by defining the Flask application (`app = Flask(__name__)`), followed by setting up a folder to upload files (`UPLOAD_FOLDER`) and configuring the base URL for the FastAPI backend, which is set to the IP `http://127.0.0.1:8000`. This indicates that the FastAPI server is located on port 8000 of our local machine.

In this file, the HTTP requests that Flask sends to the FastAPI backend are defined using the `requests` library. Depending on the functionality of each endpoint, data is sent as parameters, form data, or files. In the case of the latter, Flask first saves the files uploaded by the user in the `UPLOAD_FOLDER` directory. It then reads the file and sends it to the backend.

In `main.py` (FastAPI backend), the request is processed at the corresponding endpoint, performing the specified task and returning a result in `JSON` format, as Flask can easily process this format.

When Flask receives the response from the FastAPI backend, it uses the `JSON` data to return the final result. Finally, Flask renders the specified `HTML` file so the user can view the specified format.

The main functionalities of the GUI are the same as in previous practices, but with the addition of two new endpoints created in this one.
These functionalities are divided into color conversion, image processing, and video processing.
It is worth mentioning that each functionality of our application corresponds to an endpoint created in our previous projects.

It is important to specify that the Flask server runs on port 5000. Therefore, to access it, we must navigate to the IP `http://127.0.0.1:5000`.

### HTML and CSS files creation
Once the requests file is created in Flask, the next step is to integrate the frontend of the application so that users can interact with the features provided by the backend. To do this, we will use an HTML and CSS template extracted from the internet, which will be adapted to the specific needs of our application. This template includes both text formatting and animations required for the visual design of the application.

The GUI of the application is organized into a main menu, from which users can access the various functionalities available in the system. This menu presents a set of 14 main features, each corresponding to a specific API endpoint. Users can click on the images representing each feature and be redirected to the corresponding page where they can interact with the system. Each feature is clearly distinguished through images, and descriptive titles.

![image](https://github.com/user-attachments/assets/95aa3266-9915-44b1-b161-3ec83fd29a98)

The main menu is the entry point to all the features of the application. This menu is presented containing a series of images, each linked to a specific feature. When the user clicks on one of these images, they are redirected to the corresponding page where they can enter the necessary data.

Here we can see the data required from the conversion color functionality,

![image](https://github.com/user-attachments/assets/1e8d6f0c-6d1e-41c0-b41d-87002d313bfe)

And the one requiring to upload a video file, 

![image](https://github.com/user-attachments/assets/ea5cc2c8-b9e4-477b-8cc0-ecdc325cf25e)


The general structure of the frontend of our API is organized in two folders. The `templates` directory, where all the HTML files for the application are stored, organized os that each feature has its own page.

And the `static` directory, where the CSS file used for design and the images used in the menu are stored.

Navigation in the application is intuitive thanks to the main menu, which provides direct links to the features. Each section has a clear layout with a specific form that allows the user to enter data or upload files easily.


## AI Implementation
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

4. We should check Flask is installed in our computer. If not, use `pip install flask`. 

5. Then we have to open another terminal and change the directory to `scav_api/` and execute the comand 
`python app_requests.py`

Finally, to see the GUI and use it to execute the endpoints, we go to the browser and go to http://localhost:5000. 

