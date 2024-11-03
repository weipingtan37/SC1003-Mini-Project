'''     APPENDING INFO FROM CSV     '''
# Initialize Global Variable STUDENTS_LIST and append the information from the CSV File 
STUDENTS_LIST = []
with open('records.csv', 'r') as records:
    next(records) # Start from second line onwards
    for student in records:
        tutorial_group, student_id, school, name, gender, cgpa = student.strip().split(',')
        STUDENTS_LIST.append({ #Adding each student into dictionary
            'Tutorial Group': tutorial_group,
            'Student ID': student_id,
            'Name': name,
            'School': school,
            'Gender': gender,
            'CGPA': float(cgpa)
        })
        tutorial_ordered_list = []


    
    '''       SPLIT INTO TUTORIAL GROUPS       '''
    def split_into_groups(records_list, group_size):
        return [records_list[i:i + group_size] for i in range(0, len(records_list), group_size)]
    
    #Spliting the groups based on tutorial            
    tutorial_ordered_list = split_into_groups(STUDENTS_LIST, 50)




    '''       SORTING AND ADDING INTO GROUPS    '''
    for individual_tutorial in tutorial_ordered_list: #can slice the ordered list here 
        #sort by GPA first
        def cgpa_groups(student):
                return student["CGPA"]
        individual_tutorial.sort(key=cgpa_groups) 
        
        #Sort by gender next
        def gender_groups(student):
                return student["Gender"]
        individual_tutorial.sort(key=gender_groups) #then sort by gender

        #Algorithm to add all into their groups 
        grouping_list = split_into_groups(individual_tutorial, 10) #Split into 5 groups of 10
        temp_list = [[], [], [], [], [], [], [], [], [], []]
        for group in range(10):
            for person in range(5):
                temp_list[group].append(grouping_list[person][group]) 

        


        '''        CHECK BALANCE FUNCTION AND SWAPPING GROUPS       '''
        #This function is only used to visualize the students grouping
        def check_balance(category):
            if category == 'CGPA':
                for group in range(10):
                    total_sum = 0
                    for member in range(5):
                        total_sum += temp_list[group][member][category]
                    print(total_sum / 5)
            else:
                correct = True
                for group in range(10):
                    counter = {}
                    for member in range(5):
                        category_value = temp_list[group][member][category]
                        '''print(category_value,end=', ')'''
                        if category_value in counter:
                            counter[category_value] += 1
                        else:
                            counter[category_value] = 1
                    for key, count in counter.items():
                        if category == 'School' and count >= 3:
                            correct = False 
                        if category == 'Gender' and count >3:
                            correct = False
                if correct == True:
                    print('correct')
                else: 
                    print('wrong')


        '''
        check_balance('School')
        print()
        check_balance('Gender')
        print()
        check_balance('CGPA')
        '''
        


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
                #print(f"Group {group} counts:", school_counts) #for debugging
                for school, count in school_counts.items():
                    if count >= 3: #if inbalanced we swap
                        Imbalance_case.append(school_of_each_group[group])        
                        #swap begins here
                        for target_group in range(10): #iterate through school_of_each_group
                            if target_group != group:
                                for target_member, target_school in enumerate(school_of_each_group[target_group]):
                                    if target_school != school: #ensure sch swapped is diff
                                        # swap a member from the imbalanced group with the target group
                                        need_repeat = True 
                                        for member, member_school in enumerate(school_of_each_group[group]):#iterate thru problem grp till we find the sch to swap
                                            if need_repeat == False:
                                                break
                                            if member_school == school and temp_list[target_group][target_member]['Gender'] == temp_list[group][member]['Gender']:
                                                # Swap the students between groups
                                                temp_list[group][member], temp_list[target_group][target_member] = temp_list[target_group][target_member], temp_list[group][member]

                                                # Update school_of_each_group to reflect the swap
                                                school_of_each_group[group][member], school_of_each_group[target_group][target_member] = school_of_each_group[target_group][target_member], school_of_each_group[group][member]
                                                school_counts[school] -= 1    
                                                need_repeat = False
                                                                                    
                                                #check if both swapped is fine 
                                                grouping = [target_group, group]
                                                for diff_group in grouping:
                                                    if need_repeat == True:
                                                        break
                                                    school_target_count = {}
                                                    for schools in school_of_each_group[diff_group]:
                                                        if schools in school_target_count:
                                                            school_target_count[schools] += 1
                                                        else:
                                                            school_target_count[schools] = 1
                                                    # use this print(school_target_count)
                                                    #print(f"Group {group} counts:", school_counts) #for debugging
                                                    for schools, counts in school_target_count.items():
                                                        if counts >= 3 and schools == school and diff_group == group: 
                                                            need_repeat = True
                                                            break
                                                        elif counts >= 3: #if inbalanced we swap
                                                            temp_list[target_group][target_member], temp_list[group][member] = temp_list[group][member], temp_list[target_group][target_member]
                                                            school_of_each_group[target_group][target_member], school_of_each_group[group][member] =  school_of_each_group[group][member], school_of_each_group[target_group][target_member]
                                                            school_counts[school] += 1
                                                            need_repeat = True 
                                                
                                                # Break after swap to avoid multiple swaps at once
                                                break
                                            # Check if imbalance is resolved after each swap\

                                    if school_counts[school] < 3:
                                        break #break inner loop 
                                if school_counts[school] < 3:
                                    break #break outer loop
                                

        #testing out code   
        check_the_same_school()
        n = 1
        for Team in temp_list:
            for member in Team:
                member['Team Number'] = n
            n += 1
        #check_balance('School')
        #check_balance('School')
        #print(groups_that_need_member_switch)
        #print()
        #print("After swapping: ")
        #print() 
        #check_balance('School')
        #print() 
        #check_balance('CGPA')
        #print()
        #check_balance('Gender')
        #print()

    
    #can use if change plan
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

with open('new.record.csv', 'w') as new_record:
    new_record.write("Tutorial Group,Student ID,School,Name,Gender,CGPA,Team Number\n")
    for individual_tutorial in tutorial_ordered_list:
        for individual_member in individual_tutorial:
            new_record.write(f"{individual_member['Tutorial Group']},{individual_member['Student ID']},{individual_member['School']},{individual_member['Name']},{individual_member['Gender']},{individual_member['CGPA']},{individual_member['Team Number']}\n")
            
    
