import pandas as pd

def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Check for missing values and fill them
    if data.isnull().sum().any():
        data.fillna(data.mean(), inplace=True)
    
    # Convert categorical data if needed
    # Example: Convert 'Gender' to numerical
    data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
    
    return data 