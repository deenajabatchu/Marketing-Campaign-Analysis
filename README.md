# 📊 Customer Campaign Performance Analysis

Analyze customer marketing campaign data to uncover customer behavior patterns, evaluate campaign effectiveness, and generate actionable business insights using Python.

---

## 🚀 Project Overview

This project focuses on understanding how customers interact with marketing campaigns and identifying factors that influence campaign success.

Using data analytics techniques, the project answers business questions such as:

- Which customers are more likely to accept campaigns?
- Does income influence spending behavior?
- Which age groups have higher response rates?
- How do demographics affect purchasing patterns?
- What strategies can improve future campaigns?

---

## 🎯 Business Objective

Marketing campaigns require significant investment, but not every campaign delivers the expected return.

The objective of this project is to analyze customer demographics, spending habits, and campaign responses to help businesses:

- Improve customer targeting
- Increase campaign conversion rates
- Optimize marketing budgets
- Support data-driven decision making

---

## 📂 Dataset

**Dataset:** Superstore Marketing Campaign Dataset

- Source: Kaggle
- Records: 2,240 customers
- Features: 22 columns

### Dataset Features

| Feature | Description |
|----------|-------------|
| Year_Birth | Customer birth year |
| Education | Education qualification |
| Marital_Status | Marital status |
| Income | Annual income |
| Recency | Days since last purchase |
| MntWines | Wine spending |
| MntFruits | Fruit spending |
| MntMeatProducts | Meat spending |
| MntFishProducts | Fish spending |
| MntSweetProducts | Sweet spending |
| MntGoldProds | Gold product spending |
| NumWebPurchases | Website purchases |
| NumCatalogPurchases | Catalog purchases |
| NumStorePurchases | Store purchases |
| NumWebVisitsMonth | Monthly website visits |
| Response | Campaign acceptance |

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib

---

## 📁 Project Structure

```text
Marketing-Campaign-Analysis/
│
├── campaign_analysis.py
├── marketing_campaign.csv
├── requirements.txt
├── README.md
├── age_group_response.png
├── income_distribution.png
├── education_spending.png
└── marital_response.png
```

---

## ⚙️ Workflow

### 1. Data Collection

- Imported dataset using Pandas
- Explored dataset structure
- Identified important features

### 2. Data Cleaning

- Removed duplicate records
- Handled missing values
- Verified data consistency

### 3. Feature Engineering

Created new variables:

- Customer Age
- Total Spending

```python
df['Age'] = 2026 - df['Year_Birth']

df['Total_Spending'] = (
    df['MntWines']
    + df['MntFruits']
    + df['MntMeatProducts']
    + df['MntFishProducts']
    + df['MntSweetProducts']
    + df['MntGoldProds']
)
```

### 4. Statistical Analysis

Performed analysis using NumPy:

- Mean Income
- Median Income
- Standard Deviation
- Campaign Acceptance Rate

### 5. Exploratory Data Analysis

Analyzed:

- Income patterns
- Spending behavior
- Customer segments
- Campaign effectiveness

### 6. Visualization

Created business reports using Matplotlib.

---

## 📈 Visualizations

### Campaign Acceptance by Age Group

Identifies which age segments respond positively to campaigns.

### Income Distribution

Analyzes customer income spread.

### Average Spending by Education

Compares spending across educational backgrounds.

### Campaign Success by Marital Status

Examines response differences among marital groups.

---

## 🔍 Key Insights

- Customers with higher income generally spend more.
- Certain age groups exhibit stronger campaign engagement.
- Campaign acceptance differs across demographic segments.
- Customer demographics significantly influence purchasing behavior.
- Businesses can improve conversions using targeted campaigns.

---

## 💼 Business Impact

This analysis can help organizations:

✅ Improve customer segmentation

✅ Increase marketing ROI

✅ Optimize campaign strategies

✅ Identify high-value customers

✅ Support strategic decision-making

---

## ▶️ How to Run the Project

### Clone Repository

```bash
git clone https://github.com/yourusername/Marketing-Campaign-Analysis.git
```

### Navigate to Project Directory

```bash
cd Marketing-Campaign-Analysis
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python campaign_analysis.py
```

---

## 📊 Sample Outputs

The script automatically generates the following visualizations:

- age_group_response.png
- income_distribution.png
- education_spending.png
- marital_response.png

---

## 🔮 Future Enhancements

- Build an interactive Power BI dashboard
- Integrate SQL for reporting workflows
- Develop customer segmentation models
- Deploy using Streamlit
- Predict campaign responses using Machine Learning

---

## 📌 Resume Project Description

> Analyzed customer marketing campaign data using Pandas, NumPy, and Matplotlib to evaluate campaign effectiveness and customer behavior. Performed data cleaning, feature engineering, statistical analysis, and visualization to identify high-value customer segments and generate actionable business insights.

---

## 👩‍💻 Author

**Deenaja Batchu**

B.Tech – Computer Science and Engineering

Aspiring Data Analyst | Python Enthusiast | Future AI Engineer

---

⭐ If you found this project useful, consider giving it a star!