import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Revenue Distribution and Top 10 Companies by Revenue")

    # Load the numerical data
    file_path_ev = r"C:\Users\VARUN\Desktop\DataHack\Gojo\DataHack_1_Go-Jo\df_ev_saved.csv"
    df_ev = pd.read_csv(file_path_ev)

    # Load the categorical data
    file_path_ai = r"C:\Users\VARUN\Desktop\DataHack\Gojo\DataHack_1_Go-Jo\df_ai_saved.csv"
    df_ai = pd.read_csv(file_path_ai)

    # Select relevant columns
    selected_columns_ev = ["Name of company", "Revenue"]
    selected_columns_ai = ["Name of company", "Revenue"]

    # Filter out rows with missing revenue values
    df_ev = df_ev.dropna(subset=["Revenue"])
    df_ai = df_ai.dropna(subset=["Revenue"])

    # Calculate top 10 companies by revenue for numerical data
    top_10_revenue_ev = df_ev.sort_values(by="Revenue", ascending=False).head(10)

    # Create a bar plot for the top 10 companies by revenue
    fig_ev = px.bar(
        top_10_revenue_ev,
        x="Name of company",
        y="Revenue",
        title="Top 10 EV Startups by Revenue",
        labels={"Revenue": "Revenue (in Millions)"},
    )

    # Customize layout for the bar plot
    fig_ev.update_layout(xaxis_title="Company Name", yaxis_title="Revenue (in Millions)")

    # Calculate percentage of revenue for each category
    revenue_counts_ai = df_ai["Revenue"].value_counts()
    revenue_percentage_ai = (revenue_counts_ai / revenue_counts_ai.sum()) * 100

    # Create a pie chart for the categorical data
    fig_ai = px.pie(
        names=revenue_percentage_ai.index,
        values=revenue_percentage_ai,
        title="Revenue Distribution of AI startups (Pie Chart)",
        labels={"labels": "Revenue Categories", "values": "Percentage"},
    )

    # Display both plots
    st.plotly_chart(fig_ev)
    st.plotly_chart(fig_ai)

    # Inference
    st.markdown("## Inference:")
    st.markdown(
        "1. The bar plot highlights the top 10 EV startups with the highest revenue, providing insights into potential investment opportunities."
    )
    st.markdown(
        "2. The pie chart illustrates the distribution of revenue categories among AI startups, aiding in understanding the market segmentation."
    )
    st.markdown(
        "3. Investors may consider focusing on EV startups with a strong revenue track record and explore opportunities in high-revenue AI segments."
    )

    # Evaluation Matrix
    st.markdown("## Evaluation Matrix:")
    st.markdown(
        "Consider the following criteria when evaluating startups for investment:"
    )
    st.markdown("### 1. Revenue Growth:")
    st.markdown(
        "   - Evaluate the historical revenue growth of EV startups to identify those with a consistent upward trend."
    )
    st.markdown("### 2. Market Share:")
    st.markdown(
        "   - Assess the market share of AI startups in high-revenue categories to understand their position in the market."
    )
    st.markdown("### 3. Funding Rounds:")
    st.markdown(
        "   - Explore the number of funding rounds to gauge investor confidence and support in the startup."
    )

if __name__ == "__main__":
    main()
