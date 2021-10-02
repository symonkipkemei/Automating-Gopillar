import Database


print("We are going to store all the data collected and "
      "store into the database provided below")

def main():
    Id = Database.insertIntoProjectsTable()
    correct = False
    while not correct:
        print("Choose option \n"
              "(1) Store into project Table\n"
              "(2) Store into Deliverables Table\n")

        userOption = int(input("Choice : "))

        if userOption == 1:
            Database.insertIntoProjectsTable()
            print("Project information inserted")

        elif userOption == 2:
            Database.insertIntoDeliverablesTable(Id)
            print("Project deliverables stored")

        elif userOption == 3:
            correct = True


main()
