import utils.convertmp4tomp3 as convertmp4tomp3
import utils.createChunks as createChunks
import utils.processUserQuery as processUserQuery
import utils.read_chunks as read_chunks
import utils.speechtoText as speechtoText
from dotenv import load_dotenv
import os

load_dotenv()

# Access variables
api_key = os.getenv("API_KEY")
path = os.getenv("PATH_DIR")

query = input('Please Enter your query sir/Mam : ')

#api_key = getpass('Please Enter your google gemini api-key : ')



if (os.path.exists('embeddings.joblib')):
    print(processUserQuery.processUserQuery(query=query, api_key=api_key, path=path))

else:
    try:

        # First we will convert mp4 files to mp3

        convertmp4tomp3.convert(path=path)

        # Transcipting audio files into plain english along with time stamps

        data = speechtoText.speechtotext(apikey=api_key, path=path)
 

        # Now with this data of transcribed audio and time stamps we will process this data and make json file for every video which contains all the chunks made from the video

        createChunks.getJson(data, path)

        # Now we have json file of chunks of every video and now we will be embedding these text chunks into higher dimesnion vector using 'bge-m3:latest' model and create a data-frame containg these embedding along with all the data related to the video

        read_chunks.vectorDataSpace(path)

        # Now we a data base containing all the information related to all the videos and its time for processing user query. The user query is embeded again and cosine similarity is used to fetch the top 5 most relavnt chunks from the data base and the the chunks along with the query is passed to a LLM (Gemini 2.5 Flash) to generate response

        print(processUserQuery.processUserQuery(query=query, api_key=api_key, path=path))

    except Exception as e:
        print('Error occured,', e)    