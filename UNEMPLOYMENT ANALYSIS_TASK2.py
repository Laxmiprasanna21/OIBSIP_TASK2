import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
dataset=pd.read_csv('/content/Unemployment in India.csv')
dataset.head(100)
dataset.info()
dataset.describe()
dataset.corr()
dataset['Region']
y=dataset[' Estimated Unemployment Rate (%)']
y
plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(12,10))
sns.heatmap(dataset.corr())
plt.show()
