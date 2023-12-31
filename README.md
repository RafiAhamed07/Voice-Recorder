# Voice Recorder Application

## Overview

The Voice Recorder Application is a simple tool built using Python and Tkinter for the graphical user interface. It allows users to record audio for a specified duration and save the recording as an MP3 file. The application utilizes the sounddevice library for audio recording and scipy for writing the audio data to an MP3 file.

## Features

- User-friendly graphical interface.
- Customizable recording time and filename.
- Ability to select the directory for saving recordings.
- Recording feedback messages.

## Dependencies

Make sure to install the following dependencies before running the application:

- Tkinter: For GUI components.
- sounddevice: For audio recording.
- scipy: For saving audio data as an MP3 file.

```bash
pip install sounddevice scipy
```

```bash
pip install scipy
```

## Usage
1. Run the script using Python:
```bash
python main.py
``` 
2. Enter the recording time in seconds and specify a filename.
3. Click the "Select Path" button to choose the directory where the recording will be saved.
4. Click the "Start Recording" button to initiate the recording process.
5. The application will display messages indicating the start and end of the recording.
6. The recorded audio will be saved as an MP3 file in the selected directory.

*** You can also use Voice-Recoder.exe file to avoid python  installation.

## Notes
◾ Ensure that the required dependencies are installed before running the script.

◾ The application is relatively simple and can be extended with additional features and error handling.

## Contributors
◾ Rafi Ahamed.
