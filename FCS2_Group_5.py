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

        tutorial_ordered_list = []
    def split_into_groups(records_list, group_size):
        # Using list comprehension to split the list into chunks of size `sublist_size`
        return [records_list[i:i + group_size] for i in range(0, len(records_list), group_size)]
                  
    tutorial_ordered_list = split_into_groups(STUDENTS_LIST, 50)
    # print("ITS STARTS HERE")
    # print(tutorial_ordered_list)

        # def cgpa_groups(cgpa):
        #     if cgpa >= 4.5:
        #         return 'High'
        #     elif cgpa >= 4.0:
        #         return 'Mid'
        #     else:
        #         return 'Low'
        # for student in STUDENTS_LIST:
        #     student['CGPA Group'] = cgpa_groups(student['CGPA'])

    def cgpa_groups(student):
            return student["CGPA"]
    
    # Later put in loop to sort all 120 tutorial groups
    print("It starts here")
    tutorial_ordered_list[0].sort(key=cgpa_groups)
    
    def gender_groups(student):
            return student["Gender"]
    
    tutorial_ordered_list[0].sort(key=gender_groups)

    split_into_groups(tutorial_ordered_list[0], 10)

    temp_list = [[], [], [], [], [],[], [], [], [], []]
    print(temp_list)

    for n in range(5):
        for j in range(10):
             temp_list[j].append(tutorial_ordered_list[0][n])

    print("BBQ")
    print(temp_list)
