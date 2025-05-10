import streamlit as st
import random

# List of Kana words (Hiragana/Katakana), categories, and romaji
kana_words = [
    {"kana": "りんご", "romaji": "ringo", "type": "hiragana", "meaning": "apple"},
    {"kana": "すし", "romaji": "sushi", "type": "hiragana", "meaning": "sushi"},
    {"kana": "アニメ", "romaji": "anime", "type": "katakana", "meaning": "anime"},
    {"kana": "テレビ", "romaji": "terebi", "type": "katakana", "meaning": "TV"},
    {"kana": "ねこ", "romaji": "neko", "type": "hiragana", "meaning": "cat"},
    {"kana": "ゲーム", "romaji": "geemu", "type": "katakana", "meaning": "game"},
]

# Choose two random words (one hiragana, one katakana)
hiragana_word = random.choice([w for w in kana_words if w["type"] == "hiragana"])
katakana_word = random.choice([w for w in kana_words if w["type"] == "katakana"])

# Display the story
st.title("Kana Mad Libs 🎌")
st.write("Fill in the blanks by typing the **romaji** of the kana words shown.")

# Story with kana blanks
st.markdown(f"""
Today, I ate a delicious **{hiragana_word["kana"]}** and then watched a **{katakana_word["kana"]}** on TV.
""")

# User input
user_input_h = st.text_input(f"What is the romaji for {hiragana_word['kana']}?")
user_input_k = st.text_input(f"What is the romaji for {katakana_word['kana']}?")

# Check answers
if st.button("Submit"):
    correct_h = user_input_h.strip().lower() == hiragana_word["romaji"]
    correct_k = user_input_k.strip().lower() == katakana_word["romaji"]

    if correct_h and correct_k:
        st.success("Perfect! 🎉 You got both correct!")
    else:
        if not correct_h:
            st.error(f"❌ {hiragana_word['kana']} is **{hiragana_word['romaji']}** ({hiragana_word['meaning']})")
        if not correct_k:
            st.error(f"❌ {katakana_word['kana']} is **{katakana_word['romaji']}** ({katakana_word['meaning']})")
