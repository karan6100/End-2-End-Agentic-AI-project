import os
import streamlit as st
from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input["selected_groq_model"]

            # Raise error if no API key is entered
            if groq_api_key == "" and os.environ['GROQ_API_KEY'] == "":
                st.error("Please Enter the Groq API key")


            # Initializing ChatGroq LLM
            llm = ChatGroq(api_key = groq_api_key, model = selected_groq_model)

        except Exception as e:
            print(e)
            raise ValueError(f"Error Occured within Exception: {e}")
        
        return llm