import streamlit as st
import pandas as pd
import plotly.express as px

# Load data from Our World in Data
DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_URL)
    df['date'] = pd.to_datetime(df['date'])
    return df

df = load_data()

# Sidebar for user selections
st.sidebar.title("Untitled Dashboard")
countries = st.sidebar.multiselect("Select Countries", df['location'].unique(), default=["United States", "India", "Brazil"])
df_filtered = df[df['location'].isin(countries)]

# Main Dashboard Title
st.title("📊 Untitled Data Analytics Dashboard")

# Display Key Metrics from the latest data for the selected countries
latest_data = df_filtered[df_filtered['date'] == df_filtered['date'].max()]
total_cases = latest_data['total_cases'].sum()
total_deaths = latest_data['total_deaths'].sum()
total_vaccinations = latest_data['total_vaccinations'].sum()

st.metric("🦠 Total Cases", f"{total_cases:,.0f}")
st.metric("☠️ Total Deaths", f"{total_deaths:,.0f}")
st.metric("💉 Total Vaccinations", f"{total_vaccinations:,.0f}")

# Line Chart: Daily New Cases Trend
st.subheader("📈 Daily Trend")
fig_cases = px.line(df_filtered, x='date', y='new_cases', color='location', title="Daily New Cases")
st.plotly_chart(fig_cases)

# Bar Chart: Total Cases by Country
st.subheader("🌎 Total by Country")
fig_bar = px.bar(latest_data, x='location', y='total_cases', title="Total Cases Comparison")
st.plotly_chart(fig_bar)

# Map: Global Spread Visualization
st.subheader("🗺️ Global Spread")
world_latest = df[df['date'] == df['date'].max()]
fig_map = px.scatter_geo(
    world_latest,
    locations="iso_code",
    size="total_cases",
    hover_name="location",
    projection="natural earth",
    title="Cases Worldwide"
)
st.plotly_chart(fig_map)

st.write("📢 **Deployment Instructions:** Push this code to GitHub (repository name: 'Untitled') and deploy on Streamlit Community Cloud.")
