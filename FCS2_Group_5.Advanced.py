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


'''      Prompt for user input and try except      '''
while True:
    User_input = input("please indicate the group size (4-10):  ")
    try:
        Check_input = int(User_input)
    except ValueError:
        print("The number entered must be an integer between 4 to 10")
        continue
    Group_size = int(User_input)
    if 4 <= Group_size <= 10 and Group_size != 9:
        number_of_groups = 50 // Group_size
        break
    elif Group_size == 9:
        print("9 in a group is not possible as there will be 5 leftovers. Adding them back will result in 10 in a group.")
        print("please try again")
        continue
    else:
        print("number not in range!")
        continue



'''       SORTING AND ADDING INTO GROUPS    '''
for tutorial in range(120):
    #sort by GPA first
    def cgpa_groups(student):
            return student["CGPA"]
    tutorial_ordered_list[tutorial].sort(key=cgpa_groups) 
        
    #Sort by gender next
    def gender_groups(student):
            return student["Gender"]
    tutorial_ordered_list[tutorial].sort(key=gender_groups) #then sort by gender


    '''      Algorithm to determine which gender to take out as "extra"     '''
    Number_of_extra_student = 50 - ((50 // Group_size) * Group_size)
    if Number_of_extra_student != 0:
        Gender_to_pop_out = tutorial_ordered_list[tutorial][25]['Gender']
        Potential_students_to_be_slotted_in_later = [x for x in tutorial_ordered_list[tutorial] if x['Gender'] == Gender_to_pop_out]
        Students_to_be_slotted_in_later = Potential_students_to_be_slotted_in_later[-(Number_of_extra_student):]
        Students_to_be_slotted_in_later.reverse()

        for student in Students_to_be_slotted_in_later:
            tutorial_ordered_list[tutorial].remove(student)

    
    #Algorithm to add all into their groups 
    grouping_list = split_into_groups(tutorial_ordered_list[tutorial], number_of_groups) #Split into number of groups prompted
    temp_list = [[] for n in range(number_of_groups)]
    for group in range(number_of_groups):
        for person in range(Group_size):
            temp_list[group].append(grouping_list[person][group]) 


    
    
    
    #This function is only used to visualize the students grouping
    def check_balance(category):
        if category == 'CGPA':
            for group in range(number_of_groups):
                total_sum = 0
                for member in range(Group_size):
                    total_sum += temp_list[group][member][category]
                print(total_sum / Group_size)
        else:
            correct = True
            for group in range(number_of_groups):
                counter = {}
                for member in range(Group_size):
                    category_value = temp_list[group][member][category]
                    print(category_value,end=', ')
                print()
                    

    

    

    #this should be used to check the balance in the grouping
        #Since we already sorted the list based on CGPA and Gender, I believe most of the groups will only have problems for school?
    def check_the_same_school(): #MIGHT HAVE TO CHANGE FUNC NAME TO RECTIFY_SCHOOL_INBALANCE()
        Imbalance_case = []
        school_of_each_group = [[] for n in range(number_of_groups)]
        for group in range(number_of_groups):
            for member in range(Group_size):
                school_of_each_group[group].append(temp_list[group][member]['School'])

        school_list = ['ADM', 'ASE', 'CCDS', 'CCEB', 'CEE', 'CoB (NBS)', 'CoE', 'EEE', 'HASS', 'LKCMedicine', 'MAE', 'MSE', 'NIE', 'SBS', 'SoH', 'SPMS', 'SSS', 'WKW SCI']

        for group in range(number_of_groups):
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
                    for target_group in range(number_of_groups): #iterate through school_of_each_group
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
                            

    '''Test out the code'''   
    check_the_same_school()


    '''   slotting extra member in again   '''
    if Number_of_extra_student != 0:
        average_list = [[] for n in range(number_of_groups)]
        for group in range(number_of_groups):
                total_sum = 0
                for member in range(Group_size):
                    total_sum += temp_list[group][member]['CGPA']
                average = total_sum / Group_size
                average_list[group] = average

        groups_that_need_more_members = sorted(average_list)[:Number_of_extra_student]
        index_of_groups_that_need_more_members = [average_list.index(x) for x in groups_that_need_more_members]
        for i, student in enumerate(Students_to_be_slotted_in_later):
            temp_list[index_of_groups_that_need_more_members[i]].append(student)


    n = 1
    for Team in temp_list:
        for member in Team:
            member['Team Number'] = n
        n += 1

    tutorial_ordered_list[tutorial] = temp_list


with open('new.record.csv', 'w') as new_record:
    new_record.write("Tutorial Group,Student ID,School,Name,Gender,CGPA,Team Number\n")
    for tutorial in tutorial_ordered_list:
        for individual_group in tutorial:
            for individual_member in individual_group:
                new_record.write(f"{individual_member['Tutorial Group']},{individual_member['Student ID']},{individual_member['School']},{individual_member['Name']},{individual_member['Gender']},{individual_member['CGPA']},{individual_member['Team Number']}\n")