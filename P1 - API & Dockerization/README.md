# P1 - API & DOCKERTIZATION REPORT
## Introduction
This project demonstrates how to build and deploy an API using Fast API that interacts with FFMPEG for realizing some of the signal processing tasks of [S1 - JPEG, JPEG2000 and FFMPEG REPORT](https://github.com/JoanMontes/Audio_and_Video_Coding_Systems/tree/main/S1%20-%20JPEG%2C%20JPEG2000%20and%20FFMPEG). The solution uses Docker and Docker Compose to streamline deployment and ensure modularity.

To create the project we are using [Docker Desktop](https://www.docker.com/products/docker-desktop/). We should install this program in order to create, from local, the different docker images and containers.

In this file you will be able to install and execute all the requirements to run our API.

The project is structured in two folders, one for the FastAPI

P1 - API & DOCKERIZATION/
├── scav_api/
│   ├── main.py
│   ├── classes_and_methods.py  
│   ├── Dockerfile
│   ├── unit_tests.py
│   ├── Input Images/
│   ├── temp/
│   ├── uploads/         
│   └── requirements.txt
│ 	
├── ffmpeg-docker/
│   └── Dockerfile                             
├── docker-compose.yml      
└── README       


## 
