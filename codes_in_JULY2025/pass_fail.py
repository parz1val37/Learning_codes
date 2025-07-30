marks1 = int(input("Enter mark of Maths : "))
marks2 = int(input("Enter mark of Physics : "))
marks3 = int(input("Enter mark of Chemistry : "))

#total mark for each subject is 100

total_percentage = 100*(marks1 + marks2 + marks3)/300

if (total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3 >= 33):
    print("You have passed the exam with a percentage of", total_percentage)
else:
    print("You have failed the exam with a percentage of", total_percentage)
