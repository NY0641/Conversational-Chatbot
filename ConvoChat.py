import streamlit as st
from openai import OpenAI

# --------------------------------------------------
# Page config MUST be first Streamlit command
# --------------------------------------------------
st.set_page_config(
    page_title="Convo Chat",
    page_icon="🔮",
    layout="centered"
)

# --------------------------------------------------
# Initialize OpenAI client
# --------------------------------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# --------------------------------------------------
# UI Header
# --------------------------------------------------
st.title("🧠 GenX Chat")
st.markdown("**Powered by Generative AI** ⚡")

system_prompt = (
    "You are a helpful, factual, and safe assistant. "
    "Respond clearly, concisely, and naturally. "
    "Do not fabricate information or provide unsafe instructions. "
    "Give general guidance only for medical, legal, or financial topics."
)

# --------------------------------------------------
# Initialize session history
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": system_prompt}
    ]

# --------------------------------------------------
# Display chat history
# --------------------------------------------------
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# --------------------------------------------------
# User input
# --------------------------------------------------
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Call LLM
    response = client.responses.create(
        model="gpt-5.2",
        input=st.session_state.messages
    )

    bot_reply = response.output_text

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    # Display assistant reply
    with st.chat_message("assistant"):
        st.write(bot_reply)

# --------------------------------------------------
# Disclaimer
# --------------------------------------------------
st.markdown(
    "<hr><small><i>"
    "Disclaimer: This chatbot provides general information only and is not a substitute "
    "for professional medical, legal, or financial advice."
    "</i></small>",
    unsafe_allow_html=True
) 
