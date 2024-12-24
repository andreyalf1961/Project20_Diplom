import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px


df = pd.read_csv("Life-Expectancy-Data-Averaged (1).csv")

# hist matplotlib
plt.hist(df['Life_expectancy'], range=(45,85),bins=8, color='skyblue', edgecolor='black')
plt.xlabel('Life Expectancy')
#plt.ylabel('Count')
plt.title('Distribution of Life Expectancy')
plt.show()

# hist seaborn
sns.histplot(df, x='Life_expectancy', palette=sns.set_palette("viridis"),
             kde=True,binwidth=5,binrange=(45,85))
plt.show()

sns.displot(df, x='Life_expectancy', hue='Region', kde=True, rug=True,bins=8,binrange=(45,85))
plt.ylabel("Frequency")
plt.title("Distribution of Life Expectancy")
plt.show()

# hist plotpy
fig=px.histogram(df, x='Life_expectancy', labels={'y':'Frequency'},height=600,width=600)
fig.show()