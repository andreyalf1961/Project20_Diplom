import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

df = pd.read_csv("Life-Expectancy-Data-Averaged (1).csv")

# scatter mpl
plt.scatter(df['GDP_per_capita'], df['Life_expectancy'], color='r')
plt.xlabel('ВВП')
plt.ylabel('Продолжительность жизни')
plt.title('ВВП и продолжительность жизни')
plt.grid()
plt.show()

# scatter sns
sns.scatterplot(x=df['GDP_per_capita'], y=df['Life_expectancy'], color='g')
plt.xlabel('ВВП')
plt.ylabel('Продолжительность жизни')
plt.title('ВВП и продолжительность жизни')
plt.grid()
plt.show()

# scatter px
fig = px.scatter(x=df['GDP_per_capita'], y=df['Life_expectancy'], hover_name=df['Country'],
                 title='ВВП и продолжительность жизни', labels={'x': 'ВВП', 'y': 'Продолжительность жизни'}, height=600)
fig.show()
