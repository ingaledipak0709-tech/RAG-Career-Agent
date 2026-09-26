from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_classic.chains import RetrievalQA
from llm_config import create_llm
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def process_pdf(file_path:str="./resume_capabl.pdf"):
    # Step 1 : Document loaders and parsing
    loader = PyPDFLoader(file_path)
    document = loader.load() #parsing the document 

    # step 2 : Text splitter 
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 700, chunk_overlap = 150
    )
    chunks = splitter.split_documents(document)
    return chunks


# step 3 : create vector embeddings 
embeddings = OllamaEmbeddings(model='all-minilm')
# Gemini embeddings/ openai embeddings, huggingface embeddings, 

# step 4 : Store the vector embeddings in a 
# vector store / vector database 
# FAISS, chroma

from langchain_community.vectorstores import FAISS
# vector_store = FAISS.from_texts([" "],embedding = embeddings)

# vector_store = Chroma(
#     embedding_function=embeddings,
#     collection_name="resume_data",
#     persist_directory="./rag_database"
# )

# load document, split,embeddings,save in vectorstore 
def ingest_data():
    chunks = process_pdf()
    vector_store = FAISS.from_documents(chunks,embeddings)
    # vector_store.add_documents(chunks)
    print(" Data ingested successfully")
    return vector_store

def rag_chain(query,vector_store):
    #step 5 : create a retriever to extract 
                    # top 3 relevant chunks
    llm = create_llm() 
    retriever = vector_store.as_retriever(search_kwargs={"k":3}) # semantic search 

    # step 6 : create a RAG chain 
    chain = RetrievalQA.from_chain_type(
        llm = llm, retriever = retriever 
    )
    # step 7 : Return the results from the rag system by invoking the llm 
    return chain.invoke({"query":query})

# Function calls to run the RAG script

if __name__ == "__main__": 
    vector_store = ingest_data()   
    query = input("Enter your query :")
    response = rag_chain(query,vector_store)
    print(response)