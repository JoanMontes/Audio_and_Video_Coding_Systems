# S2 - MPEG4 AND MORE ENDPOINTS REPORT
## Introduction
This project contains the implementation of various endpoints and tools for audio and video coding systems, focusing on tasks such as changing video resolution, modify chroma subsampling, extract relevant data from a video, creation of a `.mp4` container, motion vector visualization and YUV histogram analysis. The project demonstrates how FFMPEG can be used to manipulate and analyze multimedia files efficiently.
The tasks are implemented as an endpoints of our FastAPI app, created in the previous project [P1 - API & DOCKERIZATION](https://github.com/JoanMontes/Audio_and_Video_Coding_Systems/tree/main/P1%20-%20API%20%26%20Dockerization).

All exercises of this project would be implemented using the [Big Buck Bunny](https://www.youtube.com/watch?v=aqz-KE-bpKQ&t=1s&ab_channel=Blender) (BBB) video.

In this report we will explain how we create the different tasks, using FFMPEG commands, and how we create the different endpoints of our API, as well as show and analyze all the outputs obtained in each task.


## Tasks
### Exercise 1
In this exercise we are asked to modify the resolution of the BBB video using an FFMPEG command. The FFMPEG command created is the following:

```
ffmpeg -i input_path -vf f"scale={resolution}:-1 -c:a copy output_path
```

As in the image case, the `-i` followed by the input_path specifies the input video file, then the `-vf, f"scale={resolution}:-1"` resizes the video to a resolution of a width introduced by the user and the -1 tells ffmpeg to automatically adjust the height to maintain the aspect ratio.
Then we use the library `subprocess` in order to run the FFMPEG command.

After creating the changing resolution function, we implemented the endpoint of our FastAPI. In this part the user will be asked to charge an input file from it's computer, then, an output path will be created in the GitHub folder (where the user have the repository) and after executing, the endpoint will call the previous FFMPEG function and will run the command, creating, in the output directory, the video with modified resolution. Here we can see a frame of the modified video:

![image](https://github.com/user-attachments/assets/fd14abde-22b8-4379-9c18-e8471dfe49f4)


### Exercise 2
In this exercise we are asked to modify the chroma subsampling of the video. Therefore, the FFMPEG command created is the following:

```
ffmpeg -i input_path -pix_fmt format output_path
```

As we have seen in the previous task, the `-i` followed by the input_path specifies the input video file, then the `pix_fmt` command is the parameter that FFMPEG use to modify the chroma subsampling. The `format` command is where the user will specify the chroma subsampling format, FFMPEG accepts three types of chroma subsampling format:

- yuv420p (4:2:0): It is the lower-quality format, it subsamples chroma both horizontally and vertically. We found this type of format in streaming, youtube, blu-ray, etc.
- yuv422p (4:2:2): It is a moderate-quality format, it subsamples chroma horizontally and it is tipically used in broadcast TV and semi-professional workflows.
- yuv444p (4:4:4): It is the high-quality format and no chroma subsampling is applied, that results in a full color resolution video. We found this type of format in professional editing, color grading and archiving.

As the BBB video is downloaded from YouTube, the chroma subsampling format in which we download the video is the lower quality one (4:2:0). Therefore, we can not create a video with higher quality format. Moreover, to check if the command works correctly we implemented the endpoint of our FastAPI. In this part, the user will be asked to charge an input file and write a chroma subsampling format (yuv420p, yuv422p, yuv444p). After executing, the endpoint will execute the FFMPEG command and the output file will be created in the output folder.

As we said before, as the quality format is the lowest, we are not able to create a file with higher quality format, but as the endpoint is executed correctly, we can assume that the FFMPEG command is performing well.


### Exercise 3
In this exercise we are asked to read the information and the rellevant data from the video. In order to extract the rellevant data from a video, we can use FFMPEG but adding some modifications when running the command. As we only want to read the information of the video the FFMPEG command will be the next:

```
ffmpeg -i input_path
```

But, when we use the subprocess library in order to run the command, we will use the subprocess.PIPE, that allows us to access the stream in Python, instead of print the output directly to the console, therefore, we return the `stderr` output, where we will find all the video data. We prefer doing that because we found a good idea to, instead of printing the metadata information of the video, we will create a `.txt` file as an output where all the rellevant information of the video will be stored.

That is why, when creating the endpoint, use the next lines of code:

```
with open(metadata_file_path, "w") as metadata_file:
            metadata_file.write(metadata)
```

Because, we will write the `medatada` information in the `metadata_file_path` (.txt file created in the output folder).

Once the user execute the endpoint, in the output folder we will obtain the .txt file with the rellevant data. Here we can see a screenshot of its content:

![image](https://github.com/user-attachments/assets/e8024427-f8dc-47cc-81cf-9948d426fc49)

As we can see, we can detect information features of the input video, as its name, artist, duration, bitrate, and more sofisticated features regarding its stream video and audio. In the video part we found that the video is compressed with `h264` or `MPEG-4` codec, the chroma subsampling format that we identify in the previous task, the resolution, fps, and more.
In the audio part we can detect the audio channels, in this case, the `aac` is the codification used in the video with a sampling frequency of 48000 Hz.
