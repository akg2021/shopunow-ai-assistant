# ShopUNow Agentic AI Assistant - Capstone Project

**Project Type:** Hands-on Capstone Project  
**Organization:** Analytics Vidya  
**Learner Name:** Arun Goenka

## Project Description

This capstone project builds an **Intelligent AI Assistant** for ShopUNow, a retail company. It combines intelligent sentiment detection, query decomposition, and dynamic routing with Retrieval-Augmented Generation (RAG) to efficiently handle diverse user inquiries.The assistant leverages:
- **Generative AI - OpenAI LLM**
- **RAG (Retrieval-Augmented Generation) - Chromnadb**
- **JSON-based Knowledge base**
- **LangGraph and LangChain for Agents and Routing**

The system handles queries for six ShopUNow departments, covering frequently asked questions by:
- **External customers** (Products, Shipping & Delivery, Billing & Payment)
- **Internal employees** (HR, IT Support, Facilities & Administration)

### Key Features (Mandatory):
1. **Six Departments and related queries covered**: 3 External Customers & 3 Internal Employees
2. **FAQ Datasets - Knowledge Base**: LLM-generated knowledge base for six departments with 25 FAQs for each department
3. **Vector Database**: Chromadb vector database with department metadata for retrieval
4. **Router-based Agentic RAG System**: Accepts user query, analyses and decomposes, query, analyses and decomposes and routes queries to HR, IT, Facilities, Products, Billing, or Shipping
    - **Query Sentiment Analysis**: Detects negative sentiment and escalates appropriately
    - **Query Decomposition**: Simplifies complex queries related to multiple departments into subqueries linked to individual departments
    - **Dynamic Multi-Department Routing**: Routing of subqueries to related departments for RAG based responses generation
    - **Multi-department Response compilation**:  LLM based Responses compilation 
    - **Human Escalation**: Negative Sentiment or no response for any departments
5. **Testing of system with sample queries**

### Advanced Features (Streach Goals): 
1. **Multi-User - Conversation Memory and Session Management**: Each user gets an isolated conversation session; Maintains context across multiple exchanges
2. **Responsive UI**: Clean, modern Streamlit interface
3. **Download Chat History**: Users can export their conversation


## Agentic RAG Architecture


![Agentic RAG Architecture](https://i.imgur.com/bLCdxCI.png)


## Updated Agentic RAG Architecture
![Enhanced Agentic RAG Architecture](https://i.imgur.com/10fyrT2.png)


## Agent RAG Tools Stack
 **- LLM GPT-4o**
 **- LangGraph**
 **- LangChain**
 **- Python**
 **- Chromadb**
 **- Streamlit (UI)**

 ## Future Enhancements

- [ ] Add user authentication
- [ ] Implement real email notifications
- [ ] Add analytics dashboard
- [ ] Support file uploads
- [ ] Multi-language support
- [ ] Voice input/output


#########################################################################################################################
## Prerequisites

- Python 3.9+
- OpenAI API key
- GitHub account
- Streamlit Cloud account

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/shopunow-ai-assistant.git
cd shopunow-ai-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run Locally

```bash
streamlit run streamlit_app.py
```

Visit `http://localhost:8501` in your browser.


## Deploy to Streamlit Cloud

### Step 1: Prepare GitHub Repository

1. Create a new repository on GitHub
2. Push your code to GitHub

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Connect your GitHub account
4. Select `streamlit_app.py` from `shopunow-ai-assistant` repository

### Step 3: Configure Secrets

1. In Streamlit Cloud dashboard, go to **App Settings → Secrets**
2. Add your secrets:

```toml
OPENAI_API_KEY = "sk-your-actual-openai-key"

3. Click **Save**

### Step 4: Deploy

Click **Deploy!** and wait for the app to build (2-5 minutes).

## Project Structure

```
shopunow-ai-assistant/
│
├── streamlit_app.py          # Main Streamlit interface
├── shopunow_agent.py          # Agent logic and core functionality
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .streamlit/
│   └── secrets.toml          # Local secrets
└── .gitignore                # Git ignore rules
```

## Configuration

### Agent Settings

Edit `shopunow_agent.py` to customize:

```python
class Config:
    LLM_MODEL = "gpt-4o"              # Change model
    LLM_TEMPERATURE = 0                # Adjust creativity
    EMBEDDING_MODEL = "text-embedding-3-small"
```

### Departments

To add/modify departments, edit the `generate_knowledge_base()` function in `shopunow_agent.py`.

## Usage

### Basic Chat

1. Open the app - https://appapppy-bdcjpaqyqulyvtcqk95ik2.streamlit.app/
2. Type your question in the chat input
3. Press Enter or click Send
4. Get instant AI-powered responses

### Multi-Department Queries

The agent automatically detects and routes multi-department queries:

- **Single dept**: "What laptops do you have?" → Products
- **Multi dept**: "What laptops and shipping time?" → Products + Shipping

### Download Chat History

1. Click **Download Chat** in the sidebar
2. (Optional) Enter your email
3. Click **Download History**
4. Save the TXT file