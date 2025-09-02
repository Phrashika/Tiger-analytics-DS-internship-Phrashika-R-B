# Question 20: Pathology Lab Test Comparison

# Healthy patient data (ideal values)
healthy_data = {
    "Sugar level": 15,
    "Blood pressure": 32,
    "Heartbeat rate": 71,
    "weight": 65,
    "fat percentage": 10
}

# Take patient input values
patient_data = {}
for key in healthy_data.keys():
    val = int(input(f"Enter patient's {key}: "))
    patient_data[key] = val

# Show patient data
print("\n--- Patient Data ---")
for key, val in patient_data.items():
    print(f"{key}: {val}")

# Calculate differences
differences = {}
for key in healthy_data:
    differences[key] = patient_data[key] - healthy_data[key]

print("\n--- Differences Dictionary ---")
print(differences)

# Show detailed report
print("\n--- Detailed Report ---")
for key, diff in differences.items():
    if diff < 0:
        print(f"{key} {diff}\n{key} is {-diff} less than the ideal value\n")
    elif diff > 0:
        print(f"{key} {diff}\n{key} is {diff} more than the ideal value\n")
    else:
        print(f"{key} {diff}\n{key} is exactly at the ideal value\n")
