import os
import subprocess
import ffmpeg

def mp4tmp3():
    """
    This python script is used to convert a mp4 or any video
    to an audio mp3 file. 
    """
    files = os.listdir('Videos')
    if not (os.path.isdir('audio')):
        os.mkdir('audio')

    for file in files:
        f_name = file.split(' ')[0]+'_'+str(file.split(' ')[1].split('.')[0])
        subprocess.run(['ffmpeg', '-i', f'Videos/{file}', f'audio/{f_name}.mp3'])

def convert():
    """
    This python script is used to convert a mp4 or any video
    to an audio mp3 file. 
    """

    files = os.listdir('Videos')
    if not (os.path.isdir('audio')):
        os.mkdir('audio')

    for file in files:      
        f_name = file.split(' ')[0]+'_'+str(file.split(' ')[1].split('.')[0])
        stream = ffmpeg.input(f'Videos/{file}')
        stream = ffmpeg.output(stream, f'audio/{f_name}')
        ffmpeg.run(stream)

