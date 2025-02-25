import plotly.express as px
import pandas as pd

tasks = ['Mysore pak', 'Donut', 'Kaju Barfi', 'Gulab Jamun']
start_dates = ['2025-03-01', '2025-03-05', '2025-03-10', '2025-03-12']
end_dates = ['2025-03-04', '2025-03-08', '2025-03-14', '2025-03-15']

df = pd.DataFrame({
    'Task': tasks,
    'Start': start_dates,
    'Finish': end_dates
})


fig = px.timeline(df, x_start="Start", x_end="Finish", y="Task", title="Gantt Chart", labels={"Task": "Sweets"})
fig.update_yaxes(categoryorder="total ascending")
fig.show()
