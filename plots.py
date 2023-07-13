import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


#ResNet18
d = {'pruner_name': ["L1 Unstructured", "L1 Unstructured", "L1 Unstructured", "L1 Unstructured", "L1 Unstructured",
                     "L1 Structured", "L1 Structured", "L1 Structured", "L1 Structured", "L1 Structured",
                     "L2 Structured", "L2 Structured", "L2 Structured", "L2 Structured", "L2 Structured"], 
        'prune_sparsity': [0.5, 0.6, 0.7, 0.8, 0.9, 0.5, 0.6, 0.7, 0.8, 0.9, 0.5, 0.6, 0.7, 0.8, 0.9],
        'prediction_accuracy': [69.863, 69.813, 70.681, 70.625, 68.045, 
                                67.815, 67.952, 67.047, 64.115, 58.412,
                                67.296, 68.556, 67.556, 64.437, 58.481]}

d2 = {'pruner_name': ["L1 Unstructured", "L1 Unstructured", "L1 Unstructured", "L1 Unstructured", "L1 Unstructured",
                     "L1 Structured", "L1 Structured", "L1 Structured", "L1 Structured", "L1 Structured",
                     "L2 Structured", "L2 Structured", "L2 Structured", "L2 Structured", "L2 Structured"], 
        'prune_sparsity': [0.5, 0.6, 0.7, 0.8, 0.9, 0.5, 0.6, 0.7, 0.8, 0.9, 0.5, 0.6, 0.7, 0.8, 0.9],
        'prediction_accuracy': [75.905, 75.630, 75.437, 74.215, 70.513,
                                73.085, 70.778, 71.657, 66.538, 62.283,
                                73.997, 74.147, 72.905, 67.860, 62.818]}

df = pd.DataFrame(data=d2)
#print(df)
sns.set_theme(style="darkgrid")
ax = sns.lineplot(
    data=df,
    x="prune_sparsity", y="prediction_accuracy", hue="pruner_name", style="pruner_name",
    markers=["o"], dashes=False
)
ax.axhline(73.600)
ax.set(xlabel='Model Sparsity', ylabel='Prediction Accuracy (%)', ylim=(10, 80))
plt.legend(title='Pruner Name')

plt.show()


def main(plot: str) -> None:
    if plot == "ResNet18":
        


if __name__ == '__main__':
    plot = "ResNet18"
    main(plot)