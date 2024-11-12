import altair as alt

# Grid Concatenation of Scatter and Circular Plots
concatenation = alt.concat(scatter_plot_3, circular_plot_3, scatter_plot_4, circular_plot_4, columns=2).properties(
    title="Grid Concatenation of Scatter and Circular Plots"
)
