import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

circular_plot = alt.Chart(data).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("value:Q"),
    color="category:N"
).properties(
    title="Donut Chart",
    width="container",
    height=250
)
