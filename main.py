import sqlite3

import DatabaseInsertion

# welcome message
print("^^^^^^^^^^^^^^^^^^^^^^^^^AUTOMATING GO-PILLAR^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
      "Hello!\n"
      "I am an algorithm that collects existing design data on spatial configurations of\n"
      "apartments and curates it into instant design solutions based on the spatial\n"
      "parameters given. The intention is to shorten the design decision-making process\n"
      "into milliseconds.\n"
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
                Id = DatabaseInsertion.insertIntoProjectsTable()
                print("Project information stored")
                DatabaseInsertion.insertIntoDeliverablesTable(Id)
                print("Project deliverables stored")
                DatabaseInsertion.insertIntoSpacesTable(Id)
                print("Spaces stored")
                DatabaseInsertion.insertIntoAttributesTable(Id)
                print("Your description has been stored")

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
