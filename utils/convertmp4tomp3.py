import os
import subprocess
import ffmpeg


def mp4tmp3():
    """
    This python script is used to convert a mp4 or any video
    to an audio mp3 file. 
    """
    files = os.listdir('E:\Projects\RAG_model\Videos')
    if not (os.path.isdir('E:\Projects\RAG_model\ audio')):
        os.mkdir('E:\Projects\RAG_model\ audio')

    for file in files:
        f_name = file.split(' ')[0]+'_'+str(file.split(' ')[1].split('.')[0])
        subprocess.run(['ffmpeg', '-i', f'E:\Projects\RAG_model\Videos/{file}', f'E:\Projects\RAG_model\ audio/{f_name}.mp3'])

def convert(path):
    """
    Convert all videos in 'Videos' folder to MP3 audio files.
    Saves them inside 'Audio' folder.
    """

    base_dir = r"E:\Projects\RAG_model"
    videos_dir = os.path.join(path, "Videos")
    audio_dir = os.path.join(path, "audio")

    # Create output folder if it doesn't exist
    if not os.path.exists(audio_dir):
        os.mkdir(audio_dir)

    files = os.listdir(videos_dir)

    for file in files:
        # Skip non-video files
        if not file.lower().endswith((".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv")):
            continue

        file_path = os.path.join(videos_dir, file)
        filename, _ = os.path.splitext(file)   # remove extension
        output_path = os.path.join(audio_dir, filename + ".mp3")

        # ffmpeg input → output
        stream = ffmpeg.input(file_path)
        stream = ffmpeg.output(stream, output_path)
        ffmpeg.run(stream)

        print(f"Converted: {file} → {output_path}")

