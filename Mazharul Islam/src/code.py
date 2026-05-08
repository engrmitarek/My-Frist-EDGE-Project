import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/data.csv')

#Bar Chart
plt.figure(figsize=(8,4))
plt.bar(df['name'], df['math'],color='purple',alpha=0.8)
plt.xlabel("Student Name")
plt.ylabel("Math Score")
plt.title("Math Score of Each Student")
plt.tight_layout()
plt.savefig('output/bar_chart.png')
plt.show()