def get_patient():
    all_patient = []  # create a list for all patients information
    num_patient = 1  # count the number of patient
    while True:
        ind_patient = []  # create list for each patient information
        print(f"Patient #{num_patient}")
        #  for input firstname, lastname and patient id
        firstname = input("What is your first name?: ")
        lastname = input("What is your last name?: ")
        patient_id = input("Enter your ID?: ")
        # for check whether patient id equal to 6 digits
        while len(patient_id) != 6:
            patient_id = input("Enter your ID?: ")
        # for input patient's age and symptoms
        age = int(input("How old are you?: "))
        symptoms = input("What symptom do you have?: ")
        symptom = symptoms.split(' ')  # for separate the symptoms of patient who has multiple symptoms
        # for check if there are more patient to input the information
        more = input("More patient?(y/n): ")
        print("******")
        # for append firstname, lastname, id, age and symptom of each patient
        ind_patient.append(firstname)
        ind_patient.append(lastname)
        ind_patient.append(patient_id)
        ind_patient.append(age)
        ind_patient.append(symptom)
        # for append all information of individual patient to list of all patients
        all_patient.append(ind_patient)
        num_patient += 1
        if more == 'n':
            break
    return all_patient


def find_age_above(all_patient, age):
    age_above = []  # make a list for storing the id of patient that have age more than or equal to provided age
    for i in range(len(all_patient)):
        if all_patient[i][3] >= age:  # check the age of patient in the list to get the one who can get in requirement
            age_above.append(all_patient[i][2])  # append id of patient who is older or equal to age provided in list
    return age_above


def print_patient(all_patient, patient_id):
    same_id = []  # create list for all patients that have id same as the required id
    for patient in range(len(all_patient)):
        indi_id = []  # create list for store information of individual patient who has id same as provided id
        for digit in patient_id:  # for assign j as each digit of required id
            if all_patient[patient][2] == digit:  # for check each digit of patient's id whether it same as the required one
                # for append firstname, lastname and id of patient in individual patient list respectively
                indi_id.append(all_patient[patient][0])
                indi_id.append(all_patient[patient][1])
                indi_id.append(all_patient[patient][2])
                same_id.append(indi_id)  # for append all information of patient who has same id as required id in list
    for id_ in range(len(same_id)):
        print(f"ID:{same_id[id_][2]} {same_id[id_][0]} {same_id[id_][1]}")


def find_symptoms(all_patient, symptoms):
    same_symptom = []  # create list for store information of patients who have symptom same as the required one
    for individual in range(len(all_patient)):
        for symptom in all_patient[individual][4]:  # for find the name of symptoms of each patient
            if symptom == symptoms:  # for check symptom of each patient whether it is the same as required one
                same_symptom.append(all_patient[individual][2])  # append id of patient who has same symptom as the required one in list
    return same_symptom


# Main part
# Fill in code for main part below

# insert patient information
input_patient = get_patient()
# find list of patient by age
input_age = int(input("Type Age: "))
print(f"Output the name of the patient with age more than {input_age}.")
print_patient(input_patient, find_age_above(input_patient, input_age))
# find list of patient by symptom
input_symptom = input("Type Symptoms: ")
print(f"Output the name of the patient with {input_symptom} symptoms.")
print_patient(input_patient, find_symptoms(input_patient, input_symptom))
