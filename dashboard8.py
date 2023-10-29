import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Location Wise Top 100 Startups")

    # Load the data
    file_path = r"C:\Users\VARUN\Desktop\DataHack\Gojo\DataHack_1_Go-Jo\Combined_data_ai_ev.csv"
    df = pd.read_csv(file_path)

    # Extract location counts
    location_counts = df['Location'].value_counts().reset_index()
    location_counts.columns = ['Location', 'Counts']

    # Create a pie chart
    fig = px.pie(
        location_counts,
        names='Location',
        values='Counts',
        title='Startup Locations',
    )

    # Display the pie chart
    st.plotly_chart(fig)

    # Display value counts data
    st.subheader("Location Counts Data:")
    st.dataframe(location_counts)

    # Write inference in bullet points
    st.markdown("""
    ### Inference:
    - The analysis of location-wise distribution reveals that metropolitan cities are prominent hotspots for emerging startups.
    - The concentration of innovative ventures in these urban hubs emphasizes the dynamic and conducive environments they provide.
    - Major cities play a pivotal role in fostering the growth of groundbreaking ideas and entrepreneurial endeavors.
    - As the startup ecosystem continues to flourish, investors are advised to closely monitor the trajectory of metropolitan areas.
    - Metropolitan cities are emerging as key contributors to the ever-evolving landscape of the startup ecosystem.
    """)

if __name__ == "__main__":
    main()
