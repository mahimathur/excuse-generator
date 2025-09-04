import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.markdown("<h1 style='color:deeppink;'>🩷 Intelligent Excuse Generator 🩷</h1>", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = []

scenary = st.selectbox("Select scenario:", ["Work", "School", "Social", "Family"])
tone = st.selectbox("Tone:", ["Formal", "Casual", "Funny", "Dramatic"])
urgency = st.slider("Urgency level (1=low → 5=high):", 1, 5, 3)
context = st.text_area("Provide brief context for your excuse:")

if st.button("Generate Excuse"):
    prompt = f"Generate a {tone.lower()} excuse for a {scenary.lower()} situation. Urgency level: {urgency}. Context: {context}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    excuse = response.choices[0].message['content']
    st.markdown(f"<div style='border:2px solid deeppink; padding:10px; background-color:#ffe6f2;'>{excuse}</div>", unsafe_allow_html=True)
    st.session_state.history.append(excuse)

if st.session_state.history:
    st.markdown("### Past Excuses:")
    for i, ex in enumerate(st.session_state.history[::-1], 1):
        st.markdown(f"{i}. {ex}")

st.markdown("### Proof Generator (Coming Soon!)")
proof_type = st.selectbox("Proof type:", ["Chat screenshot", "Location log", "Document"])
st.text(f"→ Here we would generate a fake {proof_type} to support the excuse.")

st.markdown("<hr><center><small style='color:deeppink;'>Made by a student, with love 💗</small></center>", unsafe_allow_html=True)
