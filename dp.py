import pytube
import os

num= 0
playlist_url =input('Enter Url : ')
playlist = pytube.Playlist(playlist_url)

# Specify the folder path where you want to save the videos
save_folder = 'C:/Users/Hijazi/Desktop/d_playlist_py/save_folder'

# Create the save folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)
all_files_in_folder=os.listdir(save_folder)
# Download the videos and save them in the specified folder
for video in playlist.videos:
    num=num+1
    print(F"Loading Download ...{video.title} !")
    for item in all_files_in_folder :
        item_path = os.path.join(save_folder, item)
        if os.path.isfile(item_path):
           if item == {video.title}:
                print(F'الملف موجود')
                
           else :
               # video.streams.get_highest_resolution().download(output_path=save_folder)
                # # video.captions.get_by_language_code('en')
                print(F'success download Video Namber  {num} ') 
               
               
               

print('Videos downloaded successfully!')
