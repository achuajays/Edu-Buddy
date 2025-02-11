import streamlit as st
from utils.api_client import get_algorithm_explanation


def run():
    st.title("Algorithm Understanding Tool")
    st.write("Use this tool to understand how different algorithms work.")

    # Input fields for the algorithm details.
    algo_type = st.text_input("Algorithm Type", placeholder="e.g., Sorting, Graph Traversal")

    # Dropdown for top 10 programming languages + "Other" option
    top_languages = [
        "Python", "c", "Java", "C++", "C#",
        "Go", "Rust", "Swift", "Kotlin", "JavaScript", "Other"
    ]

    algo_programming_language = st.selectbox("Algorithm Programming Language", top_languages)

    # Show text input if "Other" is selected
    custom_language = ""
    if algo_programming_language == "Other":
        custom_language = st.text_input("Enter Other Programming Language", placeholder="Type your language here...")

    algo_input = st.text_area("Algorithm Input", placeholder="Enter algorithm details or description here...")

    # Button to trigger explanation generation.
    if st.button("Explain Algorithm"):
        if not algo_type or not algo_input:
            st.error("Please provide both the algorithm type and its details.")
        else:
            # Use custom language if "Other" was selected
            selected_language = custom_language if algo_programming_language == "Other" else algo_programming_language

            with st.spinner("Generating explanation..."):
                try:
                    explanation = get_algorithm_explanation(algo_type, algo_input, selected_language)
                    st.success("Explanation Generated:")
                    st.write(explanation)
                except Exception as e:
                    st.error(f"An error occurred while communicating with the Groq API: {e}")

