import math

# Input angle in degrees
angle_deg = float(input("enter a value in degrees:   "))

# Convert degrees to radians
angle_rad = math.radians(angle_deg)

# Calculate values
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)
tan_val = math.tan(angle_rad)

# Print results
print(f"Results for {angle_deg} degrees:")
print(f"Sine:   {sin_val}")
print(f"Cosine: {cos_val}")
print(f"Tangent: {tan_val}")
