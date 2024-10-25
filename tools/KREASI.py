import streamlit as st
import random
import time

# Sample sentences for practice
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect.",
    "Typing fast is a valuable skill.",
    "Streamlit makes it easy to create web apps.",
    "Python programming is both fun and powerful.",
]

# Select a random sentence
if "target_sentence" not in st.session_state:
    st.session_state.target_sentence = random.choice(sentences)

if "start_time" not in st.session_state:
    st.session_state.start_time = None

if "typing_complete" not in st.session_state:
    st.session_state.typing_complete = False

# Title and instructions
st.title("Typing Practice")
st.write("Type the sentence as quickly and accurately as possible.")

# Display the target sentence
st.write("### Sentence to Type:")
st.write(f"`{st.session_state.target_sentence}`")

# Input for user's typed sentence
user_input = st.text_input("Start typing here:")

# Start timing when the user begins typing
if user_input and st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# Check if the user finished typing
if user_input == st.session_state.target_sentence:
    st.session_state.typing_complete = True
    end_time = time.time()
    time_taken = end_time - st.session_state.start_time

    # Calculate words per minute (WPM)
    words = len(st.session_state.target_sentence.split())
    wpm = (words / time_taken) * 60

    # Calculate accuracy
    correct_chars = sum(1 for i, c in enumerate(user_input) if c == st.session_state.target_sentence[i])
    accuracy = (correct_chars / len(st.session_state.target_sentence)) * 100

    # Display results
    st.write("### Results:")
    st.write(f"⏱️ Time Taken: {time_taken:.2f} seconds")
    st.write(f"💨 Words per Minute (WPM): {wpm:.2f}")
    st.write(f"🎯 Accuracy: {accuracy:.2f}%")

    # Reset for a new practice session
    if st.button("Try Another Sentence"):
        st.session_state.target_sentence = random.choice(sentences)
        st.session_state.start_time = None
        st.session_state.typing_complete = False
        st.experimental_rerun()
else:
    if st.session_state.typing_complete:
        st.write("Great job! Check your results above or try another sentence.")