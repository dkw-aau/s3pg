import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('data.csv')

# Sort the DataFrame by Category and then Dataset
df = df.sort_values(by=['Category', 'Dataset'])

# Reverse the order of unique categories
unique_categories = df['Category'].unique()[::-1]

# Set font family and size
plt.rcParams['font.family'] = 'Linux Libertine'
plt.rcParams['font.size'] = 13

# Create a grouped bar chart
fig, ax = plt.subplots(figsize=(5.5, 3), dpi=300)

# Extract unique dataset names from the DataFrame
datasets = df['Dataset'].unique()

# Determine bar width based on the number of datasets
bar_width = 0.4 / len(datasets)  # Adjusted width for dynamic number of datasets
bar_positions = range(len(unique_categories))

# Define colors for each dataset dynamically
colors = {dataset: plt.cm.get_cmap('tab10')(i) for i, dataset in enumerate(datasets)}

# Iterate over datasets in reverse order to match the legend with the bar order
for i, dataset in reversed(list(enumerate(datasets))):
    # Get the positions for each bar in the group
    positions = [p + bar_width * i for p in bar_positions]  # Adjusted positions

    # Choose hatches based on the dataset value
    hatch = '/' if dataset == datasets[0] else '\\'  # Use different hatches for different datasets

    # Plot bars for each category in the group with specified color and hatches
    ax.bar(positions, df[df['Dataset'] == dataset]['Time'], label=dataset, width=bar_width, alpha=0.7, hatch=hatch, edgecolor='black', color=colors.get(dataset, 'gray'))

# Set axis labels and title with increased font size
ax.set_xlabel('S3PG Transformation Model')
ax.set_ylabel('Time (Minutes)')

# Set x-axis ticks and labels with increased font size
ax.set_xticks([p + bar_width * (len(datasets) - 1) / 2 for p in bar_positions])
ax.set_xticklabels(unique_categories, fontsize=12)  # Use reversed order

# Set legend font size and move it to the center
ax.legend(title='Datasets', fontsize=12, bbox_to_anchor=(0.35, 0.9), loc="upper center", ncol=len(datasets))

# Remove border from top and right
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

plt.tight_layout()

# Save the plots as a high-quality PDF without borders
plt.savefig('monotonic_trans_time.pdf', bbox_inches='tight', pad_inches=0, transparent=True)

# Show the plot
plt.show()

