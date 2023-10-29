import pandas as pd
import plotly.express as px
import streamlit as st

def main():
    st.title("Funding and Revenue Trends Over the Years")

    # Load the data
    file_path_ev = r"C:\Users\VARUN\Desktop\DataHack\Gojo\DataHack_1_Go-Jo\df_ev_saved.csv"
    file_path_ai = r"C:\Users\VARUN\Desktop\DataHack\Gojo\DataHack_1_Go-Jo\df_ai_saved.csv"

    df_ev = pd.read_csv(file_path_ev)
    df_ai = pd.read_csv(file_path_ai)

    # Convert 'Year founded' to datetime and extract the year
    df_ev['Year founded'] = pd.to_datetime(df_ev['Year founded'], format='%Y').dt.year
    df_ai['Year founded'] = pd.to_datetime(df_ai['Year founded'], format='%Y').dt.year

    # Group by year and calculate average funding and average revenue for EV sector
    grouped_data_ev = df_ev.groupby('Year founded').agg({
        'Most Recent Funding Amount': 'mean',
        'Revenue': 'mean'
    }).reset_index()

    # Group by year and calculate average funding and average number of funding rounds for AI sector
    grouped_data_ai = df_ai.groupby('Year founded').agg({
        'Most Recent Funding Amount': 'mean',
        'Number of Funding Rounds': 'mean'
    }).reset_index()

    # Add a sector selection dropdown
    selected_sector = st.selectbox("Select a Sector", ["EV", "AI"])

    # Add a year slider
    selected_years = st.slider(
        "Select a Year Range",
        min_value=int(df_ev['Year founded'].min()),
        max_value=int(df_ev['Year founded'].max()),
        value=(int(df_ev['Year founded'].min()), int(df_ev['Year founded'].max()))
    )

    # Filter data based on selected years
    grouped_data_ev_filtered = grouped_data_ev[
        (grouped_data_ev['Year founded'] >= selected_years[0]) & (grouped_data_ev['Year founded'] <= selected_years[1])
    ]

    grouped_data_ai_filtered = grouped_data_ai[
        (grouped_data_ai['Year founded'] >= selected_years[0]) & (grouped_data_ai['Year founded'] <= selected_years[1])
    ]

    # Create an interactive line chart based on the selected sector and years
    if selected_sector == "EV":
        fig = px.line(
            grouped_data_ev_filtered,
            x='Year founded',
            y=['Most Recent Funding Amount', 'Revenue'],
            labels={'value': 'Amount in USD'},
            title=f'EV Sector Funding and Revenue Trends ({selected_years[0]}-{selected_years[1]})'
        )
    elif selected_sector == "AI":
        fig = px.line(
            grouped_data_ai_filtered,
            x='Year founded',
            y=['Most Recent Funding Amount', 'Number of Funding Rounds'],
            labels={'value': 'Amount in USD'},
            title=f'AI Sector Funding and Revenue Trends ({selected_years[0]}-{selected_years[1]})'
        )

    # Customize the layout
    fig.update_xaxes(type='category')

    # Display the selected sector plot
    st.plotly_chart(fig)

    # Add some interactive elements
    st.write(f"You selected: {selected_sector} sector and the year range: {selected_years[0]} to {selected_years[1]}.")
    st.markdown(
        f"Explore the funding and revenue trends of {selected_sector} startups over the selected year range. "
        "Use the dropdown to switch between different sectors and observe the patterns."
    )

if __name__ == "__main__":
    main()
