import streamlit as st
from parent_agent import ParentAgent

st.set_page_config(
    page_title="AI Multi-Agent System",
    layout="centered"
)

st.title("🧠 AI Multi-Agent Task Manager")

user_input = st.text_area("What do you want to do?")
energy = st.selectbox(
    "Your current energy level",
    ["Low", "Medium", "High"]
)

if st.button("Run AI"):
    if user_input.strip() == "":
        st.warning("Please enter a task.")
    else:
        agent = ParentAgent()
        with st.spinner("AI is thinking..."):
            result = agent.handle(user_input, energy)

        st.success("AI Output")
        st.write(result)
