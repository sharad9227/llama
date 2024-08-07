from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the tokenizer and model from Hugging Face
tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    summary_ids = model.generate(inputs['input_ids'], max_length=50, min_length=25, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
