import streamlit as st
from dashboard1 import main as dashboard1
from dashboard2 import main as dashboard2
from dashboard3 import main as dashboard3
from dashboard4 import main as dashboard4
from dashboard5 import main as dashboard5
from dashboard6 import main as dashboard6
# from question1 import main as question1
from query import query


# remaining - conclusion page that answers different questions.
dashboard_options = {
    "Startup Funding Insights": "Number of startups that appear for different types of funding rounds",
    "Top Funding Amounts": "List of companies ranked according to amount of funding recieved",
    "Top Investors and Sectors by Total Funding Amount": "Sectors and investors classified by total funding amount",
    "Funding Trend Over the Years": "Description for Funding Trend Over the Years",
    "Number of New Startups Formed Each Year": "Description for Number of New Startups Formed Each Year",
    "Total Funding in each region": "Description for Total Funding in each region",
}

question_options = {
    "What are the top 10 startups in terms of revenue over the last 5 years",
    "Give a location-wise distribution of the top 100 startups",
    "How did Covid affect funding for startups across different sectors"
}


def main():
    st.set_page_config(
        page_title="DataWiz",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("DataWiz - Dashboard Hub")

    st.sidebar.title("Sections")

    # Create an expander for Sections
    with st.sidebar.expander("Select Section"):
        section_options = {
            "Dashboards": ["Startup Funding Insights", "Top Funding Amounts",
                           "Top Investors and Sectors by Total Funding Amount",
                           "Funding Trend Over the Years",
                           "Number of New Startups Formed Each Year",
                           "Total Funding in each region"],
            "Conclusions": ["Question 1", "Question 2", "Question 3"],
        }

        selected_section = st.radio("Go to", list(section_options.keys()))

        if selected_section == "Dashboards":
            selected_dashboard = st.selectbox("Select Dashboard", section_options[selected_section])
            st.write(f"**Dashboard Description:** {dashboard_options[selected_dashboard]}")
        elif selected_section == "Conclusions":
            selected_question = st.selectbox("Select Question", section_options[selected_section])
            st.write(f"**Question Description:** {question_options[selected_question]}")

    # Flag to determine if chatbot section should be displayed
    show_chatbot_section = st.sidebar.button("Chatbot and Table")

    # Display selected dashboard, question, or chatbot section
    if not show_chatbot_section:
        if selected_section == "Dashboards":
            if selected_dashboard == "Startup Funding Insights":
                dashboard1()
            elif selected_dashboard == "Top Funding Amounts":
                dashboard2()
            elif selected_dashboard == "Top Investors and Sectors by Total Funding Amount":
                dashboard3()
            elif selected_dashboard == "Funding Trend Over the Years":
                dashboard4()
            elif selected_dashboard == "Number of New Startups Formed Each Year":
                dashboard5()
            elif selected_dashboard == "Total Funding in each region":
                dashboard6()
        elif selected_section == "Conclusions":
            if selected_question == "Question 1":
                pass
                # question1()
            # elif selected_question == "Question 2":
            #     question2()
            # elif selected_question == "Question 3":
            #     question3()
    else:
        query()

if __name__ == "__main__":
    main()
