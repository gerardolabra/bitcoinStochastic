import os
import pandas as pd

# Function to process raw BTC data
def process_btc_data():
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the input and output file paths
    input_file = os.path.join(script_dir, '../../data/raw/btc_data.csv')
    output_dir = os.path.join(script_dir, '../../data/processed')
    output_file = os.path.join(output_dir, 'btc_data_processed.csv')
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Read raw data
    df = pd.read_csv(input_file)
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Sort by timestamp
    df = df.sort_values(by='timestamp')
    
    # Generate additional features (e.g., moving averages, volatility)
    df['moving_avg_7'] = df['close'].rolling(window=7).mean()
    df['moving_avg_30'] = df['close'].rolling(window=30).mean()
    df['volatility_7'] = df['close'].rolling(window=7).std()
    df['volatility_30'] = df['close'].rolling(window=30).std()
    
    # Save processed data
    df.to_csv(output_file, index=False)
    print(f"Data processed and saved to {output_file}")

# Process data
if __name__ == '__main__':
    process_btc_data()