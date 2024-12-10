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

![image](https://github.com/user-attachments/assets/135624d1-41ed-474d-9496-1de12cf6f21f)


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

En esta parte de la practica se nos pide desenvolupar la GUI de nuestra API. Como ya sabemos, esta se divide en una parte de backend (infraestructura del programa) y una parte de frontend (lo que ven los usuarios). Para el desarrollo del backend, utilizaremos `Flask`, un framework escrito en Python que permite crear aplicaciones web. Y para el frontend utilizaremos `HTML` y `CSS`.

### app_requests.py creation

Para crear la aplicación es necesario crear una interfaz que sea capaz de interactuar con el backend implementado en el archivo `main.py`, es decir, que como se vaya interactuando con la aplicación, este envie requests al backend creado con FastAPI para asegurar su correcto funcionamiento. 

La estructura general del archivo empieza con definir la aplicación Flask (`app = Flask(__name__)`), seguidamente se establece una carpeta para subir los archivos (`UPLOAD_FOLDER`) y seguidamente se configura la URL base del backend FastAPI, la cual esta configurada con la IP `http://127.0.0.1:8000`. Esto indica que el servidor FastAPI está situado en el puerto 8000 de nuestra máquina local.

En este archivo se definen las solicitudes HTTP que Flask envia al backend de FastAPI utilizando la biblioteca `requests`. Dependiendo de la funcionalidad de cada endpoint, los datos se envían como parametros, datos de formulario o files. En el caso de estas ultimas, Flask primero guarda los archivos subidos por el usuario en el directorio `UPLOAD_FOLDER`. Para posteriormente leer el archivo i lo envia al backend. 

En `main.py` (backend de FastAPI), se procesa la solicitud en el endpoint correspondiente y se realiza la tarea especificada, devolviendo un resultado en formato JSON ya que Flask procesa este formato facilmente. 

Cuando Flaks recibe la respuesta del backend FastAPI, Flask utiliza los datos en formato JSON para devolver el resultado final. Finalmente, Flask renderiza el HTML file especificado para que el usuario pueda observar el formato especificado. 

Las principales funcionalidades de la GUI són las mismas que en las pràcticas anteriores però añadiendo los dos nuevos endpoints creados en esta.
Estas funcionalidades se dividen en, conversión de colores, procesamiento de imagenes i procesamiento de videos.
Cabe destacar, que cada funcionalidad de nuestra aplicación hace referencia a cada endpoint creado en nuestros previos proyectos.

Cabe especificar que el servidor Flask se ejecuta en el puerto 5000, por tanto, para acceder a el tendremos que entrar a la IP `http://127.0.0.1:5000`.

### HTML and CSS files creation



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

4. Then we have to open another terminal and change the directory to `scav_api/` and execute the comand 
`python app_requests.py`

Finally, to see the GUI and use it to execute the endpoints, we go to the browser and go to http://localhost:5000. 

