from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings,HuggingFaceEndpoint,ChatHuggingFace
from langchain_community.vectorstores import FAISS

def split_text(transcript: str):
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200

    )

    chunks = text_splitter.split_text(transcript)

    return chunks 

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def create_vector_store(chunks):

    vector_store= FAISS.from_texts(
        chunks,
        embedding=embedding_model
    )
    return vector_store

def create_retriever(vector_store):
    retriever= vector_store.as_retriever(
        search_kwargs={'k':4}
    )

    return retriever 


llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    temperature=0.5
)

def format_context(docs):

    context= ""

    for doc in docs:
        context += doc.page_content + "\n\n"
    
    return context 

def create_prompt(context,question):

    prompt=f"""

    You are a helpful AI assistant.

    Answer the question ONLY from the provided transcript context.

    If the answer is not present in the context, say:
    "I could not find the answer in the video transcript."

    Transcript Context:
    {context}

    Question:
    {question}

    Answer:
    """
    
    return prompt
    
    
def ask_question(retriever,question):

    relevant_docs= retriever.invoke(question)

    context = format_context(relevant_docs)

    prompt= create_prompt(context,question)

    response= llm.invoke(prompt)

    return response 