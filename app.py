import streamlit as st
import google.generativeai as genai

# Gemini Look & Branding Hide
st.set_page_config(page_title="Mihir AI", layout="centered")
st.markdown("<style>#MainMenu, footer, header {visibility: hidden;}</style>", unsafe_allow_html=True)

# API Setup
genai.configure(api_key="AIzaSyCPFQf0hfAN6xHN-sRnU00UiSc1nDVsn2I")
model = genai.GenerativeModel('gemini-1.5-flash')

# 1. SIGN-UP SCREEN
if "user_name" not in st.session_state:
    st.markdown("<h1 style='text-align: center;'>🤖 Mihir AI</h1>", unsafe_allow_html=True)
    name = st.text_input("Apna Naam Likhein (Sign-up):", placeholder="Example: Mihir")
    if st.button("Start Now"):
        if name:
            st.session_state.user_name = name
            st.rerun()
else:
    # 2. MAIN APP INTERFACE
    st.markdown(f"<h1 style='text-align: center; color: #4A90E2;'>Mihir AI</h1>", unsafe_allow_html=True)
    
    # Feature Boxes
    if "messages" not in st.session_state or len(st.session_state.messages) == 0:
        st.write(f"Hello **{st.session_state.user_name}**! Main aapki kya madad karun?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("☸️ Kundali Reading"): st.session_state.temp_input = "Analyze my Kundali"
        with col2:
            if st.button("📚 Study Help"): st.session_state.temp_input = "Help me with studies"

    # Chat Logic
    if "messages" not in st.session_state: st.session_state.messages = []
    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.markdown(m["content"])

    if prompt := st.chat_input("Ask Mihir AI..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        with st.chat_message("assistant"):
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
