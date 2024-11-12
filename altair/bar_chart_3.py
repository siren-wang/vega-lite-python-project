import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'value': [10, 15, 8, 20, 25, 12, 19, 21, 23],,
    'sales': [3, 7, 5, 10, 8, 7, 11, 9, 10]
})

bar_chart = alt.Chart(data).transform_fold(
    ['value', 'sales'],
    as_=['Measure', 'Value']
).mark_bar(size=20).encode(
    x='category:N',
    y='Value:Q',
    color='Measure:N'
).properties(
    title="Grouped Bar Chart",
    width="container",
    height=260
)
