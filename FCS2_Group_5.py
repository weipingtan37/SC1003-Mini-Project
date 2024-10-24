# Initialize Global Variable STUDENTS_LIST and append the information from the CSV File 
STUDENTS_LIST = []
with open('records.csv', 'r') as records:
    next(records) # Start from second line onwards
    for student in records:
        tutorial_group, student_id, name, school, gender, cgpa = student.strip().split(',')
        STUDENTS_LIST.append({
            'Tutorial Group': tutorial_group,
            'Student ID': student_id,
            'Name': name,
            'School': school,
            'Gender': gender,
            'CGPA': float(cgpa)
        })

        def cgpa_groups(cgpa):
            if cgpa >= 4.5:
                return 'High'
            elif cgpa >= 4.0:
                return 'Mid'
            else:
                return 'Low'
        for student in STUDENTS_LIST:
            student['CGPA Group'] = cgpa_groups(student['CGPA']) #gangster1234567
