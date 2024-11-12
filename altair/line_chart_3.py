import altair as alt
import pandas as pd

data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
    'value': [10, 15, 8, 20, 25, 12, 19, 21, 23],,
    'sales': [3, 7, 5, 10, 8, 7, 11, 9, 10]
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
