import ffmpeg

input_file_name = 'videos/flashing_lights.MOV'


#check if the file exists
import os
if not os.path.isfile(input_file_name):
    print("File not found")
    exit()

(ffmpeg
 .input(input_file_name )
 .filter('fps', fps=10, round = 'up')
 .output("%s-%%04d.jpg"%(input_file_name[:-4]), **{'qscale:v': 3})
 .run())
#put the output of the split.py into a folder called frames
# Path: src/frames