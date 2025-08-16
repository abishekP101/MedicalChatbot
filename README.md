# MedicalChatbot

A conversational AI chatbot for medical queries, built using Retrieval-Augmented Generation (RAG) architecture and LangChain. The chatbot provides accurate, helpful information on various medical conditions, treatments, and general health advice, prioritizing clarity, brevity, and patient safety.

## Features

- **RAG-based Chatbot:** Combines a large language model (LLM) with document retrieval for up-to-date, contextually accurate answers.
- **Web Interface:** User-friendly chat UI powered by Flask and Bootstrap.
- **Medical Context Awareness:** Pulls information from a curated medical knowledge base to answer user questions.
- **Safe & Reliable Responses:** Limits responses to three sentences, recommends remedies/medicines, and states “I don’t know” when uncertain.
- **Extensible Backend:** Uses LangChain, Pinecone for vector search, and Groq’s Llama3-70B model.
- **Jupyter Notebooks:** Included for research, prototyping, and model experimentation.

## Getting Started

### Prerequisites

- Python 3.8+
- [Pinecone](https://www.pinecone.io/) account and API key
- [Groq](https://groq.com/) API key
- Required Python packages (see `setup.py` and Jupyter notebooks for details)

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/abishekP101/MedicalChatbot.git
   cd MedicalChatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is missing, install from `setup.py` or use Jupyter/research notebooks for exploration.)*

3. Set your API keys in a `.env` file:
   ```
   PINECONE_API_KEY=your_pinecone_api_key
   GROQ_API_KEY=your_groq_api_key
   ```

### Running the Chatbot

```bash
python app.py
```
Visit [http://localhost:8080](http://localhost:8080) in your browser to interact with the chatbot.

## File Structure

```
.
├── app.py                # Flask application
├── src/
│   ├── helper.py         # Model download utilities
│   ├── prompt.py         # System prompt template
│   └── __init__.py
├── templates/
│   └── chat.html         # Chat UI (Bootstrap/jQuery)
├── static/
│   └── style.css         # Custom styles for chat
├── research/
│   └── trials.ipynb      # Prototyping & experiments
├── setup.py              # Package configuration
├── README.md
└── LICENSE
```

## Core Technologies

- **LangChain:** Orchestrates LLM, retrieval, and prompt engineering.
- **Groq Llama3-70B:** High-performance LLM for medical Q&A.
- **Pinecone:** Fast vector database for document retrieval.
- **Flask:** Lightweight web server for chat UI.
- **Bootstrap/jQuery:** Responsive frontend design.

## How It Works

- User message is received via the chat interface.
- The backend retrieves relevant medical documents using Pinecone.
- Context and user input are fed to the LLM (Groq/Llama3) via a structured system prompt.
- The chatbot returns a concise, evidence-based answer or states if uncertain.

## Customization

- Expand the medical corpus in your Pinecone index for richer knowledge.
- Tune the system prompt in `src/prompt.py` for response style.
- Update frontend (`templates/chat.html`, `static/style.css`) for branding or improved UX.

## License

This project is licensed under the MIT License.

## Author

Abishek Prasad  
[GitHub Profile](https://github.com/abishekP101)

---

*Disclaimer: This chatbot is for informational purposes only and does not constitute medical advice. Always consult a healthcare professional for medical concerns.*
