# LangChain Labs 🚀

This repository contains my **learning journey with LangChain**, organized topic-wise for clarity and scalability.  
It includes fundamental concepts, practical experiments, and will gradually evolve into **RAG applications, Agents, and real-world projects**.  

---

## 📂 Repository Structure

```text
LangChain_Notebook/
│── main.py                     # Entry point for testing concepts
│── Know_your_gem_models.py     # Script for exploring Gemini models
│── requirements.txt             # Python dependencies
│
├── Chains/                     # Building and linking multiple LLM calls
├── ChatModels/                  # Working with conversational models
├── Doc_Loaders/                 # Loading documents into LangChain
├── EmbeddingModels/             # Creating embeddings for text
├── LLms/                        # Core LLM usage
├── Output_Parser/               # Parsing structured outputs
├── Prompts/                     # Prompt engineering & templates
├── Runnables/                   # Runnable sequences
├── Structured_Output/           # Handling structured generation
├── Text_Splitters/              # Splitting documents into chunks
├── Vector_Database/             # Vector DB integrations (FAISS, Chroma, etc.)
└── Retrievers/                  # (Upcoming) Information retrieval methods
```

---

## 📌 Learning Roadmap

✔️ **Current Progress**  
- Learned basics of LangChain components (Chains, Models, Prompts, Parsers, etc.)  
- Explored embeddings, vector databases, and structured outputs  

🟡 **Next Steps**  
1. **Retrievers** – BM25, semantic search, hybrid retrievers  
2. **RAG (Retrieval-Augmented Generation)** – combine retrievers + vector DB + LLMs  
3. **Agents** – enable decision-making with multiple tools (retrievers, APIs, etc.)  
4. **Projects** – build real-world apps (chat with PDFs, Q&A bots, multi-tool agents)  
5. **Advanced Topics** – Memory, LangGraph, Multi-modal AI, Deployment  

---

## ⚡ How to Use

Clone the repository:
```bash 
git clone https://github.com/Priyanshu-Upadhyay-27/LangChain_Notebook.git
cd LangChain_Notebook
```

Create a virtual environment and install dependencies:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

```bash
pip install -r requirements.txt
```

## 📘 Resources

- LangChain Documentation

- CampusX (Nitish Singh Sir)

- LangSmith
 – Debugging & tracing LLM apps

- Awesome LangChain Projects

## 📄 License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) – see the LICENSE
 file for details.
