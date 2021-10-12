import subPrograms
import sqlite3

# connect to a database
with sqlite3.connect("Gopillar.db") as db:
    cursor = db.cursor()


# ADDING THE COLUMNS BELOW TO THE EXISTING Deliverables TABLE IN THE GOPILLAR DATABASE

# COLOR SCHEME, LIGHT SCHEME AND CEILING PLAN

def tables():
    """Adding the following columns in the deliverables table"""
    cursor.execute(""" ALTER TABLE Deliverables ADD ColorScheme integer """)
    cursor.execute(""" ALTER TABLE Deliverables ADD LightScheme integer """)
    cursor.execute(""" ALTER TABLE Deliverables ADD CeilingPlan integer """)

tables()

