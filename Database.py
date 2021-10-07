import subPrograms
import sqlite3

# connect to a database
with sqlite3.connect("Gopillar.db") as db:
    cursor = db.cursor()


def createTables():
    """ Creates three  tables ;
    1. The deliverable table,
    2. The spaces table
    3. The project table
    """
    # create a projects table
    cursor.execute("""CREATE TABLE IF NOT EXISTS projects(
    ID text PRIMARY KEY,
    Title text NOT NULL,
    Category text NOT NULL 
    )""")

    # create a deliverables table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Deliverables(
    ID text PRIMARY KEY,
    FloorPlan integer,
    DemolitionPlan integer,
    RenderViews integer,
    FurnitureList integer,
    LightingPlan integer,
    FinishesList integer,
    WiringPlan integer,
    FloorMaterials integer
    )""")
    # you do not need comma after the last column item

    # create a spaces table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Spaces(
        ID text PRIMARY KEY,
        LivingDiningKitchen integer,
        LivingDining integer,
        LivingOnly integer,
        KitchenOnly integer,
        KitchenDining integer,
        kitchenPantry integer,
        Cloakroom integer,
        LaundryRoom integer,
        Bedroom integer,
        MasterWalkInCloset integer,
        MasterSpaceCloset integer,
        MasterEnSuite integer,
        MasterSpace integer,
        HomeOffice integer,
        Store integer,
        Garage integer,
        Terrace integer )""")
    # you do not need comma after the last column item

    db.commit()
    db.close()


def insertIntoProjectsTable():
    """Insert items into the Gopillar database, projects table"""
    link, Id = subPrograms.projectID()
    projectName = subPrograms.projectName()
    projectCategory = subPrograms.projectCategory()

    cursor.execute(""" INSERT INTO projects(ID,Title,Category) 
    VALUES(?,?,?) """, (Id, projectName, projectCategory))

    # commit in advance to know if ID has been taken before
    db.commit()
    return Id


def insertIntoDeliverablesTable(Id):
    """Insert items into the Gopillar database, deliverables table.
    This portion is automated as we had already determined the outcomes"""
    valueFP, valueDRP, valueRV, valueFUL, valueLP, valueFIL, valueWP, valueFML = (0, 0, 0, 0, 0, 0, 0, 0)

    deliverablesList = subPrograms.projectDeliverables()

    for x in deliverablesList:
        if x == "FP":
            valueFP = valueFP + 1
        elif x == "DRP":
            valueDRP = valueDRP + 1
        elif x == "RV":
            valueRV = valueRV + 1
        elif x == "FUL":
            valueFUL = valueFUL + 1
        elif x == "LP":
            valueLP = valueLP + 1
        elif x == "FIL":
            valueFIL = valueFIL + 1
        elif x == "WP":
            valueWP = valueWP + 1
        elif x == "FML":
            valueFML = valueFML + 1
        else:
            print("Not within the Database")

    cursor.execute(""" INSERT INTO Deliverables
    (ID,FloorPlan,DemolitionPlan,
    RenderViews,FurnitureList,LightingPlan,
    FinishesList,WiringPlan,FloorMaterials) 
    VALUES(?,?,?,?,?,?,?,?,?) """, (Id, valueFP, valueDRP, valueRV, valueFUL, valueLP, valueFIL, valueWP, valueFML))
    db.commit()


def insertIntoSpacesTable(Id):
    """Insert items into the Gopillar database, Spaces table.
    This portion is automated as we had already determined the outcomes"""

    # Below are values we are going to store in each spaces table column
    # they are abbreviated as
    # v-{The first initials of the column name}
    vldk, vld, vlo, vko, vkd, vkp, vcr, vlr, vbr, vmwic, vmsc, vmes, vms, vho, vse, vge, vte = (0, 0, 0, 0, 0, 0, 0, 0,
                                                                                                0, 0, 0, 0, 0, 0, 0, 0, 0)
    spacesList, noOfBedrooms = subPrograms.projectSpaces()
    vbr = noOfBedrooms

    for x in spacesList:
        if x == "Living-Dining-Kitchen":
            vldk = 1
        elif x == "Living-Dining":
            vld = 1
        elif x == "Living-Only":
            vlo = 1
        elif x == "Kitchen-Only":
            vko = 1
        elif x == "Kitchen-Dining":
            vkd = 1
        elif x == "kitchen-Pantry":
            vkp = 1
        elif x == "Cloakroom":
            vcr = 1
        elif x == "Laundry-room":
            vlr = 1
        elif x == "Bedroom":
            vbr = vbr
        elif x == "Kitchen-Only":
            vko = 1
        elif x == "Master-walk-in-closet":
            vmwic = 1
        elif x == "Master-space-closet":
            vmsc = 1
        elif x == "Master-en-suite":
            vmes = 1
        elif x == "Master-space":
            vms = 1
        elif x == "Home-office":
            vho = 1
        elif x == "Store":
            vse = 1
        elif x == "Garage":
            vge = 1
        elif x == "Terrace":
            vge = 1
        else:
            print("Not within the Database")

    cursor.execute(""" INSERT INTO Spaces
    (ID,
    LivingDiningKitchen,
    LivingDining,
    LivingOnly,
    KitchenOnly,
    KitchenDining,
    kitchenPantry,
    Cloakroom,
    LaundryRoom,
    Bedroom,
    MasterWalkInCloset,
    MasterSpaceCloset,
    MasterEnSuite,
    MasterSpace,
    HomeOffice,
    Store,
    Garage,
    Terrace ) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) """, (Id, vldk, vld, vlo, vko, vkd, vkp, vcr, vlr, vbr, vmwic, vmsc,
                                                      vmes, vms, vho, vse, vge, vte))

    db.commit()

