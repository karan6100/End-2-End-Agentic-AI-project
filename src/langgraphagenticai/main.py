import streamlit as st
import json
from  src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.LLMs.openaillm import OpenAILLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from UI.")
    else:
        selected_llm = user_input["selected_llm"]


    # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 

    else :
        user_message = st.chat_input("Enter your message:")

    if user_message:
        try:

            # configure LLM
            if selected_llm == "Groq":
                obj_llm_config = GroqLLM(user_controls_input= user_input)
                model = obj_llm_config.get_llm_model()

            if selected_llm == 'OpenAI':
                obj_llm_config = OpenAILLM(user_controls_input= user_input)
                model = obj_llm_config.get_llm_model()


            if not model:
                st.error("Error: LLM could not be initialized.")
                return 
            
            # Initialize and set up the graph based on use case
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            # Graph Builder 
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                # Display result
                DisplayResultStreamlit(usecase=usecase, graph=graph, user_message= user_message).display_result_on_ui()
            except Exception as e:
                print(e)
                st.error(f"Error - Graph setup failed")
            return
            

        except Exception as  e:
            raise ValueError(f"Error occurred with Exception: {e}")