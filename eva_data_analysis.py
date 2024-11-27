import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv','w')
graph_file = './cumulative_eva_graph.png'

eva_df = pd.read_json(input_file, convert_dates=['date'])
# Pandas doesn't import eva column as a float - fix
eva_df['eva'] = eva_df['eva'].astype(float)
# Drop cases where eva didn't actually occur
eva_df.dropna(axis=0, inplace=True)
eva_df.sort_values('date', inplace=True)

# Data saved as csv for later analysis
eva_df.to_csv(output_file, index=False)

# Calculate duration of each spacewalk, and cumulative total time
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1]) / 60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# Create plot of total duration of spacewalks to date
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
