import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("model_answers_comparison.xlsx")
model_columns = ["baichuan", "deepseek", "xinghuo", "zhipu"]

records = []
for source, group in df.groupby("source_file"):
    for model in model_columns:
        acc = (group[model] == group["correct_answer"]).mean() * 100
        records.append({"source": source, "model": model, "accuracy": acc})

long_df = pd.DataFrame(records)

# 自定义每个模型的颜色（你也可以换成你喜欢的配色）
palette = {
    "baichuan": "#1f77b4",  # 蓝色
    "deepseek": "#2ca02c",  # 绿色
    "xinghuo": "#ff7f0e",   # 橙色
    "zhipu": "#d62728"      # 红色
}

plt.figure(figsize=(10, 6))
sns.boxplot(data=long_df, x="model", y="accuracy", palette=palette)
plt.title("不同模型在不同数据来源下的准确率分布（箱线图）")
plt.ylabel("准确率 (%)")
plt.tight_layout()
plt.show()
