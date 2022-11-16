
from calculate_gpa import calculate_gpa

# Test One: 0.0, 0 classes, get a 3.5 GPA should be 3.5
print(calculate_gpa(0.0, 0, 3.5, 3.5))

# Test Two: 4.0, 1 class, get another 4.0, GPA is still 4.0
print(calculate_gpa(4.0, 1, 4.0, 4.0))

# Test Three: 3.0, 5 classes, get another 3.0, GPA should be 1.0
print(calculate_gpa(3.0, 5, 3.0, 1.0 ))