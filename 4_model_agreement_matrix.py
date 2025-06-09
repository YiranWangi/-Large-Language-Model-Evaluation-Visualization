# -*- coding: utf-8 -*-
"""
Created on Thu May  1 21:04:02 2025

@author: rickr
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("model_answers_comparison.xlsx")
model_columns = ["baichuan", "deepseek", "xinghuo", "zhipu"]

agreement = pd.DataFrame(index=model_columns, columns=model_columns)
for i in model_columns:
    for j in model_columns:
        if i == j:
            agreement.loc[i, j] = 100.0
        else:
            agreement.loc[i, j] = (df[i] == df[j]).mean() * 100

agreement = agreement.astype(float)

plt.figure(figsize=(8, 6))
sns.heatmap(agreement, annot=True, fmt=".1f", cmap="Oranges", cbar_kws={"label": "一致率 (%)"})
plt.title("模型预测一致率矩阵")
plt.tight_layout()
plt.show()