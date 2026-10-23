import pandas as pd
import os

def clean_data(file_path):
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)
    
    # Cleaning steps
    df = df.drop_duplicates()
    df.fillna({'Product': 'Unknown', 'Price': 0, 'Stock': 0}, inplace=True)
    
    output_filename = 'cleaned_' + os.path.basename(file_path)
    output_path = os.path.join('static', output_filename)
    df.to_csv(output_path, index=False)
    
    return output_path