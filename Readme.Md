Step1: Activate Your Virtual Environment

- Ensure your virtual environment is activated:
    source langchain_env/bin/activate


Step2: Install Required Libraries
         pip install pandas langchain transformers sentence-transformers
    


Step:3 Load and Preprocess CSV Data

        - Created a script to load the CSV data and compute embeddings:

Step:4 Define Retrieval Function

        - Implement a function to retrieve relevant information based on the query:

Step:5 Load Hugging Face Generative Model

        - Load a Hugging Face model for generating responses:

Step:6 Combine Retrieval and Generation

        - Integrate the retrieval and generative components into a single RAG system:


Example Usage

Demonstrate the system with an example query:


query = "What should I take for a runny nose due to a cold?"
response = rag_system(query)
print(response)