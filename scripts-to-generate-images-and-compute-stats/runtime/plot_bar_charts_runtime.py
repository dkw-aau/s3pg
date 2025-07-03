import matplotlib.pyplot as plt
from matplotlib import gridspec
import pandas as pd
import numpy as np

# Read data from the CSV file for group_A
group_A_data = pd.read_csv('singleType.csv')
group_B_data = pd.read_csv('multiTypeHomoLit.csv')
group_C_data = pd.read_csv('multiTypeHomoLitNonLit.csv')
group_D_data = pd.read_csv('multiTypeHeteroLitNonLit.csv')

# Convert the DataFrames to dictionaries in the desired format
group_A = {
    'Index': group_A_data['Index'].tolist(),
    'RDF': group_A_data['KG'].tolist(),
    'S3PG': group_A_data['S3PG'].tolist(),
    'NeoSemantics': group_A_data['NeoSemantics'].tolist(),
    'RDF2PG': group_A_data['RDF2PG'].tolist()
}

group_B = {
    'Index': group_B_data['Index'].tolist(),
    'RDF': group_B_data['KG'].tolist(),
    'S3PG': group_B_data['S3PG'].tolist(),
    'NeoSemantics': group_B_data['NeoSemantics'].tolist(),
    'RDF2PG': group_B_data['RDF2PG'].tolist()
}

group_C = {
    'Index': group_C_data['Index'].tolist(),
    'RDF': group_C_data['KG'].tolist(),
    'S3PG': group_C_data['S3PG'].tolist(),
    'NeoSemantics': group_C_data['NeoSemantics'].tolist(),
    'RDF2PG': group_C_data['RDF2PG'].tolist()
}

group_D = {
    'Index': group_D_data['Index'].tolist(),
    'RDF': group_D_data['KG'].tolist(),
    'S3PG': group_D_data['S3PG'].tolist(),
    'NeoSemantics': group_D_data['NeoSemantics'].tolist(),
    'RDF2PG': group_D_data['RDF2PG'].tolist()
}

# Define colors with lighter tones
colors = ['#9ecae1', '#66c2a5', '#fd8d3c', '#e6550d']

# Set the font family to "Linux Libertine"
plt.rcParams['font.family'] = 'Linux Libertine'

fig = plt.figure(figsize=(15, 3), dpi=300)

# Create a gridspec with different widths for each subplot
gs = gridspec.GridSpec(1, 4, width_ratios=[1, 1, 1, 2])

# Create subplots using the gridspec
axs = [plt.subplot(gs[i]) for i in range(4)]

# Width of each bar group
width = 0.2

# Hatch patterns
hatches = ['//', '\\\\', 'xx', '--']

# Bar plot in the first subplot
index = np.arange(len(group_A['Index']))
for i, dataset in enumerate(['RDF', 'S3PG', 'NeoSemantics', 'RDF2PG']):
    bars = axs[0].bar(index - 1.5 * width + i * width, group_A[dataset], width, label=dataset, color=colors[i], edgecolor='k', hatch=hatches[i])
axs[0].set_title('   (a) Single Type \n Queries  ', fontsize=11)
axs[0].set_xlabel('Query', fontsize=11)
axs[0].set_ylabel('Time (ms) ', fontsize=11)
axs[0].set_xticks(index)
axs[0].set_xticklabels(group_A['Index'])
axs[0].legend().set_visible(False)
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].tick_params(axis='x', labelsize=10)  # Reduce x-axis label font size
axs[0].tick_params(axis='y', labelsize=10)  # Reduce y-axis label font size

# Bar plot in the second subplot
index = np.arange(len(group_B['Index']))
for i, dataset in enumerate(['RDF', 'S3PG', 'NeoSemantics', 'RDF2PG']):
    bars = axs[1].bar(index - 1.5 * width + i * width, group_B[dataset], width, label=dataset, color=colors[i], edgecolor='k', hatch=hatches[i])
axs[1].set_title('   (b) Multi Type Homo \n (Literals) Queries  ', fontsize=11)
axs[1].set_xlabel('Query', fontsize=11)
axs[1].set_xticks(index)
axs[1].set_xticklabels(group_B['Index'])
axs[1].legend().set_visible(False)
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].tick_params(axis='x', labelsize=10)  # Reduce x-axis label font size
axs[1].tick_params(axis='y', labelsize=10)  # Reduce y-axis label font size

# Bar plot in the third subplot
index = np.arange(len(group_C['Index']))
for i, dataset in enumerate(['RDF', 'S3PG', 'NeoSemantics', 'RDF2PG']):
    bars = axs[2].bar(index - 1.5 * width + i * width, group_C[dataset], width, label=dataset, color=colors[i], edgecolor='k', hatch=hatches[i])
axs[2].set_title('   (c) Multi Type Homo \n (Non-Literals) Queries', fontsize=11)
axs[2].set_xlabel('Query', fontsize=11)
axs[2].set_xticks(index)
axs[2].set_xticklabels(group_C['Index'])
axs[2].legend().set_visible(False)
axs[2].spines['top'].set_visible(False)
axs[2].spines['right'].set_visible(False)
axs[2].tick_params(axis='x', labelsize=10)  # Reduce x-axis label font size
axs[2].tick_params(axis='y', labelsize=10)  # Reduce y-axis label font size

# Bar plot in the fourth subplot (group_D) with more width
index = np.arange(len(group_D['Index']))
for i, dataset in enumerate(['RDF', 'S3PG', 'NeoSemantics', 'RDF2PG']):
    bars = axs[3].bar(index - 1.5 * width + i * width, group_D[dataset], width, label=dataset, color=colors[i], edgecolor='k', hatch=hatches[i])
axs[3].set_title('   (d) Multi Type Hetero (Literals & Non-Literals) \n Queries', fontsize=11)
axs[3].set_xlabel('Query', fontsize=11)
axs[3].set_xticks(index)
axs[3].set_xticklabels(group_D['Index'])
axs[3].legend(loc='upper center', fontsize=8)
axs[3].spines['top'].set_visible(False)
axs[3].spines['right'].set_visible(False)
axs[3].tick_params(axis='x', labelsize=10, rotation=45)  # Reduce x-axis label font size
axs[3].tick_params(axis='y', labelsize=10)

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# Save the plots as a high-quality PDF without borders
plt.savefig('query_execution_time.pdf', bbox_inches='tight', pad_inches=0, transparent=True)

# Show the plots (not necessary if you only want to save the PDF)
plt.show()
