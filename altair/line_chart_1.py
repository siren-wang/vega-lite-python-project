import altair as alt
import pandas as pd

data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
    'sales': [3, 7, 5, 10, 8, 7, 11, 9, 10]
})

line_chart = alt.Chart(data).mark_line().encode(
    x='month:N',
    y='sales:Q'
).properties(
    title="Simple Line Chart",
    width="container",
    height=250
)
