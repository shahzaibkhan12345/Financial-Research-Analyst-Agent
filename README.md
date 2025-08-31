# Financial-Research-Analyst-Agent

This project is a Streamlit web application that leverages a multi-agent system built with **CrewAI** to automate the process of financial research and blog post creation. Users can enter a topic, and a team of AI agents will research it and write a comprehensive article.


## ✨Architecture <img width="560" height="484" alt="Capture" src="https://github.com/user-attachments/assets/857b45b0-1096-468b-8ec3-ae9f3909a06c" />


- **Automated Research**: A dedicated AI agent scours the web for the latest information on any given topic.
- **Content Generation**: A specialized AI writer crafts an engaging and structured blog post based on the gathered research.
- **Interactive UI**: A clean and simple web interface built with Streamlit for easy interaction.
- **Downloadable Output**: Download the generated blog post as a Markdown (`.md`) file.
- **Powered by CrewAI**: Demonstrates a practical implementation of a multi-agent workflow.

## ⚙️ How It Works

The application employs a two-agent CrewAI setup to divide and conquer the task:

1.  **Senior Research Analyst**: This agent is responsible for using search tools (Serper) to find, analyze, and synthesize relevant information about the user-provided topic.
2.  **Senior Content Writer**: This agent takes the structured research from the analyst and writes a comprehensive and coherent blog post, formatted for readability.

The agents work sequentially, ensuring the content is based on solid research.

## 🛠️ Tech Stack

- **Framework**: Streamlit
- **AI Agents**: CrewAI
- **LLM Integration**: LangChain with Google Gemini
- **Search Tool**: Serper

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

- Python 3.8+
- An API Key from Google AI Studio for Gemini.
- An API Key from Serper for the search functionality.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Financial-Research-Analyst-Agent.git
cd Financial-Research-Analyst-Agent
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
*(Note: If a `requirements.txt` file is not available, you can create one with the following content: `streamlit`, `crewai`, `python-dotenv`, `langchain-google-genai`)*

### 4. Set Up API Keys

Create a file named `.env` in the root of the project directory and add your API keys:

```env
GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
SERPER_API_KEY="YOUR_SERPER_API_KEY"
```

### 5. Run the Application

```bash
streamlit run app.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).
