import matplotlib.pyplot as plt
import pandas as pd

# Your CSV data
data = {
    'Category': ['Non-Parsimonious', 'Non-Parsimonious', 'Parsimonious', 'Parsimonious'],
    'Dataset': ['Dbp22dec', 'Dbp22march', 'Dbp22dec', 'Dbp22march'],
    'Time': [14, 23, 39, 26]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Set font family and size
plt.rcParams['font.family'] = 'Linux Libertine'
plt.rcParams['font.size'] = 13

# Define the custom order for 'Category'
custom_order = ['Parsimonious', 'Non-Parsimonious']

# Convert 'Category' to a categorical type with the custom order
df['Category'] = pd.Categorical(df['Category'], categories=custom_order, ordered=True)

# Pivot the DataFrame to create a bar chart
pivot_df = df.pivot(index='Category', columns='Dataset', values='Time')

# Reorder the columns for each category
pivot_df = pivot_df[['Dbp22march', 'Dbp22dec']]

# Plot the bar chart
ax = pivot_df.plot(kind='bar', stacked=False, figsize=(7, 5))
#
# Set different hatches for each dataset
for i, container in enumerate(ax.containers):
    hatch = '/' if i % 2 == 0 else '\\'
    for patch in container.patches:
        patch.set_hatch(hatch)

# Set labels and title
ax.set_xlabel('S3PG Transformation Model')
ax.set_ylabel('Time (minutes)')
# ax.set_title('Bar Chart Grouped by Category')

# Rotate x-axis labels to be horizontal
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)

# Remove border from top and right
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

# Save the plots as a high-quality PDF without borders
plt.savefig('monotonic_trans_time.pdf', bbox_inches='tight', pad_inches=0, transparent=True)

# Show the plot
plt.show()
