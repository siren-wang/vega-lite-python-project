import altair as alt
import pandas as pd

data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

line_chart = alt.Chart(data).transform_fold(
    ['value', 'sales'],
    as_=['Measure', 'Value']
).mark_line().encode(
    x='month:N',
    y='Value:Q',
    color='Measure:N'
).properties(
    title="Multi-Line Chart",
    width="container",
    height=250
)
