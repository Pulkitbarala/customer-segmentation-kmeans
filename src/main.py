from preprocessing import load_and_preprocess_data
from clustering import determine_optimal_clusters, apply_kmeans
from visualization import plot_clusters
import os


def main():
    # Load and preprocess the data
    file_path = 'data/Mall_Customers.csv'
    data = load_and_preprocess_data(file_path)
    
    # Select features for clustering
    features = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]
    
    # Determine the optimal number of clusters
    determine_optimal_clusters(features)
    
    # Apply K-Means clustering
    optimal_clusters = 5  # This should be determined from the Elbow plot
    cluster_labels = apply_kmeans(features, optimal_clusters)
    
    # Visualize the clusters
    plot_path = plot_clusters(data, cluster_labels)
    
    # Ensure the results directory exists
    os.makedirs('results', exist_ok=True)
    
    # Save a summary
    with open('results/summary.txt', 'w') as f:
        f.write("Customer Segmentation Analysis\n")
        f.write("Optimal number of clusters: {}\n".format(optimal_clusters))
        f.write("Cluster plot saved at: {}\n".format(plot_path))


if __name__ == "__main__":
    main() 