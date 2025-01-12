import streamlit as st
from dashboard1 import main as dashboard1
from dashboard2 import main as dashboard2
from dashboard3 import main as dashboard3
from dashboard4 import main as dashboard4
from dashboard5 import main as dashboard5
from dashboard6 import main as dashboard6
from dashboard7 import main as dashboard7
from dashboard8 import main as dashboard8
from dashboard9 import main as dashboard9
from dashboard10 import main as dashboard10
from query import query

def main():
    st.set_page_config(
        page_title="DataWiz",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.title("DataWiz")

    st.sidebar.title("Dashboards Hub")

    # Create an expander for Dashboards
    with st.sidebar.expander("Select Dashboard"):
        dashboard_options = {
            "Startup Funding Insights": "Explore insights into startup funding.",
            "Top Funding Amounts": "Discover the top funding amounts for startups.",
            "Top Investors and Sectors by Total Funding Amount": "See top investors and sectors by total funding.",
            "Funding Trend Over the Years": "Visualize the funding trend over the years.",
            "Number of New Startups Formed Each Year": "Explore the number of new startups each year.",
            "Total Funding in each region": "View total funding in each region.",
            "Top 10 AI/EV Startups by Revenue": "Uncover the financial giants in Artificial Intelligence (AI) and Electric Vehicle (EV) sectors with a glance at the revenue leaders.",
            "Location Wise Top 100 Startups": "Navigate through the startup landscape with insights into the top 100 companies, categorized by their geographical presence.",
            "Covid-19 effect on fundings": "Explore the transformative impact of the Covid-19 pandemic on startup fundings with detailed insights and trends",
            "Trend Analysis of Revenue and Fund across years of EV and AI startups" : ""
            # Add more dashboards as needed
        }

        selected_dashboard = st.radio("Go to", list(dashboard_options.keys()))

        # Display description of the selected dashboard
        st.write(f"**Dashboard Description:** {dashboard_options[selected_dashboard]}")

    # Flag to determine if chatbot section should be displayed
    show_chatbot_section = st.sidebar.button("Chatbot and Table")

    # Display selected dashboard or chatbot section
    if not show_chatbot_section:
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
        elif selected_dashboard == "Top 10 AI/EV Startups by Revenue":
            dashboard7()
        elif selected_dashboard == "Location Wise Top 100 Startups":
            dashboard8()
        elif selected_dashboard == "Covid-19 effect on fundings":
            dashboard9()
        elif selected_dashboard == "Trend Analysis of Revenue and Fund across years of EV and AI startups":
            dashboard10()
        # Add more conditions for additional dashboards as needed
    # else:
    query()

if __name__ == "__main__":
    main()
