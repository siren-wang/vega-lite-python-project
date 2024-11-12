import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

scatter_plot = alt.Chart(data).mark_circle(size=100).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).mark_text(align='left', baseline='middle', dx=7).encode(
    text='category:N'
).properties(
    title="Scatter Plot with Labels",
    width="container",
    height=250
)