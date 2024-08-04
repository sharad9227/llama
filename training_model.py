import pandas as pd
from datasets import Dataset
from sklearn.model_selection import train_test_split
from langchain import DataLoader
from transformers import Trainer,TrainingArguments
from transformers import LLamaTokenizer,LLamaForSequenceClassification

#Load the csv file 
file_path = "//provide path"
data = pd.read_csv(file_path);

#Split data into training and testing sets
train_data, test_data = train_test_split(data, test_size=0.2,random_state=42)
#Convert to Hugging face datasets

train_dataset = Dataset.from_pandas(train_data)
test_dataset = Dataset.from_pandas(test_data)
train_loader = DataLoader(train_dataset,batch_size=8,shuffle =True)
test_loader = DataLoader(test_dataset,batch_size=8)

#Define training arguments
training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps =10
        )
#Load Tokenizer and model
tokenizer = LLamaTokenizer.from_pretrained('meta-llama/LLaMa-3B')

model = LLamaForSequenceClassification.from_pretrained('meta-llama/LLaMA-3B')

#Configure the model for number of unique solutions.
model.config_num_labels = len(data['solution'].unique())
#Define the trainer
trainer= Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset = test_dataset,
        tokenizer = tokenizer
)

#Train the model
trainer.train()

#Evaluate the model
results =trainer.evaluate()
print(results)