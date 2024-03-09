import streamlit as st
import pandas as pd
import os
from pandasai.llm import GooglePalm  
from pandasai import SmartDataframe
from dotenv import load_dotenv

load_dotenv()
google_palm_api_key = os.getenv("GOOGLE_PALM_API_KEY")
llm = GooglePalm(api_key=google_palm_api_key)

# Function to interact with the chatbot and get response
def get_chatbot_response(data, question):
    return data.chat(question)

# Function to display data and chatbot response
def display_data_and_response(data, question):
    st.subheader("Preview of the Data:")
    st.dataframe(data.head(5))
    st.subheader("Chatbot Response:")
    
    # print("Question:", question)
    chatbot_reply = get_chatbot_response(data, question)
    # print("Chatbot Reply:", chatbot_reply)

    # Display chatbot reply in Streamlit
    st.write("You asked:", question)
    st.write("Chatbot Reply:", chatbot_reply)

# Main function
def query():
    st.title("DataWiz - Chatbot and Table")

    # Load the data
    file_path = "startup_funding_all_years.csv"
    df = pd.read_csv(file_path)
    df_startup = SmartDataframe(df, config={"llm": llm})

    # having trouble with submit button and changing user input after initial input
    with st.form(key='my_form'):
        user_input = st.text_input("You:", "Name of companies who have HeadQuarter at Mumbai and are formed on Year 2018")
        st.form_submit_button("Ask Chatbot")

        # Display the first few rows of the data and chatbot response
        if user_input:
            display_data_and_response(df_startup, user_input)


if __name__ == "__main__":
    query()
