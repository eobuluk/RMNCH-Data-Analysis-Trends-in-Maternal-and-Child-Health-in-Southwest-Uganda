import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt



import numpy as np

# Load the Excel file
file_path = '/Users/mac/Desktop/RMNCH_Data.xlsx'
df = pd.read_excel(file_path)

# View the first few rows of the dataset
print(df.head())

# Check data types and missing values
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Fill missing values with zero
df_filled_zero = df.fillna(0)

# Check for duplicate rows
print(df.duplicated().sum())

# Remove duplicates
df_cleaned = df.drop_duplicates()

# Strip whitespace and standardize column names
df.columns = df.columns.str.strip().str.lower()

# Print the updated column names
print(df.columns)

# Exploring the data
# Get summary statistics for numerical columns
print(df.describe())

# Visualizing data
# Set plot style
sns.set(style="whitegrid")

# Plot the distribution of 'Total ANC visits (New clients + Re-attendances)'
plt.figure(figsize=(10, 6))
sns.histplot(df['105-2.1 a3:total anc visits (new clients + re-attendances)'], kde=True, color='blue')
plt.title('Distribution of Total ANC Visits')
plt.xlabel('Total ANC Visits')
plt.ylabel('Frequency')
plt.show()

# Plot the trend of 'ANC 1st Visit for women' over the years
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='105-2.1 a1:anc 1st visit for women', hue='region', marker='o')
plt.title('Trend of ANC 1st Visit for Women Over Time by Region')
plt.xlabel('Year')
plt.ylabel('ANC 1st Visit for Women')
plt.show()


# RMNCH Dashboard
# Set the title of the Streamlit app
st.title("RMNCHDashboard")

# Data Overview Section
st.header("Data Overview")
st.write("Here are the first few rows of the dataset:")
st.write(df.head())

# KPI Section - Display summary stats for key indicators
st.header("Key Performance Indicators (KPIs)")
kpis = {
    'Total ANC Visits': df['105-2.1 a3:total anc visits (new clients + re-attendances)'].sum(),
    'Pregnant Women Receiving Iron/Folic Acid': df['105-2.1 a8:pregnant women receiving iron/folic acid on anc 1st visit'].sum(),
    'Syphilis Positive Cases': df['105-2.1 a11:pregnant women tested positive for syphilis'].sum(),
    'Postnatal Attendance at 6 Weeks': df['105-2.3 postnatal attendances 6 weeks'].sum(),
}

for kpi, value in kpis.items():
    st.metric(kpi, f"{value:,}")

# ANC Visits Distribution
st.header("Total ANC Visits Distribution")
plt.figure(figsize=(10, 6))
sns.histplot(df['105-2.1 a3:total anc visits (new clients + re-attendances)'], kde=True, color='blue')
plt.title('Distribution of Total ANC Visits')
plt.xlabel('Total ANC Visits')
plt.ylabel('Frequency')
st.pyplot(plt)

# Trend of ANC 1st Visit for Women
st.header("Trend of ANC 1st Visit for Women")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='105-2.1 a1:anc 1st visit for women', hue='region', marker='o')
plt.title('Trend of ANC 1st Visit for Women Over Time by Region')
plt.xlabel('Year')
plt.ylabel('ANC 1st Visit for Women')
st.pyplot(plt)

# Pregnant Women Receiving Iron/Folic Acid
st.header("Pregnant Women Receiving Iron/Folic Acid on ANC 1st Visit")
plt.figure(figsize=(10, 6))
sns.barplot(x=df['year'], y=df['105-2.1 a8:pregnant women receiving iron/folic acid on anc 1st visit'], estimator='sum')
plt.title('Total Pregnant Women Receiving Iron/Folic Acid on ANC 1st Visit by Year')
plt.xlabel('Year')
plt.ylabel('Total Number of Women')
st.pyplot(plt)

# Pregnant Women Receiving Free LLINs
st.header("Pregnant Women Receiving Free LLINs")
plt.figure(figsize=(10, 6))
sns.barplot(x=df['year'], y=df['105-2.1 a9:pregnant women receiving free llins'], estimator='sum')
plt.title('Total Pregnant Women Receiving Free LLINs by Year')
plt.xlabel('Year')
plt.ylabel('Total Number of Women')
st.pyplot(plt)

# Syphilis Testing and Positive Cases
st.header("Syphilis Testing and Positive Cases")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sns.lineplot(data=df, x='year', y='105-2.1 a10:pregnant women tested for syphilis', ax=ax1)
ax1.set_title('Pregnant Women Tested for Syphilis Over Time')
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Tested')

sns.lineplot(data=df, x='year', y='105-2.1 a11:pregnant women tested positive for syphilis', ax=ax2)
ax2.set_title('Pregnant Women Testing Positive for Syphilis Over Time')
ax2.set_xlabel('Year')
ax2.set_ylabel('Total Positive')

st.pyplot(fig)

# Postnatal Care Attendance (6 Weeks and 6 Months)
st.header("Postnatal Care Attendance")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sns.barplot(x=df['year'], y=df['105-2.3 postnatal attendances 6 weeks'], estimator='sum', ax=ax1)
ax1.set_title('Postnatal Attendance at 6 Weeks')
ax1.set_xlabel('Year')
ax1.set_ylabel('Total Number of Women')

sns.barplot(x=df['year'], y=df['105-2.3 postnatal attendances 6 months'], estimator='sum', ax=ax2)
ax2.set_title('Postnatal Attendance at 6 Months')
ax2.set_xlabel('Year')
ax2.set_ylabel('Total Number of Women')

st.pyplot(fig)

# Maternal Deaths Audited
st.header("Maternal Deaths Audited")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='105-3 oa5 maternal deaths audited', marker='o')
plt.title('Maternal Deaths Audited Over Time')
plt.xlabel('Year')
plt.ylabel('Maternal Deaths')
st.pyplot(plt)

# Perinatal Deaths Audited
st.header("Perinatal Deaths Audited")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='year', y='105-3 oa6-perinatal deaths audited', marker='o')
plt.title('Perinatal Deaths Audited Over Time')
plt.xlabel('Year')
plt.ylabel('Perinatal Deaths')
st.pyplot(plt)

# Projected Population & Births
st.header("Projected Population and Expected Births")
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

sns.lineplot(data=df, x='year', y='expected pregnancies (0.05*popn/4)', ax=ax1)
ax1.set_title('Projected Pregnancies')
ax1.set_xlabel('Year')
ax1.set_ylabel('Projected Pregnancies')

sns.lineplot(data=df, x='year', y='expected deliveries (0.0485*popn/4)', ax=ax2)
ax2.set_title('Expected Deliveries')
ax2.set_xlabel('Year')
ax2.set_ylabel('Expected Deliveries')

st.pyplot(fig)

