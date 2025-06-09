
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("model_answers_comparison.xlsx")
model_columns = ["baichuan", "deepseek", "xinghuo", "zhipu"]
accuracy_overall = {
    model: (df[model] == df["correct_answer"]).mean() * 100
    for model in model_columns
}

plt.figure(figsize=(8, 5))
sns.barplot(x=list(accuracy_overall.keys()), y=list(accuracy_overall.values()), palette="Set2")
plt.title("各大模型整体预测准确率")
plt.ylabel("准确率 (%)")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
