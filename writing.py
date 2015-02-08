f = open("new_scores.txt", "w")
#STUDENTS: the file name here was originally `scores.txt`


while True:
    student = input("Enter Student's name: ")
    if student == 'quit':
        print("Thanks! We're done")
        break
    grade = input("Enter the student's grade: ")
    f.write(student + "," + grade + "\n")

f.close()
