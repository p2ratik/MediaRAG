import os
import subprocess

def convertmp4tomp3():
    files = os.listdir('Videos')
    for file in files:
        f_name = file.split(' ')[0]+'_'+str(file.split(' ')[1].split('.')[0])
        subprocess.run(['ffmpeg', '-i', f'Videos/{file}', f'audio/{f_name}.mp3'])
convertmp4tomp3()
