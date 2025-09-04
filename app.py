import streamlit as st
from openai import OpenAI
import time

st.set_page_config(page_title="🩷 Intelligent Excuse Generator 🩷", page_icon="🩷")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("🩷 Intelligent Excuse Generator 🩷")

scenary = st.selectbox("Select scenario:", ["School", "Work", "Social", "Family"])
tone = st.selectbox("Tone:", ["Funny", "Serious", "Professional", "Emotional"])
urgency = st.slider("Urgency level (1=low → 5=high):", 1, 5, 3)
context = st.text_input("Provide brief context for your excuse:", "")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if st.button("Generate Excuse"):
    prompt = f"Generate a {tone.lower()} excuse for a {scenary.lower()} situation. Urgency level: {urgency}. Context: {context}."

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        excuse = response.choices[0].message.content

        st.markdown(
            f"<div style='border:2px solid deeppink; padding:10px; background-color:#ffe6f2;'>{excuse}</div>",
            unsafe_allow_html=True
        )

        st.session_state.history.append(excuse)

    except Exception as e:
        st.error("⚠️ OpenAI error: Try again later or slow down. Details: {}".format(str(e)))

if st.session_state.history:
    st.subheader("📜 Excuse History")
    for idx, h in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**{idx}.** {h}")

