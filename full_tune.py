from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Load model and tokenizer
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Set padding token and resize embeddings
tokenizer.pad_token = tokenizer.eos_token
model.resize_token_embeddings(len(tokenizer))
model.config.pad_token_id = tokenizer.pad_token_id

# Load dataset
raw_dataset = load_dataset("json", data_files="sample_dataset.jsonl")
dataset = raw_dataset["train"]

# Tokenise
def tokenize(batch):
    tokens = tokenizer(batch["text"], padding="max_length", truncation=True, max_length=1024)
    tokens["labels"] = tokens["input_ids"].copy()
    return tokens

dataset = dataset.map(tokenize, batched=True).remove_columns(["text"])

# Training config
training_args = TrainingArguments(
    output_dir="./finetuned-gpt2",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_strategy="epoch",
    logging_dir="./logs",
    fp16=False,  # Set True if using GPU
)

# Trainer setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Start training
trainer.train()

model.save_pretrained("./finetuned-gpt2-final")
tokenizer.save_pretrained("./finetuned-gpt2-final")
