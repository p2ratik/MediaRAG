# RAG based AI teaching assistant

This AI project is used to extract information/summary of any course or any specific video using RAG setup.


## 📦 Installation
This project requires a python environment of 3.9 or above .
### Clone the repo to your local machine
```bash
git clone https://github.com/p2ratik/MediaRAG.git
cd MediaRAG
mkdir Videos
```
### Install all the dependencies
```bash
pip install -r requirements.txt
ollama pull bge-m3:latest
```
## 🚀 How to use the model

- Upload all your videos to the Videos folder

- Make sure that the video names are in this format: sampleVideo 01.mp4/webm/mov

- Once the videos are uploaded, open your terminal in the project folder and run this command.

### For Windows 
```bash
cp .env .env.example
python main.py
```
### For MacOS/Linux/Debian
```
cp .env .env.example
python3 main.py
```
### Example Configuration
```
API_KEY=your_gemini_api_key
PATH_DIR=path of your directory
```

- Replace your_gemini_api_key with a actual google gemini api key.

- You can make your very own free api key
here:
https://aistudio.google.com/apikey

- Replace path of your directory with the actual path of your project folder:
Example : E:\Projects\RAG_model 
- If everything is followed correctly , the desired output will be seen within few seconds. 

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Author
Pratik Chakraborty 

