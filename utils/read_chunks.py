import requests
import os
import pandas as pd
import joblib
from sklearn.metrics.pairwise import cosine_similarity
import json

def getEmbeddings(textVector):
    """
    Returns the vector embeddings of the text vector 
    provided.
    """
    r= requests.post('http://localhost:11434/api/embed', json={
    'model':'bge-m3',
    'input':textVector
})
    return r.json()['embeddings']

def vectorDataSpace(path):  
    """
    Creates vector embedding for every text chunk of every video and 
    stores it into a joblib file as a pandas dataframe.
    """
    json_dir = os.path.join(path, 'json')
    json_files = os.listdir(json_dir)

    data_embeded = []

    for filename in json_files:
        chunk_id = 1
        with open(f'{json_dir}/{filename}')as f:
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

    joblib.dump(df, f'{path}/embeddings.joblib')



 