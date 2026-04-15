import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file (make sure to replace with the correct file name/path)
data = pd.read_csv('history.csv')

# Clean column names by stripping unwanted spaces or quotes
data.columns = data.columns.str.strip().str.replace('"', '')

# Print the available columns to check
print("Available columns in the CSV file:", data.columns.tolist())

# Access the relevant columns
Time_iter_col = 'Time_Iter'
cd_col = 'CD'
cl_col = 'CL'

# Plot C_D (Drag Coefficient)
plt.figure(figsize=(8, 6))  # Create a new figure for C_D
plt.plot(data[Time_iter_col], data[cd_col], label='C_D', color='b')
plt.xlabel('Time Iterations')
plt.ylabel('C_D')
plt.title('Drag Coefficient (C_D) vs Time Iterations')
plt.legend()
plt.grid(True)

# Save the plot for C_D to a file
plt.savefig('C_D_plot.png')

# Close the figure to avoid overlap when plotting the next one
plt.close()

# Plot C_L (Lift Coefficient)
plt.figure(figsize=(8, 6))  # Create a new figure for C_L
plt.plot(data[Time_iter_col], data[cl_col], label='C_L', color='r')
plt.xlabel('Time Iterations')
plt.ylabel('C_L')
plt.title('Lift Coefficient (C_L) vs Time Iterations')
plt.legend()
plt.grid(True)

# Save the plot for C_L to a file
plt.savefig('C_L_plot.png')

# Close the figure after saving
plt.close()

print("Plots saved as 'C_D_plot.png' and 'C_L_plot.png'")
