# P1 - API & DOCKERTIZATION REPORT
## Introduction
This project demonstrates how to build and deploy an API using Fast API that interacts with FFMPEG for realizing some of the signal processing tasks of [S1 - JPEG, JPEG2000 and FFMPEG REPORT](https://github.com/JoanMontes/Audio_and_Video_Coding_Systems/tree/main/S1%20-%20JPEG%2C%20JPEG2000%20and%20FFMPEG). The solution uses Docker and Docker Compose to streamline deployment and ensure modularity.

To create the project we are using [Docker Desktop](https://www.docker.com/products/docker-desktop/). We should install this program in order to create, from local, the different docker images and containers.

In this file you will be able to install and execute all the requirements to run our API.

The project is structured in two folders, one for the FastAPI app (Docker and API) and the other for the FFMPEG Docker. In these both folders we have two Dockerfiles, in order to build the Docker images and containers. In the folder of our API we can also find all the files from the `S1 - JPEG, JPEG2000 and FFMPEG REPORT` and the `requirements.txt` file that contains all the dependences needed to create the Docker image.
Both Dockers will be connected because of the use of a docker compose file.


## Files implementation

### Dockerfile for API
In order to put the API inside a Docker, we have to create a Dockerfile to build the container. To create the Dockerfile we first select the base image of the container, and we used the Python:3.11 image, which includes Python and all its essential tools. 

The next step is to set the working directory. Which is where all the following comands will be executed. The next step is to copy the requirements text we created with all the required libraries inside the container. Then we install the required libraries. First we upgrade pip to ensure compatibility with the libraries. Then we install the libraries in the requirements.txt. Then we copy all the contents we have into the app directory we set previously. Then we expose the port 8000 so that the container listens to connections to this port. Then we use the last command to start the fastAPI application with the main file in the port 8000 when the container starts

### API code main.py


### Dockerfile for FFMPEG
The Dockerfile for the ffmpeg is much simpler, as we only have two steps. The first step is to install the base image of the container, and just as we did in the Dockerfile for the API, we used Python:3.11. Then, we simply install ffmpeg.

### Docker Compose
To be able to run a multi-container application we define the following Docker-compose file. 
The first step is to select the version, we have chosen the versión "3.8".

Then we define the two services that make up the application. First we define the scav_api service, which defines the configuation to build the Docker image. To do this, we define the folder that we will use as context, we select the Dockerfile that is inside the folder. We also define the container name and we map the ports to allow access to the API. Then we mount the uploads directory of the computer inside the container. 

Finally we specify that this service depends on the ffmpeg_service container, ensuring that this is executed before that scav_api container. Finally we declare the ffmpeg service, following the same metodology we followed with the previous service.

## Creation process
In order to build the Dockerfile of the API, first, we need to create the `requirements.txt`, that will contain the necessary packages that should be installed. In our case, we need FastAPI, Uvicorn, numpy and opencv-python.
Once we have created the Dockerfile and the requirements.txt we are able to build the Docker image, for that we will use the terminal. Navegating to our project directory and writing the command `docker build -t scav-api .` we build the Docker image. After building the docker image we will find it in the list of Docker images: 

`scav-api                             latest      bd2827a584c9   4 hours ago   429MB`

After building the docker image, we run the container using the command: `docker run -d --name scav-api-container -p 8000:8000 scav-api`

To ensure that our FastAPI application is running correctly inside the Docker container we need to acces the application. For that we will use the Swagger UI Documentation of FastAPI: http://localhost:8000/docs.

After creating the FastAPI docker and checking the correct functionality of the app we can create the docker image which contains the FFMPEG.

Considering the Dockerfile of this docker, we can build the docker image using the same command `docker build -t ffmpeg-docker`, but now in the folder where this Dockerfile is ubicated. Checking the list of Docker images, we can see the image created:

`ffmpeg-docker                        latest      c9f30e80d62a   4 hours ago   467MB`

And in the same way, run the container using the previous command but with the new docker image created, `docker run -d --name ffmpeg_service -p 8000:8000 ffmpeg-docker`.


## How to execute the API?
To be able to run the code when downloading the code from GitHub the following steps must be followed: 

The first step is, obviously, downloading all the resources in the GitHub repository. Then, we must open a terminal and change the directory to the folder with the name of the practice (P1 – API &
Dockerization), and once we are inside the folder, execute the following command: `docker-compose up --build`.
To execute this command, we must ensure that the following libraries are installed: uvicorn, fastapi, opencv and python-multipart. If these are not installed, an error will come up and we simply have to install the library `(pip install <library>)` and execute the previous command again. 

Once the project is created, we change the directory to `scav_api/`, where the `main.py` is located, and we execute the following command:
`python -m uvicorn main:app --reload`. This will launch the application. 

Then to see the API, we go to the browser and we use the Swagger UI Documentation at http://localhost:8000/docs.
