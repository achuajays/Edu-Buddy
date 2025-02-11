# main.py
import streamlit as st
from modules import data_structure_understander , theory_explainer

def main():
    st.sidebar.title("Edu Buddy")
    # Add more topics to this list as you build additional pages.
    topic = st.sidebar.selectbox("Select Topic", ["Data Structure Understander", "Theory Explainer"])

    match topic:
        case "Data Structure Understander":
            data_structure_understander.run()
        case "Theory Explainer":
            theory_explainer.run()
        case _:
            print("No matching topic found.")


if __name__ == "__main__":
    main()
