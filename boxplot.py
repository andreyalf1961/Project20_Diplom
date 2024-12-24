import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

df = pd.read_csv("Life-Expectancy-Data-Averaged (1).csv")

# boxplot plt
df.boxplot(['Life_expectancy'], by=['Region'], rot=45, fontsize=5)
plt.show()

# boxplot sns
fig, ax = plt.subplots()
sns.boxplot(data=df, x=df['Region'], y=df['Life_expectancy'], hue='Region', palette='Set2')
plt.grid(True)
plt.xticks(rotation=45)
plt.title('Продолжительность жизни по регионам')
plt.show()

# boxplot px
fig_ = px.box(x=df['Region'], y=df['Life_expectancy'], points='all',
              title='продолжительность жизни по регионам', height=600)
fig_.show()
