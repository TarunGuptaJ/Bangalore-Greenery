import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("csv_files/green_all.csv")
# 76x66
result = df.pivot(index='yval', columns='xval', values='Percentage')

fig, ax = plt.subplots(figsize=(12, 7))
title = "Greenery"
plt.title(title, fontsize=18)
ttl = ax.title
ttl.set_position([0.5, 1.05])
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
sns.heatmap(result, fmt="", cmap="BuGn", linewidths=0.0, ax=ax)
plt.show()