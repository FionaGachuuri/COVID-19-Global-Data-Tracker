#!/usr/bin/env python3
"""
COVID-19 Data Downloader and Preprocessor
This script downloads the latest COVID-19 dataset from Our World in Data
and performs initial preprocessing to prepare it for analysis.
"""

import os
import pandas as pd
import urllib.request
import argparse
from datetime import datetime


def download_covid_data(output_dir='data'):
    """
    Downloads the latest COVID-19 dataset from Our World in Data.
    
    Parameters:
    output_dir (str): Directory to save the downloaded data
    
    Returns:
    str: Path to the downloaded file
    """
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    
    # Data source URL
    data_url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    
    # Output file path
    today = datetime.now().strftime("%Y%m%d")
    output_file = os.path.join(output_dir, f"owid-covid-data_{today}.csv")
    standard_file = os.path.join(output_dir, "owid-covid-data.csv")
    
    # Download the data
    print(f"Downloading COVID-19 data from {data_url}...")
    try:
        urllib.request.urlretrieve(data_url, output_file)
        print(f"Data downloaded successfully to {output_file}")
        
        # Save as the standard filename for use in the notebook
        urllib.request.urlretrieve(data_url, standard_file)
        print(f"Data also saved as {standard_file}")
        
        return output_file
    except Exception as e:
        print(f"Error downloading data: {e}")
        return None

def preprocess_data(input_file, output_file=None):
    """
    Performs initial preprocessing on the COVID-19 dataset.
    
    Parameters:
    input_file (str): Path to the input CSV file
    output_file (str): Path to save the processed file (optional)
    
    Returns:
    pandas.DataFrame: Preprocessed DataFrame
    """
    print(f"Preprocessing data from {input_file}...")
    
    try:
        # Load the data
        df = pd.read_csv(input_file)
        
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Filter out aggregated regions
        df = df[~df['location'].isin(['World', 'European Union', 'International'])].copy()
        
        # Handle missing values for critical columns
        for col in ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']:
            # Group by location and forward fill within each group
            df[col] = df.groupby('location')[col].transform(lambda x: x.fillna(method='ffill'))
        
        # Fill remaining NaNs with 0
        numeric_cols = ['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 
                        'total_vaccinations', 'people_vaccinated']
        df[numeric_cols] = df[numeric_cols].fillna(0)
        
        # Calculate additional metrics
        # Death rate (%)
        df['death_rate'] = (df['total_deaths'] / df['total_cases'] * 100).replace([np.inf, -np.inf], np.nan).fillna(0)
        
        # Vaccination rate (%)
        df['vaccination_rate'] = (df['people_vaccinated'] / df['population'] * 100).replace([np.inf, -np.inf], np.nan).fillna(0)
        
        # 7-day moving averages
        df['new_cases_smoothed'] = df.groupby('location')['new_cases'].transform(lambda x: x.rolling(window=7).mean())
        df['new_deaths_smoothed'] = df.groupby('location')['new_deaths'].transform(lambda x: x.rolling(window=7).mean())
        
        print(f"Preprocessing complete. DataFrame shape: {df.shape}")
        
        # Save processed data if output file is specified
        if output_file:
            df.to_csv(output_file, index=False)
            print(f"Processed data saved to {output_file}")
        
        return df
    
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Download and preprocess COVID-19 data')
    parser.add_argument('--data-dir', default='data', help='Directory to store data files')
    parser.add_argument('--no-download', action='store_true', help='Skip downloading and use existing data')
    parser.add_argument('--no-preprocess', action='store_true', help='Skip preprocessing')
    args = parser.parse_args()
    
    # Download data unless skipped
    input_file = os.path.join(args.data_dir, "owid-covid-data.csv")
    if not args.no_download:
        downloaded_file = download_covid_data(args.data_dir)
        if not downloaded_file:
            print("Download failed. Exiting.")
            return
    
    # Preprocess data unless skipped
    if not args.no_preprocess:
        output_file = os.path.join(args.data_dir, "processed_covid_data.csv")
        df = preprocess_data(input_file, output_file)
        if df is not None:
            print("Data ready for analysis.")
    
    print("Done!")

if __name__ == "__main__":
    import numpy as np
    main()