import pandas

student_dict = {
    "student":["angela","bob","lily"],
    "scores":[98,44,23]
}

for (key, value) in student_dict.items():
    print(value)


student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)
for (key, value) in student_data_frame.items():
    print(value)

#loop through rows in dataframe
for (index, row) in student_data_frame.iterrows():
    print(row.student)

    if row.student == "angela":
        print(row.scores)