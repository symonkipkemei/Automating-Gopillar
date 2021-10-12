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



def projectAttributesTable():
    """Creates the Attributes Table"""

    # create a projects table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Attributes(
    ID text PRIMARY KEY,
    Attributes text)""")


projectAttributesTable()