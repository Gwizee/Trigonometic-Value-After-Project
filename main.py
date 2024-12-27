import math

angle = float(input("Enter an angle in degree: "))

angle_in_radians = math.radians(angle)

sin_value = math.sin(angle_in_radians)
cos_value = math.cos(angle_in_radians)
tan_value = math.tan(angle_in_radians)

print(f"Sine Value of {angle}: {sin_value}")
print(f"Cosine Value of {angle}: {cos_value}")
print(f"Tangent Value of {angle}: {tan_value}")