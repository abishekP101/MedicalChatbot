# MedicalChatbot

A conversational AI chatbot for medical queries, built using Retrieval-Augmented Generation (RAG) architecture and LangChain. The chatbot provides accurate, helpful information on various medical conditions, treatments, and general health advice, prioritizing clarity, brevity, and patient safety.

## Features

- **RAG-based Chatbot:** Combines a large language model (LLM) with document retrieval for up-to-date, contextually accurate answers.
- **Web Interface:** User-friendly chat UI powered by Flask and Bootstrap.
- **Medical Context Awareness:** Pulls information from a curated medical knowledge base to answer user questions.
- **Safe & Reliable Responses:** Limits responses to three sentences, recommends remedies/medicines, and states “I don’t know” when uncertain.
- **Extensible Backend:** Uses LangChain, Pinecone for vector search, and Groq’s Llama3-70B model.
- **Jupyter Notebooks:** Included for research, prototyping, and model experimentation.
- **Docker Support:** Easily deploy and run the chatbot in a containerized environment.
- **GitHub Actions:** Automated workflows for testing, linting, and deployment.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker (for containerized deployment)
- [Pinecone](https://www.pinecone.io/) account and API key
- [Groq](https://groq.com/) API key
- Required Python packages (see `setup.py` and Jupyter notebooks for details)

### Installation (Local)

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

### Running the Chatbot (Local)

```bash
python app.py
```
Visit [http://localhost:8080](http://localhost:8080) in your browser to interact with the chatbot.

---

## Docker

To run the chatbot using Docker:

1. Build the Docker image:
   ```bash
   docker build -t medical-chatbot .
   ```
2. Run the container (make sure to set up your `.env` file or pass environment variables):
   ```bash
   docker run --env-file .env -p 8080:8080 medical-chatbot
   ```
3. Access the chatbot at [http://localhost:8080](http://localhost:8080).

#### Notes

- The provided `Dockerfile` ensures reproducible builds and isolates dependencies.
- Customize the Dockerfile for GPU support or additional packages as needed.

---

## GitHub Actions

This repository uses GitHub Actions for CI/CD automation:

- **Linting & Testing:** Automatically checks code style and runs tests on every push/pull request.
- **Build & Deploy:** Optionally build Docker images and deploy to cloud providers or registries.
- **Notebook Checks:** Can be extended to validate Jupyter notebook execution.

To customize workflows, edit the files in `.github/workflows/`. Example workflow steps include installing dependencies, running tests, checking notebooks, and building Docker images.

---

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
├── Dockerfile            # Container build configuration
├── .github/
│   └── workflows/
│       └── main.yml      # GitHub Actions workflow
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
- **Docker:** Containerized deployment.
- **GitHub Actions:** Workflow automation and CI/CD.

## How It Works

- User message is received via the chat interface.
- The backend retrieves relevant medical documents using Pinecone.
- Context and user input are fed to the LLM (Groq/Llama3) via a structured system prompt.
- The chatbot returns a concise, evidence-based answer or states if uncertain.

## Customization

- Expand the medical corpus in your Pinecone index for richer knowledge.
- Modify workflows under `.github/workflows/` for your CI/CD needs.
- Adjust Dockerfile for specialized deployments.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

- MedicalChatbot does **not** replace professional medical advice, diagnosis, or treatment.
- Always consult a qualified healthcare provider for medical concerns.
- Data privacy and ethical use are strictly enforced.

## Contact

For issues, feature requests, or feedback, please open a [GitHub Issue](https://github.com/abishekP101/MedicalChatbot/issues) or reach out to [Abishek P](mailto:your-email@example.com).

---

*Empowering healthcare with accessible, intelligent technology.*
