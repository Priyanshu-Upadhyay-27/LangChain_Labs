import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables (e.g., API keys)
load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite")

# Initialize Streamlit app
st.set_page_config(page_title="Teacher Chatbot", page_icon="📜")
st.title("📚 Assistant AI")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [SystemMessage(content="You are a coder")]

# Display chat messages
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(msg.content)

# Chat input
if prompt := st.chat_input("Ask any question..."):
    # Append user message
    st.session_state.chat_history.append(HumanMessage(content=prompt))
    st.chat_message("user").markdown(prompt)

    # Get model response
    result = model.invoke(st.session_state.chat_history)
    st.session_state.chat_history.append(AIMessage(content=result.content))
    st.chat_message("assistant").markdown(result.content)
