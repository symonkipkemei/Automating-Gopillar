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
        LivingOpen integer,
        LivingDining integer,
        LivingOnly integer,
        Kitchen integer,
        Pantry integer,
        Cloak  integer,
        SingleRoom integer,
        Bedroom integer,
        MasterWalkIn integer,
        MasterOpenCloset integer,
        Garage integer,
        Terrace integer       
        )""")
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
    return Id


def insertIntoDeliverablesTable(Id):
    """Insert items into the Gopillar database, deliverables table.
    This portion is automated as we had already determined the outcomes"""

    deliverablesList = subPrograms.projectDeliverables()

    if "FP" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,FloorPlan) 
            VALUES(?,?) """, (Id, 1))

    elif "DRP" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,DemolitionPlan) 
            VALUES(?,?) """, (Id, 1))

    elif "RV" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,RenderViews) 
            VALUES(?,?) """, (Id, 1))

    elif "FUL" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,FurnitureList) 
            VALUES(?,?) """, (Id, 1))

    elif "LP" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,LightingPlan) 
            VALUES(?,?) """, (Id, 1))

    elif "FIL" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,FinishesList) 
            VALUES(?,?) """, (Id, 1))

    elif "WP" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,WiringPlan) 
            VALUES(?,?) """, (Id, 1))

    elif "FML" in deliverablesList:
        cursor.execute(""" INSERT INTO Deliverables(ID,FloorMaterials) 
            VALUES(?,?) """, (Id, 1))

    db.commit()
    db.close()
