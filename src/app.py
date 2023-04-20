from dotenv import load_dotenv
import pandas as pd
import os

# Load env variables
load_dotenv()
state = os.getenv('state')
assigned_to = os.getenv('assigned_to')
iteration_path = os.getenv('iteration_path')

# Read the original CSV file
original_data = pd.read_csv('files/source.csv')

# Rename the columns and drop some others
new_data = original_data.rename(columns={'Description': 'Title'})\
    .drop(columns=['Client', 'Project', 'Duration'])

# Split the Duration column into separate columns for hours, minutes, and seconds
duration_split = original_data['Duration']\
    .str\
    .split(':', expand=True)\
    .astype(int)

# Calculate the total duration in hours as a float
new_data['Completed Work'] = (duration_split[0] + duration_split[1]/60 + duration_split[2]/3600)\
    .round(decimals=3)
new_data['Original Estimate'] = new_data['Completed Work']

# Fill static variables
new_data['Remaining Work'] = 0
new_data['Work Item Type'] = "Task"

if not state == None:
    new_data['State'] = state
else:
    new_data['State'] = "New"

# Fill personal variables
if not assigned_to == None:
    new_data['Assigned To'] = assigned_to

if not iteration_path == None:
    new_data['Iteration Path'] = iteration_path


# Write the result to a new CSV file
new_data.to_csv('files/result.csv', index=False)
