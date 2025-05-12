import matplotlib.pyplot as plt
import seaborn as sns
import os


def plot_clusters(data, cluster_labels, output_dir='results/cluster_plots/'):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Add cluster labels to the data
    data['Cluster'] = cluster_labels
    
    # Create a scatter plot
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=data, palette='viridis')
    plt.title('Customer Segments')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend(title='Cluster')
    
    # Save the plot
    plot_path = os.path.join(output_dir, 'customer_segments.png')
    plt.savefig(plot_path)
    plt.close()
    
    return plot_path 