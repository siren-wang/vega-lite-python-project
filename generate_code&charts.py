import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [3, 7, 5, 4, 6, 8, 5, 6, 7, 9],
    'z': [7, 2, 6, 3, 8, 7, 4, 5, 9, 10]
})

# Define charts and save both HTML and Python code
charts = {
    "bar_chart": alt.Chart(data).mark_bar().encode(x='x', y='y'),
    "line_chart": alt.Chart(data).mark_line().encode(x='x', y='y'),
    "scatter_plot": alt.Chart(data).mark_circle(size=100).encode(x='x', y='z', color='y')
}

for name, chart in charts.items():
    # Save the HTML chart
    chart.save(f'charts/{name}.html')

    # Define Python code string and save it as .py file
    code = f"""
import altair as alt
import pandas as pd

data = pd.DataFrame({{
    'x': range(10),
    'y': [3, 7, 5, 4, 6, 8, 5, 6, 7, 9],
    'z': [7, 2, 6, 3, 8, 7, 4, 5, 9, 10]
}})

chart = alt.Chart(data).mark_{'bar' if 'bar' in name else 'line' if 'line' in name else 'circle(size=100)'}().encode(
    x='x',
    y='y'{" if 'bar' in name else ', color=\'y\', y=\'z\'" if 'scatter' in name else ""}
)
"""
    with open(f'code/{name}.py', 'w') as f:
        f.write(code)
