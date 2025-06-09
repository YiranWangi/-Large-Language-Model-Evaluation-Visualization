# -*- coding: utf-8 -*-
"""
Created on Thu May  1 20:52:59 2025

@author: rickr
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# 设置支持中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
matplotlib.rcParams['axes.unicode_minus'] = False     # 正常显示负号

# 读取模型预测结果数据
df = pd.read_excel("model_answers_comparison.xlsx")

# 检查是否存在 source 列
if "source_file" not in df.columns:
    raise ValueError("Excel 文件中缺少 'source_file' 列，无法按来源分组")

# 所有模型的列名
model_columns = ["baichuan", "deepseek", "xinghuo", "zhipu"]

# 创建正确率矩阵（每个 source 每个模型的正确率）
accuracy_matrix = {}

for source, group in df.groupby("source_file"):
    accuracy_matrix[source] = {}
    for model in model_columns:
        correct = (group[model] == group["correct_answer"]).sum()
        total = len(group)
        accuracy = correct / total if total > 0 else 0
        accuracy_matrix[source][model] = accuracy * 100  # 百分比形式

# 转为 DataFrame
accuracy_df = pd.DataFrame(accuracy_matrix).T  # 行为 source，列为模型

# 绘制热力图
plt.figure(figsize=(10, max(6, len(accuracy_df) * 0.5)))
sns.heatmap(accuracy_df, annot=True, fmt=".1f", cmap="YlGnBu", cbar_kws={"label": "准确率 (%)"})
plt.title("模型预测准确率矩阵（按数据来源分组）")
plt.xlabel("大模型")
plt.ylabel("题目来源（source）")
plt.tight_layout()
plt.show()
