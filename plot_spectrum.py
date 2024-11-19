import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Path to the file
file_path = '/Users/louptl/Desktop/NTNU/Material physics/Lab 3/Lab3_6/P2.txt'

# Lists to store x and y data
x_data = []
y_data = []

# Read the file line by line
with open(file_path, 'r') as file:
    data_section = False  # flag to indicate when we reach the data section
    for line in file:
        # Identify the start of data
        if "SPECTRUM    : Spectral Data Starts Here" in line:
            data_section = True
            continue
        if "ENDOFDATA" in line:
            break
        
        # If we're in the data section, parse x and y values
        if data_section:
            # Split line by commas and strip spaces
            values = line.strip().split(',')
            if len(values) == 2:
                try:
                    x_val = float(values[0].strip())
                    y_val = float(values[1].strip())
                    x_data.append(x_val)
                    y_data.append(y_val)
                except ValueError:
                    # Skip lines that can't be converted to float (header or malformed lines)
                    continue

# Convert lists to numpy arrays for peak detection
x_data = np.array(x_data)
y_data = np.array(y_data)

# Find peaks in the y_data with a minimum height threshold to avoid noise
peaks, _ = find_peaks(y_data, height=500)  

# Plotting the data
plt.figure(figsize=(13, 6))
plt.plot(x_data, y_data, label="Spectral Data", color='blue')
plt.xlabel("Energy (keV)")
plt.ylabel("Counts")
plt.title("EDS Spectral Data Plot - Minimal Peak height annoted: 500")
plt.legend()
plt.grid(True)


# Annotate peaks
for peak in peaks:
    plt.annotate(f'{x_data[peak]:.2f} keV',  # Label with the energy value
                 (x_data[peak], y_data[peak]),
                 textcoords="offset points",
                 xytext=(0, 10),  # Offset the label a bit above the peak
                 ha='center',
                 color='red',
                 fontsize=8)


plt.savefig('/Users/louptl/Desktop/NTNU/Material physics/Lab 3/P2_spectrum.png', bbox_inches='tight')
plt.show()
