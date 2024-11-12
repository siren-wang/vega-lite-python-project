import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    'value': [10, 15, 8, 20, 25, 12, 19, 21, 23],
})

circular_plot = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta("value:Q", stack=True),
    color="category:N"
).properties(
    title="Radial Bar Chart",
    width="container",
    height=250
)
