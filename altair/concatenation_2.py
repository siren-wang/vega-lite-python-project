import altair as alt

# Vertical Concatenation of Scatter and Circular Plot
concatenation = alt.vconcat(scatter_plot_1, circular_plot_1).properties(
    title="Vertical Concatenation of Scatter and Circular Plot"
)
