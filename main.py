from subPrograms import *
import sqlite3

def createTables():
    """ Creates three  tables ;
    1. The deliverable table,
    2. The spaces table
    3. The project table
    """
    # connect to a database
    with sqlite3.connect("Gopillar.db") as db:
        cursor = db.cursor()
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

def projectsTable():
    """"""







