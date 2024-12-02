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


### Exercise 4
In the next task we are asked to cut the BBB video into 20 seconds, and export this 20 seconds creating three audio channels, as AAC mono track, MP3 stereo with lower bitrate, and in AC3 codec. Before that, we will package everything in a `.mp4`. For this exercise we are going to use some FFMPEG commands, one for each requirement and finally one for package all in a `.mp4` file.
First, and in order to execute the different requirements, we need to create temporary files of each part. After that, we will cut the video into a 20 seconds video, using the following command:

```
ffmpeg -i input_path -t 20 -c:v copy -c:a copy video_cut_path
```

In this command, the `-t 20` is in charge of cutting the video in a 20 seconds video. After that, we will use this 20 seconds video to create all the different commands and the output video file.

The following three FFMPEG commands will be the ones that export the audio tracks. First the AAC mono track command:

```
ffmpeg -i video_cut_path -vn -ac 1 -c:a aac aac_audio_path
```

After specify the input file, the `-c:a aac` command encodes the audio in AAC format, and then the `-ac 1` converts the audio to a mono by using a single channel. Finally the output is stored in the `aac_audio_path`.
Now, the MP3 stereo track:

```
ffmpeg -i video_cut_path -vn -ac 2 -b:a 128k -c:a mp3 mp3_audio_path
```

As in the previous command, after specify the input file, the `-c:a libmp3lame` uses the LAME encoder to create an `MP3` file, and then the `ac 2` converts the audio to stereo, with 2 channels. Finally, the `-b:a 128k` sets a lower bitrate of 128kbps.
Finally, the AC3 codec track:

```
ffmpeg -i video_cut_path -vn -c:a ac3 ac3_audio_path
```

Here, the `-c:a ac3` encodes the audio in the AC3 (Dolby Digital) codec, and then outputs the encoded audio into the `ac3_audio_path`.

Once the requirements are reached, the next step was to package everything into a single `MP4` file. For this process, we will use the `-map` option in FFMPEG, that ensures each desired stream is added correctly to the final container.
The command we use for this part is the next:

```
ffmpeg -i video_cut_path -i aac_audio_path -i mp3_audio_path -i ac3_audio_path -map 0:v -map 1:a -map 2:a -map 3:a -c:v copy -c:a copy output_path
```

After specify all the input files, `video_cut_path`, `aac_audio_path`, `mp3_audio_path` and `ac3_audio_path`, we use the `-map` command to map all toghether. First, the `-map 0:v:0` that maps the video stream for the first input (the 20 seconds video). Then, `-map 1:a:0` maps the first audio track (AAC mono), the `-map 2:a:0` maps the second audio tracks (MP3 stereo) and `-map 3:a:0` maps the third audio track (AC3 codec). After that, the `-c:v copy` and `-c:a copy` copy the video and audio streams without re-encoding. Finally, all is saved in the `output_path`, where a `.mp4` will be created.

Once we have all the commands and running steps created we need to create the endpoint. As in the preovious endpoints, the user will upload the input BBB video, and after execute the endpoint, the output video is stored in the `output_path` stablished, the video, will be a 20 seconds `.mp4` video with the three audio tracks created.
In the next task we will see how many tracks are created and check if our command works correctly.

### Exercise 5


### Exercise 6
In this exercise we are asked to create a video with the motion vectors and macroblocks of the input video BBB. For this, we will use the following FFMPEG command:

```
ffmpeg -flags2 +export_mvs -i input_path -vf codecview=mv=pf+bf+bb output_path
```

The `-flags2` and `+export_mvs` commands enable the extraction of the motion vector data, while the `-vf codecview=mv=pf+bf+bb` is used to display the motion vectors and the macroblocks types.
As in the previous tasks, we use the subprocess library in order to run the FFMPEG command.

After the creation of the command, we create the endpoint, where the user will upload an input video and execute the endpoint in order to execute the FFMPEG command and create an output video, in the output folder established, of the motion vectors and macroblocks.

One disadvantage of this execution is the time it takes to create the output video, therefore, to be faster, we use the 20 seconds video created in exercise 4. Here we can see one frame of the output video:

![image](https://github.com/user-attachments/assets/43cf45a6-16a2-4f15-8321-9bf1d67aee42)

In this frame we can clearly see how the movement of the butterfly's wings is established by the motion vectors.


### Exercise 7
Finally, we are asked to generate a video with it's YUV histogram. For this task, we found an FFMPEG command that can generate an output video, with the YUV histogram of the input video overlayed in the output video. The FFMPEG command used is the following:

```
ffmpeg -i input_path -vf split=2[a][b],[b]histogram,format=yuva420p[hh],[a][hh]overlay output_path
```

The `split=2[a][b],[b]histogram,format=yuva420p[hh],[a][hh]overlay` command is structured in short commands being able to create the output video. The `split=2[a][b]` is the one that splits the input into two streams, the stream [a] (main video) and [b] the one we will use to create the histogram.
Then, the `[b]histogram` generates a YUV histogram in overlay mode, and the `format=yuva42p` ensures proper pixel format for histogram overlay (it must be the same than the input video).
Finally, the `[a][hh]overlay` command overlays the histogram onto the original video [a].

Once the command is created, we create the endpoint, where the user will upload the input video and execute the command. After the execution, the endpoint will generate a video with an overlaid YUV histogram, providing a visual representation of luminance and chrominance levels.

Here we can see one frame of the output video where we can observe the YUV histogram with the different representation levels:

![image](https://github.com/user-attachments/assets/b2c7886a-f47a-40e4-925d-cf7b2ba90b40)

