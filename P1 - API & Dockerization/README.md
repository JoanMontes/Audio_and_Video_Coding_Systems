# P1 - API & DOCKERIZATION REPORT
## Introduction
This project demonstrates how to build and deploy an API using FastAPI that interacts with FFMPEG to perform some signal processing tasks outlined in [S1 - JPEG, JPEG2000 and FFMPEG REPORT](https://github.com/JoanMontes/Audio_and_Video_Coding_Systems/tree/main/S1%20-%20JPEG%2C%20JPEG2000%20and%20FFMPEG). The solution leverages Docker and Docker Compose to streamline deployment and ensure modularity.

To set up the project, we are using [Docker Desktop](https://www.docker.com/products/docker-desktop/). This program must be installed to create the required Docker images and containers locally.

In this file, you will find all the instructions to install and execute the requirements needed to run our API.

The project is structured into two folders: one for the FastAPI app (API and Docker configuration) and the other for the FFMPEG Docker setup. Each folder contains a `Dockerfile` to build its respective Docker image and container. The API folder also includes all the files from the `S1 - JPEG, JPEG2000, and FFMPEG REPORT` along with a `requirements.txt` file containing the dependencies needed to create the Docker image. Both containers are connected using a `docker-compose.yml` file.


## Files implementation

### Dockerfile for API
To containerize the API, we create a `Dockerfile`. The first step is selecting the base image; we use the `python:3.11` image, which includes Python and essential tools.

Next, we set the working directory, which specifies where subsequent commands will execute. We then copy the `requirements.txt` file, which lists all the required libraries, into the container. Before installing the libraries, we upgrade `pip` for compatibility. Once the dependencies are installed, we copy all contents into the app directory.

We expose port 8000 so the container listens for connections on this port. Finally, we use a command to start the FastAPI application `(main.py)` on port 8000 when the container starts.

### API code (main.py)
This file contains the core application that runs when we start the Docker containers. The first step is importing Python files and methods created in the previous seminar. Afterward, we create the FastAPI app instance with `FastAPI()`.

We define endpoints, such as "GET" requests for the root URL and "POST" requests for various tasks. These "POST" endpoints are adapted from previous exercises using an AI tool like ChatGPT, ensuring they integrate seamlessly with FastAPI. The generated Swagger UI at http://localhost:8000/docs provides a visual interface to interact with these endpoints.

### Dockerfile for FFMPEG
The Dockerfile for the `FFMPEG` is much simpler, as we only have two steps. The first step is to install the base image of the container, and just as we did in the Dockerfile for the API, we used `python:3.11`. Then, we simply install `FFMPEG`.

### Docker Compose
To be able to run a multi-container application we define a `docker-compose.yml` file. 
The first step is to select the version, we have chosen the versión "3.8".

Then we define the two services that make up the application:

- First we define the scav_api service, which defines the configuation to build the Docker image. To do this, we define the folder that we will use as context, we select the Dockerfile that is inside the folder. We also define the container name and we map the ports to allow access to the API. Then we mount the uploads directory of the computer inside the container. Finally we specify that this service depends on the ffmpeg_service container, ensuring that this is executed before that scav_api container.

- Finally we declare the ffmpeg service, following the same metodology we followed with the previous service.

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

After running the containers, we should create the `docker-compose.yml` in order to combine both dockers, and execute the `docker-compose up --build` command to run the docker compose and create the container with both containers as we can see in the following image.

![image](https://github.com/user-attachments/assets/af78beb5-1eca-4dc3-837a-6bf6d7d9c3cb)

After creating the `main.py` we can access the API using the Swagger UI Documentation, entering the http://localhost:8000/docs when the API is running. In order to run the API we need to execute the command `python -m uvicorn main:app --reload` inside the folder where the `main.py` is ubicated.

Entering the previous URL we can access to all the endpoints developed, in our case, the next ones will be holded:
![image](https://github.com/user-attachments/assets/e18b7d7f-4a4c-4e5e-809a-7df245c7765f)


## How to execute the API?
To execute the API after downloading it from GitHub, follow these steps:

1. The first step is, obviously, downloading all the resources in the GitHub repository. 

2. Then, we must open a terminal and change the directory to the folder with the name of the practice `(P1 – API & Dockerization)`, and once we are inside the folder, execute the following command: `docker-compose up --build`.
To execute this command, we must ensure that the following libraries are installed: uvicorn, fastapi, opencv and python-multipart. If these are not installed, an error will come up and we simply have to install the library `(pip install <library>)` and execute the previous command again. 

3. Once the project is created, we change the directory to `scav_api/`, where the `main.py` is located, and we execute the following command:
`python -m uvicorn main:app --reload`. This will launch the application. 

Then to see the API, we go to the browser and we use the Swagger UI Documentation at http://localhost:8000/docs.
