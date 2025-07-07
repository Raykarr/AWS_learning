import streamlit as st
from llm_handler import call_llm
from s3_uploader import upload_reflection
import json

st.set_page_config(layout="wide",page_title="Clarity Mirror", page_icon="🪞")

# Load config
try:
    with open("config.json") as f:
        config = json.load(f)
except Exception as e:
    st.error("⚠️ Failed to load config.json")
    st.stop()

st.title("🪞 Clarity Mirror")
st.markdown("Reflect deeply on your thoughts using an LLM-powered assistant.")

# Input box
user_input = st.text_area("🧠 Write your thought here:", height=100)

if st.button("Reflect"):
    if not user_input.strip():
        st.warning("Please write something first.")
        st.stop()

    with st.spinner("Thinking deeply..."):
        try:
            reflection = call_llm(user_input, config)
            st.success("Reflection complete!")
        except Exception as e:
            st.error(f"LLM Error: {e}")
            st.stop()

        # Show result
        st.subheader("💬 Structured Reflection:")
        st.markdown(reflection)

        # Upload to S3
        try:
            upload_reflection(user_input, reflection, config)
            st.info("🟢 Reflection saved to S3.")
        except Exception as e:
            st.warning(f"S3 upload failed: {e}")
