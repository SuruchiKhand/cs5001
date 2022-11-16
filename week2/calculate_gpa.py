def calculate_gpa(current_gpa, num_classes, new_class_grade, expected_output):
    updated_class = int(num_classes + 1)    
    updated_gpa = float(current_gpa + new_class_grade)
    update_gpa = float(updated_gpa / updated_class)
    return update_gpa




