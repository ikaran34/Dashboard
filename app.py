import streamlit as st
import pandas as pd
import seaborn as sns

# Title and introduction
st.title("Iris Data Analytics Dashboard")
st.write("Explore the classic Iris dataset with interactive visualizations.")

# Load the dataset (using Seaborn’s sample iris dataset)
df = sns.load_dataset("iris")

# Option to display raw data
if st.checkbox("Show raw data"):
    st.write(df)

# Display basic statistics
st.subheader("Data Summary")
st.write(df.describe())

# Create a scatter plot for sepal dimensions
st.subheader("Scatter Plot: Sepal Length vs. Sepal Width")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="sepal_length", y="sepal_width", hue="species", ax=ax)
st.pyplot(fig)

# Additional customization or analytics can be added here
