from Rag_langchain import retrieve_info
from loadhugging import generate_response
def rag_system(query):
    retrieved_info = retrieve_info(query)
    prompt = f"Based on the symptoms of {retrieved_info['Symptom']} for {retrieved_info['Health Issue']}, the common medicines are {retrieved_info['Common Medicines']}. Please provide detailed advice."
    response = generate_response(prompt)
    return response
query = "What should I take if I have leg pain?"
response = rag_system(query)
print(f"""
Result:
{response}
""")
