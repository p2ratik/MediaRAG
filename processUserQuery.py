import numpy as np
import joblib
import read_chunks
from sklearn.metrics.pairwise import cosine_similarity
import os
from google import genai


def getResponseLLM(prompt, api_key):
    """
    Process the prompt along with the data provided
    and responds the user based on that.
    """

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

    return response.text

def processUserQuery(query, api_key):
    """
    Converts the user query to vectors and fetch the top 5
    most relavant chunks from the database using cosine similarity 
    and passes it to the LLM.
    """

    if(os.path.exists('embeddings.joblib')):
        df = joblib.load('embeddings.joblib')
        #question = input('Please enter your query :')   
        question_embedding = np.array(read_chunks.getEmbeddings(query))

        emebed_text = np.vstack(df['Embedding'].values)
        cos_sim = cosine_similarity(emebed_text, question_embedding).flatten()

        index = np.argsort(cos_sim)[::-1][0:3]

        df_new = df[['Video_No', 'Video_title', 'Text', 'Start', 'End']].iloc[index, :]
        df_new = df_new.reset_index(drop=True)
        #print(df[['Video_No', 'Video_title', 'Text', 'Start', 'End']].iloc[index, :])

    prompt = f'''I am teaching python and AI tools. Here are video subtitle chunks containing video title, video number, start time in seconds, end time in seconds, the text at that time:

    {df_new.to_json(orient='records')}
    ---------------------------------
    "{query}"
    User asked this question related to the video chunks, you have to answer in a human way (dont mention the above format, its just for you) where and how much content is taught in which video (in which video and at what timestamp) and guide the user to go to that particular video. If user asks unrelated question, tell him that you can only answer questions related to the course. Only answer the video number , video title and the timestamps present in the data. Don't answer your opinion or don't provide any other information about the topic. Only respond according to the data provided.
    '''
    try:
        response = getResponseLLM(prompt=prompt, api_key=api_key)
    except Exception as e:
        print('some error occured.....', e)    
    

    return response


