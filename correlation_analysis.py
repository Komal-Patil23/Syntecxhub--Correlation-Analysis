import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from pandas.plotting import scatter_matrix

# -----------------------------
# Create folders
# -----------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Seed
# -----------------------------
np.random.seed(42)

# -----------------------------
# Create dataset
# -----------------------------
data = {
    "Sales": np.random.randint(1000, 10000, 200),
    "Profit": np.random.randint(100, 3000, 200),
    "Discount": np.random.uniform(0, 0.5, 200),
    "Quantity": np.random.randint(1, 20, 200),
    "Shipping_Cost": np.random.randint(50, 500, 200),
    "Customer_Age": np.random.randint(18, 65, 200),
    "Order_Value": np.random.randint(500, 12000, 200)
}

df = pd.DataFrame(data)
df.to_csv("data/sales_data.csv", index=False)

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/sales_data.csv")

# -----------------------------
# Correlation Heatmap
# -----------------------------
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))

plt.figure(figsize=(10, 8))
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap of Business Metrics")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png")
plt.close()

# -----------------------------
# Scatter Matrix (FULL IMAGE FIX)
# -----------------------------
fig = plt.figure(figsize=(14, 14))

axes = scatter_matrix(
    df[["Sales", "Profit", "Discount", "Quantity"]],
    diagonal="hist",
    alpha=0.7,
    figsize=(14, 14)
)

plt.suptitle(
    "Scatter Matrix of Key Business Variables",
    fontsize=16,
    y=1.02
)

plt.savefig(
    "outputs/pairplot.png",
    bbox_inches="tight",
    pad_inches=0.5
)

plt.close()
