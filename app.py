import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pyperclip

# Page Settings
st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 AI-Powered Language Translation Tool")

st.write("Translate text into multiple languages instantly!")

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja"
}

# Text Input
text = st.text_area("✍ Enter Text Here")

# Character Count
st.write("🔢 Character Count:", len(text))

# Target Language
target_lang = st.selectbox(
    "🌐 Select Target Language",
    list(languages.keys())
)

# Translation History
if "history" not in st.session_state:
    st.session_state.history = []

# Translate Button
if st.button("🚀 Translate"):

    if text.strip() != "":

        try:
            # Translation
            translated_text = GoogleTranslator(
                source='auto',
                target=languages[target_lang]
            ).translate(text)

            # Show Output
            st.subheader("✅ Translated Text")
            st.write(translated_text)

            # Copy Button
            if st.button("📋 Copy Text"):
                pyperclip.copy(translated_text)
                st.success("Copied Successfully!")

            # Text-to-Speech
            st.subheader("🔊 Listen Translation")

            tts = gTTS(
    text=translated_text,
    lang=languages[target_lang]
)
            tts.save("output.mp3")

            audio_file = open("output.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")

            # Save History
            st.session_state.history.append(translated_text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("⚠ Please enter text.")

# History Section
if st.session_state.history:

    st.subheader("📝 Translation History")

    for idx, item in enumerate(st.session_state.history, 1):
        st.write(f"{idx}. {item}")