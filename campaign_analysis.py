
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep=",")

print("Dataset Shape:", df.shape)
print(df.head())

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=['Income'], inplace=True)

# Feature Engineering
df['Age'] = 2026 - df['Year_Birth']

df['Total_Spending'] = (
    df['MntWines'] +
    df['MntFruits'] +
    df['MntMeatProducts'] +
    df['MntFishProducts'] +
    df['MntSweetProducts'] +
    df['MntGoldProds']
)

# Campaign Response
accepted = df['Response'].sum()
total_customers = len(df)

acceptance_rate = accepted / total_customers * 100

print(f"Campaign Acceptance Rate: {acceptance_rate:.2f}%")

# NumPy Statistics
print("\nIncome Statistics")
print("Mean:", np.mean(df['Income']))
print("Median:", np.median(df['Income']))
print("Std Dev:", np.std(df['Income']))

# Age Groups
bins = [18, 30, 40, 50, 60, 100]
labels = ['18-30', '31-40', '41-50', '51-60', '60+']

df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Visualization 1
age_response = df.groupby('Age_Group')['Response'].mean() * 100

plt.figure(figsize=(8,5))
age_response.plot(kind='bar')
plt.title("Campaign Acceptance by Age Group")
plt.ylabel("Acceptance Rate (%)")
plt.tight_layout()
plt.savefig("age_group_response.png")
plt.close()

# Visualization 2
plt.figure(figsize=(8,5))
plt.hist(df['Income'], bins=20)
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("income_distribution.png")
plt.close()

# Visualization 3
edu_spending = df.groupby('Education')['Total_Spending'].mean()

plt.figure(figsize=(8,5))
edu_spending.plot(kind='bar')
plt.title("Average Spending by Education")
plt.ylabel("Average Spending")
plt.tight_layout()
plt.savefig("education_spending.png")
plt.close()

# Visualization 4
marital_response = df.groupby('Marital_Status')['Response'].mean() * 100

plt.figure(figsize=(8,5))
marital_response.plot(kind='bar')
plt.title("Campaign Success by Marital Status")
plt.ylabel("Acceptance Rate (%)")
plt.tight_layout()
plt.savefig("marital_response.png")
plt.close()

print("\nTop Insights")
print("- Customers with higher income tend to spend more.")
print("- Certain age groups respond better to campaigns.")
print("- Marital status influences campaign conversion.")
