# Write a python script that will take in a name and compare it to a list of faculty and a list
# of students. If the name is in the faculty list then it will greet the user as a faculty and
# exit, and if the name is in the student list then it will greet the user as a student, inform
# the student of the next due assignment, and then prompt for another name. The lists are
# as follows:
#           Faculty: "Rucker, Gatto, Doheny, Ingersoll, Lauer"
#           Students: "Johnson, Russell, Zeck, Nehdar, Sainz"

listStudents = ['Johnson','Russell','Zeck','Nehdar','Sainz']
listFaculty = ['Rucker','Gatto','Doheny','Ingersoll','Lauer']

def main():

    name = input("Name: ")
    for j in listFaculty:
        if name == j:
            print("Goodbe, Mr.",name)
        break
    for j in listStudents:
        if name == j:
            name = input("Name: ")
    print("Goodybye, Mr.",name)




            #print("This is,", listFaculty.append(name))
            #print(listFaculty
main()


