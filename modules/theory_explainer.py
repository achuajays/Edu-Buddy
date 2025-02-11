import streamlit as st
from utils.api_client import get_theory_explanation

def run():
    st.title("Theory Explainer")
    st.write("Enter a theory topic and configure the depth and level of explanation.")

    # Main inputs
    theory_topic = st.text_input("Theory Topic", placeholder="Enter a theory topic (e.g., Quantum Mechanics)")
    how_deep = st.slider("How Deep", min_value=1, max_value=10, value=5,
                         help="Select the depth of the explanation")
    explanation_level = st.slider("Explanation Level", min_value=1, max_value=5, value=3,
                                  help="Select the level of detail for the explanation")



    # Button to trigger the explanation generation.
    if st.button("Explain Theory"):
        if not theory_topic:
            st.error("Please provide a theory topic.")
        else:
            with st.spinner("Generating theory explanation..."):
                try:
                    explanation = get_theory_explanation(theory_topic, how_deep, explanation_level)
                    st.success("Theory Explanation Generated:")
                    st.write(explanation)
                except Exception as e:
                    st.error(f"An error occurred while generating the theory explanation: {e}")