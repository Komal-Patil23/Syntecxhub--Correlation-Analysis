# Correlation Heatmap & Pairwise Relationship Analysis

## Overview
This project performs exploratory data analysis to study relationships between numerical business variables using correlation analysis and pairwise visualizations.

---

## Objectives
- Compute Pearson correlation coefficients  
- Visualize correlations using a masked and annotated heatmap  
- Analyze pairwise relationships using a scatter matrix  

---

## Dataset
A synthetic business dataset is generated programmatically to ensure reproducibility.  
Features include:
Sales, Profit, Discount, Quantity, Shipping_Cost, Customer_Age, Order_Value.

---

## Tools Used
- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib

---

## Project Structure
Correlation_Analysis/
│
├── correlation_analysis.py
├── data/
│ └── sales_data.csv
├── outputs/
│ ├── correlation_heatmap.png
│ └── pairplot.png
└── README.md

---
## How to Run
1. Open Command Prompt in the project folder  
2. Run:
   ```bash
   python correlation_analysis.py
3. Output images will be saved in the outputs/ folder.
