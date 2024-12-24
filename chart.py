import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px

df = pd.read_csv("Life-Expectancy-Data-Averaged (1).csv")
des = df['Life_expectancy'].describe()
life_exp_more50 = df[df['Life_expectancy'] > des['mean']]

# Bar chart matplotlib
plt.figure(figsize=(15, 6))
plt.bar(life_exp_more50['Country'], life_exp_more50['Life_expectancy'], color='#f39c12')
plt.xlabel("Countries")
plt.ylabel("Life Expectancy")
plt.title("Countries with Life Expectancy Above the Mean")
plt.xticks(rotation=90)
plt.show()

# bar chart seaborn
f, ax = plt.subplots(figsize=(15, 6))
(sns.barplot(x=life_exp_more50['Country'], y=life_exp_more50['Life_expectancy']).
 set(title='Countries with Life Expectancy Above the Mean'))
ax.tick_params(axis='x', labelrotation=90, labelsize=5)
plt.show()

# bar chart plotly
fig = px.bar(x=life_exp_more50['Country'], y=life_exp_more50['Life_expectancy'],
             title='Countries with Life Expectancy Above the Mean',
             labels={'y': 'Life_expectancy', 'x': 'Country'}, height=600)
fig.show()
