import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'value': [10, 15, 8, 20, 25, 12, 19, 21, 23],
})

bar_chart = alt.Chart(data).mark_bar(size=20).encode(
    x='category:N',
    y='value:Q',
).properties(
    title="Simple Vertical Bar Chart",
    width="container",
    height=260
)
