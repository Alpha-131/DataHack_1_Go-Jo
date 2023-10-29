import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Covid-19 Effect on Fundings")

    # Load the data
    file_path = r'C:\Users\VARUN\Desktop\DataHack\Gojo\DataHack_1_Go-Jo\df_startup_2018_2021.csv'
    df = pd.read_csv(file_path)

    # Filter out rows with missing values
    df = df.dropna(subset=['Amount($)', 'Year', 'Sector'])

    # Split sectors into individual items
    sectors = set()
    for sector_list in df['Sector'].str.split(', '):
        sectors.update(sector_list)

    # Filter sectors without funding in at least two years
    sectors_with_funding = df.groupby('Sector')['Year'].nunique()
    valid_sectors = sectors_with_funding[sectors_with_funding >= 2].index
    valid_sectors_list = sorted(list(valid_sectors))

    # Multiselect for sector selection
    selected_sectors = st.multiselect("Select Sectors", valid_sectors_list)

    # Filter data based on selected sectors
    filtered_data = df[df['Sector'].apply(lambda x: any(sector in x for sector in selected_sectors))]

    # Plot amount vs year for selected sectors using Plotly Express
    fig = px.line(
        filtered_data,
        x='Year',
        y='Amount($)',
        color='Sector',
        title='Funding Trend for Selected Sectors Over the Years',
        labels={'Amount($)': 'Funding Amount ($)', 'Year': 'Year'},
    )

    # Display the plot
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
