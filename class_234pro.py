import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

dataset = pd.read_csv('projectC234_EPL.csv')

goals_columns = dataset['Goals']

sorted_club_data_by_ascending_order = goals_columns.groupby(dataset['Club'])

sum_of_goals_by_each_club = sorted_club_data_by_ascending_order.sum()

sorted_goals_values = sorted_club_data_by_ascending_order.sort_values(ascending = False)

print(sorted_goals_values)

top_goals = dataset.sort_values(by=['Goals'], ascending = False)[:10]

print(top_goals)

fig = px.bar(top_goals, x = 'Name', y = 'Goals', hover_data = ['Club', 'Age'], text = ' Goals')

fig.show()