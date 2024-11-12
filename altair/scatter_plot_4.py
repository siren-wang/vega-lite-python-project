import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'value': [10, 15, 8, 20, 25, 12, 19, 21, 23],,
    'sales': [3, 7, 5, 10, 8, 7, 11, 9, 10]
})

scatter_plot = alt.Chart(data).mark_circle().encode(
    x='value:Q',
    y='sales:Q',
    size='value:Q',
    color='category:N'
).properties(
    title="Bubble Chart",
    width="container",
    height=250
)
