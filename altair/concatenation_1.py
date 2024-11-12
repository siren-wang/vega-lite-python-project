import altair as alt

# Horizontal Concatenation of Bar and Line Chart
concatenation = alt.hconcat(bar_chart_1, line_chart_1).properties(
    title="Horizontal Concatenation of Bar and Line Chart"
)
