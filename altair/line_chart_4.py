import altair as alt
import pandas as pd

data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [3, 7, 5, 10, 8]
})

line_chart = alt.Chart(data).mark_line(interpolate='step-after').encode(
    x='month:N',
    y='sales:Q'
).properties(
    title="Step Line Chart",
    width="container",
    height=250
)
