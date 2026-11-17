
import math

# Get input values
frequency = float(input("Enter Frequency (MHz): "))
distance = float(input("Enter Distance (km): "))
tx_power = float(input("Enter Transmitted Power (dBm): "))

# Calculate Free Space Path Loss
fspl = 32.44 + (20 * math.log10(frequency)) + (20 * math.log10(distance))

# Calculate Received Power
rx_power = tx_power - fspl

# Display results
print("\nFree Space Path Loss:", round(fspl, 2), "dB")
print("Received Power:", round(rx_power, 2), "dBm")
