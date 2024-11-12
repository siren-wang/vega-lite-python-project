import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

bar_chart = alt.Chart(data).mark_bar().encode(
    y='category:N',
    x='value:Q',
    color='category:N'
).properties(
    title="Horizontal Bar Chart with Color",
    width="container",
    height=260
)
