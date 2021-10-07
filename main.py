import sqlite3

import Database

# welcome message
print("Hello! This AUTOMATING GO-PILLAR!\n"
      "We will be storing updating the sql database with Go-pillar projects \n"
      "and analyze later."
      "Please insert information as requested.\n")


#
def main():
    """main programme running"""

    correct = False
    while not correct:
        print("(1). Add project to database\n"
        "(2). View database\n"
        "(3). End program")


        userInput = int(input("Enter: "))

        if userInput == 1:
            try:
                Id = Database.insertIntoProjectsTable()
                print("Project information stored")
                Database.insertIntoDeliverablesTable(Id)
                print("Project deliverables stored")
                Database.insertIntoSpacesTable(Id)
                print("Spaces stored")
            except sqlite3.IntegrityError:
                print("Project Already recorded in the database.")
            correct = False

        elif userInput == 2:
            print("This feature is not available at the moment"
                  "\ncoming soon!")
            correct = False

        elif userInput == 3:
            print("The end"
                  "\nThank you!")
            correct = True
        else:
            print("wrong input, try again.")
            correct = False


main()
