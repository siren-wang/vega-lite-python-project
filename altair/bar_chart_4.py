import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

bar_chart = alt.Chart(data).mark_bar().encode(
    x='category:N',
    y='value:Q',
    color='category:N'
).properties(
    title="Stacked Bar Chart",
    width="container",
    height=260
)