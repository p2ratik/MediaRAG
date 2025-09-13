import json
import re
def getJson(data):    
    pattern = r"\[(\d{1,2}:\d{2}),\s*(\d{1,2}:\d{2})\]\s*(.+?)(?=\n\[|\Z)"  
    db = []
    for video, text in data.items():
        metadata = {}
        video_data = []
        description = re.findall(pattern, text, flags=re.DOTALL)

        for items in description:
            video_data.append({'Video_No': video.split('_')[1].split('.')[0],
                               'Video_title': video.split('_')[0],
                               'Start': items[0],
                               'End':items[1],
                               'Text': items[2]})
            
        metadata['Chunks'] = video_data
        metadata['text'] = text
        with open(f'json/{video}.json', 'w') as f:
            json.dump(metadata, f)  

  


# getJson(data)

