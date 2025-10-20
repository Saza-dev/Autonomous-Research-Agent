# Autonomous Research Agent 🤖🔍

An autonomous AI agent built with **LangGraph** and **LangChain** designed to perform comprehensive research on any given topic. It mimics a human research process by planning, searching the web, synthesizing information, and writing a final, structured report.

---

## Features

* **Dynamic Planning**: Creates a step-by-step research plan before execution.
* **Web-Enabled**: Integrates with search tools (Google Search) to gather up-to-date information.
* **Iterative Synthesis**: Reflects on gathered information and refines its search queries to dig deeper.
* **Structured Output**: Generates a final, comprehensive report based on its findings.
* **Stateful & Cyclic**: Uses LangGraph to manage a complex, multi-step agentic workflow.

---

## Tech Stack

* **Python 3.10+**
* **LangGraph**: For building the stateful, multi-agent graph.
* **LangChain**: For core components, tool integrations, and LLM wrappers.
* **Groq**: For the core reasoning and generation models.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/saza-dev/Autonomous-Research-Agent.git
cd Autonomous-Research-Agent
````

### 2\. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3\. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4\. Set Up Environment Variables

Create a `.env` file in the root of the project and add your API keys:

```
GROQ_API_KEY="..."
```

To run the agent:

```bash
streamlit run main.py
```
