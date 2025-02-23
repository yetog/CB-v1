import sys
import os
import streamlit as st

# Ensure Python recognizes "src" as a module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import backend function
try:
    from src.backend import query_ionos
except ModuleNotFoundError as e:
    st.error(f"Module import error: {e}")
    st.stop()

# Streamlit UI
st.title("🚀 IONOS AI Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Ask me anything..."):
    st.session_state["messages"].append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            response = query_ionos(user_input)
            st.markdown(response)
            st.session_state["messages"].append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Error querying IONOS API: {e}")
