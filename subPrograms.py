"""This is automating Gopillar with python.The main task is to analyze existing
design data and look which option is close to or similar to a new clients requirements then duplicate
it with little or no adjustment.The plan is to steal it all."""




def projectID():
    """The unique identifier of each project.
    Used to retrieve the project information from Gopillar website """
    projectID = int(input("Insert the project 1D: "))
    return projectID

def projectName():
    """Records the name of the project"""
    projectName = input("Insert project name: ")
    return projectName

def projectCategory():
    """The type of project based on size and the number of rooms"""
    print("project Category\n"
          "(1)Apartment-Small\n"
          "(2)Single room-Small\n"
          "(3)Single room-Medium\n"
          "(4)Single room-Large\n"
          "(5)Living Sleeping area-Small\n"
          "(6)Living Sleeping area-Medium\n")

    userInput = int(input("Option: "))

    if userInput == 1:
        return "Apartment-Small"
    elif userInput == 2:
        return "SingleRoom-Small"
    elif userInput == 3:
        return "SingleRoom-Medium"
    elif userInput == 4:
        return "SingleRoom-Large"
    elif userInput == 5:
        return "LivingSleepingArea-Small"
    elif userInput == 6:
        return "LivingSleepingArea-Medium"
    else:
        print("wrong input")


def projectDeliverables():
    """The expected outcomes set by the client of the expected submissions and their type"""
    #storage for values selected by user
    deliverableList = []

    #recording one by one until all the parameters are captured
    correct  = False
    while correct == False:
        print("\nChoose Avalable project Deliverables \n"
              "(1)Floor Plan (FP)\n"
              "(2)Demolition and reconstruction plans (DRP)\n"
              "(3)Render views (RV)\n"
              "(4)Furniture lists ( FUL)\n"
              "(5)Lighting plan (LP)\n"
              "(6)Finishes list (FIL)\n"
              "(7)Wiring plan (WP)\n"
              "(8)Flooring materials lists(FML)\n"
              "(9)END\n")

        # Use of known keys to make refrence to the long and dynamic values
        # Makes it shorter for the user to type

        deliverableDict = {1: "FP", 2: "DRP", 3: "RV", 4: "FUL", 5: "LP", 6: "FIL", 7: "WP", 8: "FML"}

        # The selected key
        userInput = int(input("Enter one of the options above: "))

        # Within the specified range of keys
        if userInput <= 8  and userInput >= 1:
            #checking if the value in the dictionary is already stored in the list
            # if not add,otherwise warn of repetition
            if deliverableDict[userInput] not in deliverableList:
                deliverableList.append(deliverableDict[userInput])
                print(f"Added {deliverableDict[userInput]}")
                print(deliverableList)
                correct = False
            else:print("Already added, try another one:")

        # The gunshot
        # This ends the continuous loop

        elif userInput == 9:
            correct = True

        # Wrong inputs are not tolerated
        else:
            print("wrong input,Try again")

    return deliverableList


def projectSpaces():
    """This is where the cleaning of data begins.
    Sorting the best submission and document the spaces designed"""
    # storage for spaces selected by user,collected through observation
    spacesList = []

    # recording spaces one by one until all  are captured
    correct = False
    while correct == False:
        print("\nChoose Avalable project Spaces \n"
              "1.Living-Dining-Kitchen(open)\n"
              "2.Living-Dining\n"
              "3.Living only\n"
              "4.Kitchen\n"
              "5.Pantry\n"
              "6.Cloak\n"
              "7.Single\n"
              "8.bedroom 1\n"
              "9.bedroom 2\n"
              "10.Master-walk-in\n"
              "11.Master-open-closet\n"
              "12.Store\n"
              "13.Garage\n"
              "14.Terrace\n"
              "15.END\n")

        # Use of known keys to make reference to the long and dynamic spaces
        # The goal is to make it easier for the user to type.

        spacesDict = {1: "Living-Dining-Kitchen(open)",
                      2: "Living-Dining",
                      3: "Living only",
                      4: "Kitchen",
                      5: "Pantry",
                      6: "Cloak",
                      7: "Singleroom",
                      8: "bedroom 1",
                      9: "bedroom 2",
                      10: "Master-walk-in",
                      11: "Master-open-closet",
                      12: "Store",
                      13: "Garage",
                      14: "Terrace",}

        # The selected key
        userInput = int(input("Enter one of the options above: "))

        # Within the specified range of keys
        if userInput <= 14 and userInput >= 1:
            # checking if the value in the space dictionary is already stored in the list
            # if not add,otherwise warn of repetition
            if spacesDict[userInput] not in spacesList:
                spacesList.append(spacesDict[userInput])
                print(f"Added {spacesDict[userInput]}")
                print(spacesList)
                correct = False
            else:
                print("Already added, try another one:")

        # The gunshot
        # This ends the continuous loop

        elif userInput == 15:
            correct = True

        # Wrong inputs are not tolerated
        else:
            print("wrong input,Try again")

    return spacesList


answer = projectSpaces()
print(answer)