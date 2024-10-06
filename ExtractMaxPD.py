# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 20:56:08 2024

@author: Ashish Bahuguna
Glenn Dept. of Civil Engineering
Clemson University
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to extract data from the text file
def extract_data_from_txt(file_path):
    data = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Skip initial lines and only read the data rows
        for line in lines[5:]:  # Assuming the data starts from the 8th line
            # Split the line into components and strip whitespace
            parts = line.strip().split()
            if len(parts) == 4:  # Ensure there are exactly four columns
                # Convert to float and append to the data list
                data.append([float(part) for part in parts])

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data, columns=['T', 'PI_CO', 'PI_PI', 'PI_SO'])
    # Calculate the difference between column 1 (X) and column 4 (PI_PI) and store it in Col5
    df['Rel_CO'] = df['PI_SO'] - df['PI_CO']
    # df['Rel_PI'] = df['PI_SO'] - df['PI_PI']
    
    # Calculate the absolute values of Col5 and find the maximum absolute value
    max_abs_value = df['Rel_CO'].abs().max()
    # max_abs.append(max_abs_value)
    # print('Max PD',max_abs_value)
    return df, max_abs_value


# Function to process multiple text files in a directory
def process_multiple_files_in_directory(directory):
    all_dataframes = []
    max_abs_values = []

    # Get a list of all .txt files in the given directory
    file_list = [f for f in os.listdir(directory) if f.endswith('.txt')]
    
    for file_name in file_list:
        file_path = os.path.join(directory, file_name)
        print(f'Processing {file_path}...')
        data_frame, max_abs_value = extract_data_from_txt(file_path)
        
        all_dataframes.append(data_frame)
        max_abs_values.append(max_abs_value)

        # Print the DataFrame for the current file
        # print(data_frame)
        # print(f'Maximum absolute value of Col5 in {file_path}: {max_abs_value}\n')

        # Plot Col2 (PI_SO) against Col5 for the current DataFrame
        plt.figure(figsize=(10, 6))
        plt.plot(data_frame['T'], data_frame['Rel_CO'], linestyle='--', color='r')
        plt.title(f'{os.path.basename(file_path)}')
        plt.xlabel('Time(s)')
        plt.ylabel('Disp. (m)')
        plt.grid()
        plt.show()
    column_vector = [[element] for element in  max_abs_values]
    
    print('Max Peak Disp. for ',file_path)
    for element in  max_abs_values:
        print(element)
    return all_dataframes, max_abs_values


# Specify the directory containing the text files
directory = 'C:/Users/abahugu/OneDrive - Clemson University/Desktop/New folder (2)/Northridge/'  # Replace with your actual directory path
all_dataframes, max_abs_values = process_multiple_files_in_directory(directory)

# Optionally, save each DataFrame to a separate CSV file
for i, df in enumerate(all_dataframes):
    df.to_csv(f'extracted_data_file_{i+1}.csv', index=False)
    
    
# # Specify the path to your text file
# file_path = 'C:/Users/abahugu/OneDrive - Clemson University/Desktop/New folder (2)/3x3-4d-Elcentro-0-1.odbU1.txt'  # Replace with your file path
# data_frame, maxPD = extract_data_from_txt(file_path)

# # Print the DataFrame
# # print(data_frame)

# # Plot Col2 (PI_SO) against Col5
# plt.figure(figsize=(10, 6))
# # plt.plot(data_frame['T'], data_frame['Rel_PI'], linestyle='-', color='b')
# plt.plot(data_frame['T'], data_frame['Rel_CO'], linestyle='--', color='r')
# # plt.title('Plot of Rel_PI vs. Col5')
# plt.xlabel('Time(s)')
# plt.ylabel('Disp. (m)')
# plt.grid()
# plt.show()


# # Optionally, save to a CSV file
# data_frame.to_csv('extracted_data.csv', index=False)
