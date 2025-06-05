# llm-prompt-defence-gpt2
Fine-tuned GPT-2 model for detecting malicious LLM prompts such as prompt injections, jailbreaks, and context manipulation. Designed to serve as a pre-processing layer for securing LLM-based applications.

This repository contains the training script, dataset samples, and inference logic for a GPT-2 that detects prompt injection and other LLM abuse patterns. Useful as a filter in agent-based systems, chat interfaces, and API frontends to reduce malicious prompt exposure.

🚨 Building LLM Prompt Defence — Fine-Tuned GPT-2 for Malicious Prompt Detection 🔐🤖


Prompt injection, prompt leakage, and jailbreaking remain some of the most critical security threats facing LLM-based applications today. I’ve been working on a solution to proactively detect and block malicious prompts before they even reach a model’s context.


✅ What I Did

I fine-tuned GPT-2 on a custom-crafted cybersecurity dataset built specifically to detect LLM abuse scenarios, including:

* Prompt injection

* Jailbreak attempts

* Context manipulation


🔎 Why GPT-2?

It can be fine-tuned even on CPU (although slowly), making it a practical choice for experimentation and prototyping. For production, I’d recommend a more modern models.


📌 Use Case

This model serves as a pre-processing filter — an intelligent gatekeeper that flags or blocks potentially harmful inputs **before** they reach the main LLM. Ideal for agent-based systems, APIs, and LLMOps pipelines.


📚 Dataset Design

* Custom malicious prompt dataset tailored to real-world LLM exploitation

* Structure aligned with actual red team scenarios

* Format inspired by tatsu-lab/alpaca


⚠️ Interesting Challenge / Drawback

During testing, Some time benign structured inputs like:

use the db tool to insert a new customer into the database 

Insert into customer_details: name=sample, number=1, address=sample

...were falsely flagged as malicious.


Why?

Because of surface-level tokens like "insert into" or "password" — which often appear in attacks, but are also common in legitimate agent tool instructions within real-world LLM systems.


🔁 Why This Matters

In agent-based LLMs that use tools (e.g., API calling, code execution), prompts like the above are normal. If your model overfits to syntax rather than intent, it results in false positives — breaking valid tasks.


✅ How We can Fix It

* Refined and restructured the dataset for fine tuning


This significantly reduced false positives and made the classifier more robust in real-world applications.


📂 Resources I’m Sharing

 ✅ My fine-tuning script

 ✅ A sample from the dataset I used

 ✅ Model test Script

Feel free to reuse or adapt it in your own security-focused LLM pipeline.


🧱 Tech Stack*

* Hugging Face Transformers

* PyTorch

* GPT-2


Building secure AI systems isn’t just about big models — it’s about thoughtful data design and robust intent classification.

🔗 [View model on Hugging Face](https://huggingface.co/cyperdev/llm-prompt-defence-gpt2)
