import os
import streamlit as st
from langchain_openai import ChatOpenAI


class OpenAILLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self):
        try:
            openai_llm_key = self.user_controls_input["OPENAI_API_KEY"]
            selected_openai_model = self.user_controls_input["selected_openai_model"]

            # Raise error if no API key is entered
            if openai_llm_key == "" and os.environ['OPENAI_API_KEY'] == "":
                st.error("Please Enter the OpenAI API key")


            # Initializing ChatGroq LLM
            llm = ChatOpenAI(api_key = openai_llm_key, model = selected_openai_model)

        except Exception as e:
            print(e)
            raise ValueError(f"Error Occured within Exception: {e}")
        
        return llm