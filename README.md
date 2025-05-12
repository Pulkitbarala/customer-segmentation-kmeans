# Customer Segmentation Analysis

This project performs customer segmentation analysis using K-Means clustering on the `Mall_Customers.csv` dataset. The dataset includes features such as CustomerID, Gender, Age, Annual Income (k$), and Spending Score (1-100).

## Project Structure

```
customer-segmentation/
├── data/
│   └── Mall_Customers.csv
├── src/
│   ├── main.py
│   ├── preprocessing.py
│   ├── clustering.py
│   └── visualization.py
├── results/
│   ├── cluster_plots/
│   └── summary.txt
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.x
- Pandas
- Scikit-Learn
- Matplotlib
- Seaborn

Install the required packages using:

```
pip install -r requirements.txt
```

## Usage

1. Place the `Mall_Customers.csv` file in the `data/` directory.
2. Run the main script:

```
python src/main.py
```

3. The results will be saved in the `results/` directory, including cluster plots and a summary file.

## Insights

The analysis provides insights into customer segments, which can help a retail company optimize marketing strategies by targeting different customer groups based on their purchasing behavior. 