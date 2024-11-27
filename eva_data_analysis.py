import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe.
    Clean the data by removing any incomplete rows and sort by date

    Args:
        input_file (str): The path to the JSON file.

    Returns:
        eva_df (pd.DataFrame): The cleaned and sorted data as a dataframe
    """
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    # Pandas doesn't import eva column as a float - fix
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Drop cases where eva didn't actually occur
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """
    Writes the dataframe to a CSV file for later analysis

    Args:
        df (pd.DataFrame): Dataframe to be exported to CSV
        output_file (str): Path to the csv to be created
    """
    print(f'Saving to CSV file {output_file}')
    df.to_csv(output_file, index=False)


def plot_cumulative_time_in_space(df, graph_file):
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv','w')
graph_file = './cumulative_eva_graph.png'

# Read data from the JSON file
eva_df = read_json_to_dataframe(input_file)

# Data saved as csv for later analysis
write_dataframe_to_csv(eva_df, output_file)

# Calculate duration of each spacewalk, and cumulative total time
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1]) / 60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# Create plot of total duration of spacewalks to date
plot_cumulative_time_in_space(eva_df, graph_file)
