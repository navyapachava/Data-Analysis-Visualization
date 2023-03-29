import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a Pandas dataframe
df = pd.read_csv('./Bacterial_Isolates_Explorer.csv', header=0)

# Print the first 5 rows of the dataframe
print(df.head())

# Count the number of unique bacterial species
species_counts = df['Bacterial Species'].nunique()
print(f'There are {species_counts} unique bacterial species in the dataset')


# Define a dictionary to map each Origin to a specific color
color_map = {'Human feces': 'red', 'Milk': 'blue', 'Pig intestine': 'green'}

# Generate a list of colors for each point based on the Origin column
colors = [color_map[origin] for origin in df['Origin']]

# Create the scatterplot with color-coded points
plt.figure(figsize=(10, 12))
plt.scatter(df['Bacterial Species'], df['Origin'], c=colors)
plt.title('Bacterial Species vs Origin')
plt.xlabel('Bacterial Species')
plt.xticks(rotation=15, fontsize = 8)
plt.ylabel('Origin')

# Define a dictionary to map each susceptibility to a specific color
color_map = {'Susceptible':'green', 'Resistant': 'red'}

# Create the scatter plot with color-coded points
fig, ax = plt.subplots(figsize=(12, 8))
for susceptible, group in df.groupby('Susceptibility'):
    group.plot(kind='scatter', x='Bacterial Species', y='Antibiotic ', c=color_map[susceptible],
               label=susceptible, ax=ax)

# Set the axis labels and title
ax.set_xlabel('Bacterial Species')
plt.xticks(rotation=15, fontsize = 8)
ax.set_ylabel('Antibiotic')
ax.set_title('Bacterial Species and Antibiotic Susceptibility')

# Set the legend and show the plot
ax.legend()
plt.show()