import h5py
import numpy as np

# Load the dataset
file_path = "C:/Users/28905/Documents/NTU/semester2/CI/data/Skills.hdf5"
dataset = h5py.File(file_path, 'r')


# Since the dataset might be large, let's read a sample to understand the data better
sample_data = dataset[:1000]  # Read the first 1000 entries

# Convert bytes to strings for analysis if necessary
sample_data_str = np.array([d.decode('utf-8') for d in sample_data])

# Descriptive statistics
unique_elements, counts = np.unique(sample_data_str, return_counts=True)

# Display basic statistics
unique_elements, counts