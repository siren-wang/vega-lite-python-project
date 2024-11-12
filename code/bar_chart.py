
import altair as alt
import pandas as pd

data = pd.DataFrame({
    'x': range(10),
    'y': [3, 7, 5, 4, 6, 8, 5, 6, 7, 9],
    'z': [7, 2, 6, 3, 8, 7, 4, 5, 9, 10]
})

chart = alt.Chart(data).mark_bar().encode(
    x='x',
    y='y'
)
