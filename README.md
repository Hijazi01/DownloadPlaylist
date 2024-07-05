# YouTube Playlist Downloader

This Python script downloads a YouTube playlist and saves the videos in a specified folder.

## Features

- Downloads all videos from a given YouTube playlist
- Checks if the video file already exists in the save folder to avoid duplicates
- Saves the downloaded videos in the specified folder

## Requirements

- Python 3.x
- `pytube` library
- `os` module (built-in)

## Installation

1. Install the required libraries:
   pip install pytube

Copy

2. Save the script in a directory of your choice.

## Usage

1. Run the script:

python playlist_downloader.py

livecodeserver
Copy

2. When prompted, enter the URL of the YouTube playlist you want to download.

3. The script will create a folder called `save_folder` in the specified path (currently set to `C:/Users/Hijazi/Desktop/d_playlist_py/save_folder`) and download the videos into this folder.

4. The script will print the progress of the download, including the title of the video being downloaded and the number of the video being downloaded.

5. If a video file already exists in the save folder, the script will skip that video and move on to the next one.

6. Once all the videos have been downloaded, the script will print a "Videos downloaded successfully!" message.

## Customization

- You can customize the save folder path by changing the value of the `save_folder` variable.
- If you want to download the captions for the videos, you can uncomment the line `# video.captions.get_by_language_code('en')`.
- You can modify the code to handle different file naming conventions or to add additional features, such as progress tracking or error handling.
