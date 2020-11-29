# ---------------- Import ----------------
import matplotlib.pyplot as plt
import numpy as np

# Plot data
def plotData(x, y):
  # Plot
  plt.title('Rain - Temperature')
  plt.plot(x, y, '.')
  plt.show()

# Print stats 
def printStats(x, y):
  # Print
  print("The mean temperature is: ")
  print(np.mean(x))

  print("The total amount of rain is: ")
  print(np.sum(x))