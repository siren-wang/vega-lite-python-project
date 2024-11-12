import altair as alt

# Horizontal Concatenation of Two Line Charts
concatenation = alt.hconcat(line_chart_3, line_chart_4).properties(
    title="Horizontal Concatenation of Two Line Charts"
)
