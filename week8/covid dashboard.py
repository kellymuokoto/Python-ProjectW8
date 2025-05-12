# Streamlit Dashboard (Enhanced)

import streamlit as st
import pandas as pd
import plotly.express as px

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stMetric {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data
def load_data():
    df = pd.read_csv("owid-covid-data.csv", parse_dates=["date"])
    df = df[df['continent'].notna()]
    return df

df = load_data()

# Sidebar
st.sidebar.title("COVID-19 Dashboard")
country = st.sidebar.selectbox("Select Country", sorted(df["location"].unique()))
min_date, max_date = df["date"].min(), df["date"].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Filter data
df_country = df[(df["location"] == country) &
                (df["date"] >= pd.to_datetime(date_range[0])) &
                (df["date"] <= pd.to_datetime(date_range[1]))]

# Main Dashboard
st.title("🌍 COVID-19 Dashboard")
st.subheader(f"Tracking COVID-19 Data for {country}")
st.write(f"Date Range: {date_range[0]} to {date_range[1]}")

# Metrics in columns
latest = df_country.sort_values("date").iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("Total Cases", f"{int(latest['total_cases']):,}")
col2.metric("Total Deaths", f"{int(latest['total_deaths']):,}" if pd.notna(latest['total_deaths']) else "N/A")

# Handle NaN for fully vaccinated percentage
fully_vaccinated = latest['people_fully_vaccinated_per_hundred']
col3.metric("Fully Vaccinated (%)", f"{fully_vaccinated:.2f}%" if pd.notna(fully_vaccinated) else "0.00%")

# Function to plot line charts
def plot_line(y, title, y_label):
    fig = px.line(
        df_country,
        x="date",
        y=y,
        title=title,
        labels={"date": "Date", y: y_label},
        template="plotly_white",
    )
    st.plotly_chart(fig, use_container_width=True)

# Charts
st.markdown("### Trends Over Time")
plot_line("new_cases", "Daily New COVID-19 Cases", "New Cases")
plot_line("new_deaths", "Daily New Deaths", "New Deaths")

if "icu_patients" in df_country.columns and df_country["icu_patients"].notna().any():
    plot_line("icu_patients", "ICU Patients Over Time", "ICU Patients")

if "hosp_patients" in df_country.columns and df_country["hosp_patients"].notna().any():
    plot_line("hosp_patients", "Hospitalized Patients Over Time", "Hospital Patients")

if "people_fully_vaccinated_per_hundred" in df_country.columns:
    plot_line("people_fully_vaccinated_per_hundred", "Vaccination Coverage", "% Fully Vaccinated")

# Footer
st.markdown("---")
st.markdown("**Dashboard by Kelly Muokoto | Data Source: [Our World in Data](https://ourworldindata.org/covid-vaccinations)")
