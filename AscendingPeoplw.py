import numpy as np

#define data type (structured array)
data_type = [
    ('name', 'S15'), # string of max 15 charecters
    ('class', int),  # integer  
    ('height', float)  # float
]

#student details
student_details = [
    ("Jack", 4, 142.67),
    ("Jill", 4, 143.28),
    ("Paul", 5, 148.7),
    ("Dash", 6, 148.64),
    ("Neil", 5, 141.87)
]

students = np.array(student_details, dtype=data_type)

print("Original array:")
print(students)

print("\n Sorted by height(Ascending Order)")
sorted_students = np.sort(students, order='height')
print(sorted_students)
