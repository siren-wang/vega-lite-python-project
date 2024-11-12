import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

scatter_plot = alt.Chart(data).mark_circle(size=100, opacity=0.5).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).properties(
    title="Scatter Plot with Opacity",
    width="container",
    height=250
)
