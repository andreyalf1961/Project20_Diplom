import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.graph_objects as go

df = pd.read_csv("Life-Expectancy-Data-Averaged (1).csv")
df_year = pd.read_csv("Life-Expectancy-Data-Updated.csv")
sel = ['Japan', 'Lesotho', 'Israel']
df_selected = df_year[df_year['Country'].isin(sel)]
df_selected = df_selected.sort_values(by='Year')

# plt
for i in df_selected['Year']:
    x = df_selected['Life_expectancy']
    y = df_selected['GDP_per_capita']
    z = df_selected['Year']
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z)
plt.show()


def func_z(x, y):
    return x ** 2 + y ** 3


n = 50
X_VAL = np.linspace(-5, 5, n)
Y_VAL = np.linspace(-5, 5, n)
X1, Y1 = np.meshgrid(X_VAL, Y_VAL)
Z1 = func_z(X1, Y1)

axes = plt.axes(projection="3d")
axes.plot_surface(X1, Y1, Z1)
plt.show()

# plotly
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title=dict(text='Mt Bruno Elevation'), autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
