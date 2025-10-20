import streamlit as st
from src.agent.graph import app
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage
from src.prompts.system_prompts import AGENT_SYSTEM_PROMPT
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

st.title("Autonomous Research Agent")
st.caption("Enter a research question to start the autonomous agent.")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display past messages from chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("ai"):
            st.write(message.content)

# Handle user input
if user_question := st.chat_input("Ask a research question..."):
    # Add user question to chat history and display it
    st.session_state.chat_history.append(HumanMessage(content=user_question))
    with st.chat_message("user"):
        st.write(user_question)

    # Start the agent's thinking process
    with st.chat_message("ai"):
        with st.spinner("Agent is thinking, fetching papers, and reading..."):
            
            # Create a dropdown expander 
            with st.expander("Show agent's thought process"):
                steps_container = st.empty()
                steps_log = []

            # Define the initial state for the agent
            initial_state = {
                "messages": [
                    SystemMessage(content=AGENT_SYSTEM_PROMPT),
                    HumanMessage(content=user_question)
                ],
                "user_question": user_question,
                "research_summary": "" 
            }

            final_answer = ""
            # Stream the agent's execution to get live updates
            for chunk in app.stream(initial_state):
                for node_name, node_state in chunk.items():
                    if 'messages' in node_state:
                        message = node_state['messages'][-1]
                        if isinstance(message, AIMessage) and message.tool_calls:
                            tool_name = message.tool_calls[0]['name']
                            tool_args = message.tool_calls[0]['args']
                            steps_log.append(f"**Tool Call:** `{tool_name}` with arguments `{tool_args}`")
                            steps_container.info("\n\n".join(steps_log))
                        elif isinstance(message, ToolMessage):
                            steps_log.append(f"**Tool Output:** Received output from `{message.name}`.")
                            steps_container.info("\n\n".join(steps_log))
                        elif isinstance(message, AIMessage) and not message.tool_calls:
                            final_answer = message.content

            st.write(final_answer)
            st.session_state.chat_history.append(AIMessage(content=final_answer))
