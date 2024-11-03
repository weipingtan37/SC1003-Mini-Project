# Initialize Global Variable STUDENTS_LIST and append the information from the CSV File 
STUDENTS_LIST = []
with open('records.csv', 'r') as records:
    next(records) # Start from second line onwards
    for student in records:
        tutorial_group, student_id, school, name, gender, cgpa = student.strip().split(',')
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
    tutorial_ordered_list[0].sort(key=cgpa_groups) #sort by GPA first
    
    def gender_groups(student):
            return student["Gender"]
    
    tutorial_ordered_list[0].sort(key=gender_groups) #then sort by gender


    grouping_list = split_into_groups(tutorial_ordered_list[0], 10)
    
    temp_list = [[], [], [], [], [], [], [], [], [], []]

    for j in range(10):
        for n in range(5):
            temp_list[j].append(grouping_list[n][j])



    
    
    #this function is only used to visualize the students grouping, need another function to return the weird case for the grouping
    def check_balance(catogery):
        if catogery == 'CGPA':
            for group in range(10):
                total_sum = 0
                for member in range(5):
                    total_sum += temp_list[group][member][catogery]
                print(total_sum / 5)
        else:
            for group in range(10):
                for member in range(5):
                    print(temp_list[group][member][catogery],end=', ')
                print()
    
    check_balance('School')
    print()
    check_balance('Gender')
    print()
    check_balance('CGPA')

    
    
    #this should be used to check the balance in the grouping
    #Since we already sorted the list based on CGPA and Gender, I believe most of the groups will only have problems for school?
    def check_the_same_school(): #MIGHT HAVE TO CHANGE FUNC NAME TO RECTIFY_SCHOOL_INBALANCE()
        Imbalance_case = []
        school_of_each_group = [[], [], [], [], [], [], [], [], [], []]
        for group in range(10):
            for member in range(5):
                school_of_each_group[group].append(temp_list[group][member]['School'])

        school_list = ['ADM', 'ASE', 'CCDS', 'CCEB', 'CEE', 'CoB (NBS)', 'CoE', 'EEE', 'HASS', 'LKCMedicine', 'MAE', 'MSE', 'NIE', 'SBS', 'SoH', 'SPMS', 'SSS', 'WKW SCI']

        for group in range(10):
            school_counts = {}
            for school in school_of_each_group[group]:
                if school in school_counts:
                    school_counts[school] += 1
                else:
                    school_counts[school] = 1
            print(f"Group {group} counts:", school_counts) #for debugging

    
            for school, count in school_counts.items():
                if count >= 3: #if inbalanced we swap
                    Imbalance_case.append(school_of_each_group[group])
                    print(f"Imbalance found in group {group} for school {school}") 
                
                    #swap begins here
                    for target_group in range(10): #iterate through school_of_each_group
                        if target_group != group: #ensure group(target_group) to swap is not the same as grp with inbalanced sch
                            for target_member, target_school in enumerate(school_of_each_group[target_group]):
                                if target_school != school: #ensure sch swapped is diff
                                    # swap a member from the imbalanced group with the target group
                                    for member, member_school in enumerate(school_of_each_group[group]):#iterate thru problem grp till we find the sch to swap
                                        if member_school == school:
                                            # Swap the students between groups
                                            temp_list[group][member], temp_list[target_group][target_member] = temp_list[target_group][target_member], temp_list[group][member]

                                            # Update school_of_each_group to reflect the swap
                                            school_of_each_group[group][member], school_of_each_group[target_group][target_member] = school_of_each_group[target_group][target_member], school_of_each_group[group][member]

                                            # Break after swap to avoid multiple swaps at once
                                            break
                                # Check if imbalance is resolved after each swap
                                
                                school_counts[school] -= 1
                                if school_counts[school] < 3:
                                    break #break inner loop
                        if school_counts[school] < 3:
                            break #break outer loop


    # Return the list of imbalanced groups after attempted swaps
        return Imbalance_case #SHOULD BE BALANCED NOW
        
        
    groups_that_need_member_switch = check_the_same_school()
    print(groups_that_need_member_switch)
    print()
    print("After swapping: ")
    print()    
    check_balance('School')
    print()
    check_balance('Gender')
    print()
    check_balance('CGPA')


