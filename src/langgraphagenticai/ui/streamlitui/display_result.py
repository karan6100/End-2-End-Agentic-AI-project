# Display data in the front-end
import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
import json

class DisplayResultStreamlit:
    """
    Displays data in the front-end
    """
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message


    def display_result_on_ui(self):
        # usecase = self.usecase
        # graph = self.graph
        # user_message = self.user_message

        if self.usecase == "Basic Chatbot":
            for event in self.graph.stream({"messages": ("user",self.user_message)}):
                print(event.values())
                for value in event.values():
                    print(value["messages"])
                    with st.chat_message("user"):
                        st.write(self.user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)

