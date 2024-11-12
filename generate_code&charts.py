import altair as alt
import pandas as pd

# Sample data
data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [3, 7, 5, 10, 8]
})

# Function to save chart and code files
def save_chart_and_code(chart, chart_name, code):
    # Save the chart as an HTML file
    chart.save(f'charts/{chart_name}.html')

    # Save the Altair code
    with open(f'altair/{chart_name}.py', 'w') as f:
        f.write(code)

    # Save the Vega-Lite JSON
    vega_lite_json = chart.to_json()
    with open(f'vega/{chart_name}.json', 'w') as f:
        f.write(vega_lite_json)

### 1. Bar Charts

# Bar Chart 1: Simple vertical bar chart
bar_chart_1 = alt.Chart(data).mark_bar().encode(
    x='category:N',
    y='value:Q',
).properties(
    title="Simple Vertical Bar Chart",
    width="container",
    height=260
)

bar_chart_1_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

bar_chart = alt.Chart(data).mark_bar().encode(
    x='category:N',
    y='value:Q',
).properties(
    title="Simple Vertical Bar Chart",
    width="container",
    height=260
)
'''

save_chart_and_code(bar_chart_1, "bar_chart_1", bar_chart_1_code)

# Bar Chart 2: Horizontal bar chart with color
bar_chart_2 = alt.Chart(data).mark_bar().encode(
    y='category:N',
    x='value:Q',
    color='category:N'
).properties(
    title="Horizontal Bar Chart with Color",
    width="container",
    height=250
)

bar_chart_2_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

bar_chart = alt.Chart(data).mark_bar().encode(
    y='category:N',
    x='value:Q',
    color='category:N'
).properties(
    title="Horizontal Bar Chart with Color",
    width="container",
    height=260
)
'''

save_chart_and_code(bar_chart_2, "bar_chart_2", bar_chart_2_code)

# Bar Chart 3: Grouped bar chart
bar_chart_3 = alt.Chart(data).transform_fold(
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

bar_chart_3_code = '''import altair as alt
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
'''

save_chart_and_code(bar_chart_3, "bar_chart_3", bar_chart_3_code)

# Bar Chart 4: Stacked bar chart
bar_chart_4 = alt.Chart(data).mark_bar().encode(
    x='category:N',
    y='value:Q',
    color='category:N'
).properties(
    title="Stacked Bar Chart",
    width="container",
    height=260
)

bar_chart_4_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

bar_chart = alt.Chart(data).mark_bar().encode(
    x='category:N',
    y='value:Q',
    color='category:N'
).properties(
    title="Stacked Bar Chart",
    width="container",
    height=260
)
'''

save_chart_and_code(bar_chart_4, "bar_chart_4", bar_chart_4_code)

### 2. Line Charts

# Line Chart 1: Simple line chart
line_chart_1 = alt.Chart(data).mark_line().encode(
    x='month:N',
    y='sales:Q'
).properties(
    title="Simple Line Chart",
    width="container",
    height=250
)

line_chart_1_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [3, 7, 5, 10, 8]
})

line_chart = alt.Chart(data).mark_line().encode(
    x='month:N',
    y='sales:Q'
).properties(
    title="Simple Line Chart",
    width="container",
    height=250
)
'''

save_chart_and_code(line_chart_1, "line_chart_1", line_chart_1_code)

# Line Chart 2: Line chart with points
line_chart_2 = alt.Chart(data).mark_line(point=True).encode(
    x='month:N',
    y='sales:Q',
    color='month:N'
).properties(
    title="Line Chart with Points",
    width="container",
    height=250
)

line_chart_2_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [3, 7, 5, 10, 8]
})

line_chart = alt.Chart(data).mark_line(point=True).encode(
    x='month:N',
    y='sales:Q',
    color='month:N'
).properties(
    title="Line Chart with Points",
    width="container",
    height=250
)
'''

save_chart_and_code(line_chart_2, "line_chart_2", line_chart_2_code)

# Line Chart 3: Multi-line chart
line_chart_3 = alt.Chart(data).transform_fold(
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

line_chart_3_code = '''import altair as alt
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
'''

save_chart_and_code(line_chart_3, "line_chart_3", line_chart_3_code)

# Line Chart 4: Step line chart
line_chart_4 = alt.Chart(data).mark_line(interpolate='step-after').encode(
    x='month:N',
    y='sales:Q'
).properties(
    title="Step Line Chart",
    width="container",
    height=250
)

line_chart_4_code = '''import altair as alt
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
'''

save_chart_and_code(line_chart_4, "line_chart_4", line_chart_4_code)

### 3. Circular Plots

# Circular Plot 1: Radial bar chart
circular_plot_1 = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta("value:Q", stack=True),
    color="category:N"
).properties(
    title="Radial Bar Chart",
    width="container",
    height=250
)

circular_plot_1_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

circular_plot = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta("value:Q", stack=True),
    color="category:N"
).properties(
    title="Radial Bar Chart",
    width="container",
    height=250
)
'''

save_chart_and_code(circular_plot_1, "circular_plot_1", circular_plot_1_code)

# Circular Plot 2: Pie chart
circular_plot_2 = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta("value:Q"),
    color="category:N"
).properties(
    title="Pie Chart",
    width="container",
    height=250
)

circular_plot_2_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

circular_plot = alt.Chart(data).mark_arc().encode(
    theta=alt.Theta("value:Q"),
    color="category:N"
).properties(
    title="Pie Chart",
    width="container",
    height=250
)
'''

save_chart_and_code(circular_plot_2, "circular_plot_2", circular_plot_2_code)

# Circular Plot 3: Donut chart
circular_plot_3 = alt.Chart(data).mark_arc(innerRadius=50).encode(
    theta=alt.Theta("value:Q"),
    color="category:N"
).properties(
    title="Donut Chart",
    width="container",
    height=250
)

circular_plot_3_code = '''import altair as alt
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
'''

save_chart_and_code(circular_plot_3, "circular_plot_3", circular_plot_3_code)

# Circular Plot 4: Sunburst-like radial bar chart
circular_plot_4 = alt.Chart(data).mark_arc(innerRadius=100, outerRadius=200).encode(
    theta=alt.Theta("value:Q"),
    color="category:N"
).properties(
    title="Sunburst-like Radial Bar Chart",
    width="container",
    height=250
)

circular_plot_4_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25]
})

circular_plot = alt.Chart(data).mark_arc(innerRadius=100, outerRadius=200).encode(
    theta=alt.Theta("value:Q"),
    color="category:N"
).properties(
    title="Sunburst-like Radial Bar Chart",
    width="container",
    height=250
)
'''

save_chart_and_code(circular_plot_4, "circular_plot_4", circular_plot_4_code)

### 4. Scatter Plots

# Scatter Plot 1: Simple scatter plot
scatter_plot_1 = alt.Chart(data).mark_circle(size=100).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).properties(
    title="Simple Scatter Plot",
    width="container",
    height=245
)

scatter_plot_1_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

scatter_plot = alt.Chart(data).mark_circle(size=100).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).properties(
    title="Simple Scatter Plot",
    width="container",
    height=245
)
'''

save_chart_and_code(scatter_plot_1, "scatter_plot_1", scatter_plot_1_code)

# Scatter Plot 2: Scatter plot with opacity
scatter_plot_2 = alt.Chart(data).mark_circle(size=100, opacity=0.5).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).properties(
    title="Scatter Plot with Opacity",
    width="container",
    height=250
)

scatter_plot_2_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

scatter_plot = alt.Chart(data).mark_circle(size=100, opacity=0.5).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).properties(
    title="Scatter Plot with Opacity",
    width="container",
    height=250
)
'''

save_chart_and_code(scatter_plot_2, "scatter_plot_2", scatter_plot_2_code)

# Scatter Plot 3: Scatter plot with text labels
scatter_plot_3 = alt.Chart(data).mark_circle(size=100).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).mark_text(align='left', baseline='middle', dx=7).encode(
    text='category:N'
).properties(
    title="Scatter Plot with Labels",
    width="container",
    height=250
)

scatter_plot_3_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

scatter_plot = alt.Chart(data).mark_circle(size=100).encode(
    x='value:Q',
    y='sales:Q',
    color='category:N'
).mark_text(align='left', baseline='middle', dx=7).encode(
    text='category:N'
).properties(
    title="Scatter Plot with Labels",
    width="container",
    height=250
)
'''

save_chart_and_code(scatter_plot_3, "scatter_plot_3", scatter_plot_3_code)

# Scatter Plot 4: Bubble chart
scatter_plot_4 = alt.Chart(data).mark_circle().encode(
    x='value:Q',
    y='sales:Q',
    size='value:Q',
    color='category:N'
).properties(
    title="Bubble Chart",
    width="container",
    height=250
)

scatter_plot_4_code = '''import altair as alt
import pandas as pd

data = pd.DataFrame({
    'category': ['A', 'B', 'C', 'D', 'E'],
    'value': [10, 15, 8, 20, 25],
    'sales': [3, 7, 5, 10, 8]
})

scatter_plot = alt.Chart(data).mark_circle().encode(
    x='value:Q',
    y='sales:Q',
    size='value:Q',
    color='category:N'
).properties(
    title="Bubble Chart",
    width="container",
    height=250
)
'''

save_chart_and_code(scatter_plot_4, "scatter_plot_4", scatter_plot_4_code)

### 5. Concatenation

# Concatenation 1: Horizontal concatenation of bar and line chart
concatenation_1 = alt.hconcat(bar_chart_1, line_chart_1).properties(
    title="Horizontal Concatenation of Bar and Line Chart"
)

concatenation_1_code = '''import altair as alt

# Horizontal Concatenation of Bar and Line Chart
concatenation = alt.hconcat(bar_chart_1, line_chart_1).properties(
    title="Horizontal Concatenation of Bar and Line Chart"
)
'''

save_chart_and_code(concatenation_1, "concatenation_1", concatenation_1_code)

# Concatenation 2: Vertical concatenation of scatter and circular plot
concatenation_2 = alt.vconcat(scatter_plot_1, circular_plot_1).properties(
    title="Vertical Concatenation of Scatter and Circular Plot"
)

concatenation_2_code = '''import altair as alt

# Vertical Concatenation of Scatter and Circular Plot
concatenation = alt.vconcat(scatter_plot_1, circular_plot_1).properties(
    title="Vertical Concatenation of Scatter and Circular Plot"
)
'''

save_chart_and_code(concatenation_2, "concatenation_2", concatenation_2_code)

# Concatenation 3: Horizontal concatenation of two line charts
concatenation_3 = alt.hconcat(line_chart_3, line_chart_4).properties(
    title="Horizontal Concatenation of Two Line Charts"
)

concatenation_3_code = '''import altair as alt

# Horizontal Concatenation of Two Line Charts
concatenation = alt.hconcat(line_chart_3, line_chart_4).properties(
    title="Horizontal Concatenation of Two Line Charts"
)
'''

save_chart_and_code(concatenation_3, "concatenation_3", concatenation_3_code)

# Concatenation 4: Grid concatenation of scatter and circular plots
concatenation_4 = alt.concat(scatter_plot_3, circular_plot_3, scatter_plot_4, circular_plot_4, columns=2).properties(
    title="Grid Concatenation of Scatter and Circular Plots"
)

concatenation_4_code = '''import altair as alt

# Grid Concatenation of Scatter and Circular Plots
concatenation = alt.concat(scatter_plot_3, circular_plot_3, scatter_plot_4, circular_plot_4, columns=2).properties(
    title="Grid Concatenation of Scatter and Circular Plots"
)
'''

save_chart_and_code(concatenation_4, "concatenation_4", concatenation_4_code)
