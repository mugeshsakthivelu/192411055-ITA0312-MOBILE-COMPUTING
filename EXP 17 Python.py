
import math

# Get input values
i = int(input("Enter i value: "))
j = int(input("Enter j value: "))
total_channels = int(input("Enter Total Channels: "))

# Calculate cluster size
N = i**2 + i*j + j**2

# Calculate system capacity
capacity = total_channels // N

# Calculate reuse ratio
q = math.sqrt(3 * N)

# Calculate S/I ratio (for 6 co-channel interferers)
si = (q**4) / 6

# Convert S/I into dB
si_db = 10 * math.log10(si)

# Display results
print("\nCluster Size:", N)
print("System Capacity:", capacity, "channels per cell")
print("S/I Ratio:", round(si_db, 2), "dB")
