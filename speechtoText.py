from google import genai
import os


def speechtotext(apikey):
    """
    Transcibes every audio files present and prepare a dictionary
    containing the video-deatils , transcibed/translated audio along
    with time stamps

    """
    prompt = 'Transcibe the audio clip along with timestamp of average 10 seconds. If the audio is in Hindi then translate and transcibe in English not in Hindi. The format of time stamps is [start, end]'
    data = {}
    files = os.listdir('audio')

    client = genai.Client(api_key=apikey)

    for filename in files:
        videono = filename.split('_')[1].split('.')[0]
        video_tit = filename.split('_')[0]
        try:
            file = client.files.upload(file = f'audio/{filename}')
            response = client.models.generate_content(
            model="gemini-2.5-flash", contents=[prompt, file]
        )   
            data[f'{video_tit}_{videono}'] = response.text         
        except Exception as e:
            print('Failed to transcibe the text', e)   
    return data


