import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

bar_chart = alt.Chart(data).transform_fold(
    ['value', 'sales'],
    as_=['Measure', 'Value']
).mark_bar().encode(
    x='category:N',
    y='Value:Q',
    color='Measure:N'
).properties(
    title="Grouped Bar Chart",
    width="container",
    height=260
)
