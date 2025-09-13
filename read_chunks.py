import requests
import os
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import json

def getEmbeddings(textVector):
    r= requests.post('http://localhost:11434/api/embed', json={
    'model':'bge-m3',
    'input':textVector
})
    return r.json()['embeddings']

def vectorDataSpace():  
    json_files = os.listdir('json')

    data_embeded = []

    for filename in json_files:
        chunk_id = 1
        with open(f'json/{filename}')as f:
            content = json.load(f)
        chunk_text = [text['Text'] for text in content['Chunks']]
        embeddings = getEmbeddings(chunk_text)
        for index, embeding in enumerate(embeddings):
            metadata = {'ChunkId':chunk_id, 
                        'Embedding': embeding}
            my_dict = {**content['Chunks'][index], **metadata}
            data_embeded.append(my_dict)
            chunk_id+=1

    df = pd.json_normalize(data_embeded)

    joblib.dump(df, 'embeddings.joblib')



  
#     break

# vector = getVectors(['My name is Pratik and I like python'])
# print(len(vector[0]))

# with open('json/PythonForwebDev_01.json') as f:
#     content = json.load(f)
# df = pd.json_normalize(content['Chunks'])
# print(df)    