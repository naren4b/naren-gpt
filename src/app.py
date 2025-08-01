import streamlit as st
from ollama import chat
from ollama import ChatResponse

st.title("Naren GPT")

if "ollama_model" not in st.session_state:
    st.session_state["ollama_model"] = "llama3"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response: ChatResponse = chat(
            model=st.session_state["ollama_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )
        st.markdown(response.message.content)
    st.session_state.messages.append(
        {"role": "assistant", "content": response.message.content}
    )
