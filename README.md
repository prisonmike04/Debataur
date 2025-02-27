# 🎙️ Debataur: AI-Powered Debating Platform

---

## 📖 Introduction
The **AI-Powered Debating Platform** is designed to facilitate **intelligent, structured debates** between users and an **LLM-driven AI**. It is fine-tuned to generate persuasive, logical arguments and incorporates **real-time fact-checking** using **Wolfram Alpha** and **Wikipedia AI**.

The platform allows users to:
- Engage in **real-time** debates with AI.
- **Verify claims instantly** through live fact-checking.
- Evaluate AI-generated arguments based on logical reasoning, factual accuracy, and coherence.

---

## 🚀 Features
✔️ **AI-Generated Arguments** – The AI constructs logical arguments for and against a given motion.  
✔️ **Real-Time Debate Simulation** – Engage in structured debates with AI.  
✔️ **Multi-Turn Debate Format** – AI dynamically responds to user arguments.  
✔️ **Fine-Tuned for Debate Quality** – Models are trained on debate datasets.  
✔️ **Bias Detection & Logical Coherence** – AI evaluates biases in its own responses.  
✔️ **Live Performance Metrics** – AI rates responses based on logic and persuasiveness.  
✔️ **Real-Time Fact Checking** – Uses **Wolfram Alpha** and **Wikipedia AI** to verify claims.  

---

## 🎯 Project Objective
- Develop an **AI-powered debating assistant** capable of generating persuasive and logical arguments.
- Fine-tune **LLaMA-2-7B** and **Falcon-7B** models for **debate-specific responses**.
- Ensure **factual consistency** using **real-time fact-checking tools**.
- Enable **multi-turn debates** with rebuttals and counterarguments.
- Evaluate **AI debate performance** using **customized metrics**.

---

## 🧠 Models Used
### 🔹 **Base Models**
- **LLaMA-2-7B** (Meta) – Optimized for reasoning and factual correctness.
- **Falcon-7B** (TII) – Suited for generating high-quality natural language responses.

### 🔹 **Fine-Tuning**
- **4-bit Quantization & CPU Offloading** for training efficiency.
- **LoRA & QLoRA** for parameter-efficient fine-tuning.
- **Gradient Checkpointing** to optimize memory usage.

---

## 📊 Dataset
- **Debate-Specific Dataset** from Kaggle and IBM.
- **Argument Quality Datasets** from AI2.
- **Political & Philosophical Debates** scraped from online sources.


---

## 🔧 Fine-Tuning Process
1️⃣ **Baseline Testing** – Evaluate vanilla **LLaMA-2-7B** & **Falcon-7B** on debate prompts.  
2️⃣ **Data Preprocessing** – Tokenization, formatting, and prompt engineering.  
3️⃣ **Fine-Tuning on Debate Datasets** – Using **LoRA/QLoRA** for efficient training.  
4️⃣ **Hyperparameter Tuning** – Optimizing learning rates, batch sizes, and weight decay.  
5️⃣ **Evaluation on Logical Consistency** – Using custom-defined scoring metrics.  
6️⃣ **Bias & Hallucination Control** – Detecting factually incorrect or biased arguments.  

---

## 📏 Evaluation Metrics
📌 **Logical Consistency Score (LCS)** – Measures argument coherence.  
📌 **Factual Accuracy Score (FAS)** – Uses **real-time fact-checking** for AI-generated claims.  
📌 **Bias Detection Score (BDS)** – Identifies politically/socially biased arguments.  
📌 **Engagement Score (ES)** – Evaluates AI's responsiveness in a debate.  

---

---

## 📦 2️⃣ Install Dependencies

**pip install -r requirements.txt
**cd frontend && yarn install

## 🔄 3️⃣ Run Backend
**cd backend
**python main.py

## 🌍 4️⃣ Start Frontend

**cd frontend
**yarn dev

