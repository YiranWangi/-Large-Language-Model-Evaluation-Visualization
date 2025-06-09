
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("model_answers_comparison.xlsx")
model_columns = ["baichuan", "deepseek", "xinghuo", "zhipu"]

results = []
for source, group in df.groupby("source_file"):
    for model in model_columns:
        correct = (group[model] == group["correct_answer"]).sum()
        incorrect = len(group) - correct
        results.append({
            "source": source,
            "model": model,
            "Correct": correct,
            "Incorrect": incorrect
        })

bar_df = pd.DataFrame(results)

stacked = bar_df.melt(id_vars=["source", "model"], value_vars=["Correct", "Incorrect"],
                      var_name="Result", value_name="Count")

plt.figure(figsize=(12, 6))
sns.barplot(data=stacked, x="source", y="Count", hue="Result", palette="coolwarm", ci=None)
plt.title("各数据来源下模型预测结果（正确 vs 错误）")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
