
# News Article Q&A 📰

This project allows users to ask questions about a news article by providing the article's URL. The application uses the LangChain library along with the NVIDIA AI Endpoints to process the article, split it into chunks, create a vector store, and provide answers to user questions based on the article's content.




## Features


- Fetch article text from a provided URL using the WebBaseLoader from LangChain
- Split the article text into chunks using RecursiveCharacterTextSplitter from LangChain
- Create a vector store using FAISS from LangChain and NVIDIAEmbeddings
- Provide a conversational question-answering chain using ChatNVIDIA from LangChain
- Allow users to input questions and display the answers based on the article's content

## Installation

Install my-project with 

```bash
  git clone https://github.com/Chiranth-070/news-teller.git
```

Install requirements

```bash
  pip install -r requirements.txt 
```


Set the environment variables:
- LANG_CHAIN: Your LangChain API key
- NVIDIA_API_KEY: Your NVIDIA API key

Run the application:

```bash
  streamlit run app.py
```
## Usage/Examples

- Enter the URL of the news article you want to ask questions about in the sidebar.
- Click the "Get Article" button to process the article and create the vector store.
- Ask a question in the main section of the application.
- The application will display the answer based on the article's content.


## Screenshots

<img width="1280" alt="Screenshot 2024-09-08 181651" src="https://github.com/user-attachments/assets/c217519b-82b9-456c-a1be-f3e9caaf39c8">

<img width="1280" alt="image" src="https://github.com/user-attachments/assets/98c00043-b3bb-4db5-b05f-85008eb8ebfb">



