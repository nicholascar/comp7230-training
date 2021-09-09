import csv
import sqlite3

# create an SQLite DB
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# create a table
conn.execute("DROP TABLE IF EXISTS dwellings;")
conn.execute(
    """
    CREATE TABLE dwellings
    (ID INT PRIMARY KEY    NOT NULL,
    NoPeople        INT    NOT NULL,
    ContainingMB    TEXT   NOT NULL,
    CensusYear      INT    NOT NULL);
    """
)
print("Table created successfully")

# check it's empty
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dwellings;")
rows = cur.fetchall()
print(f"Rows in table: {rows[0][0]}")

# read CSV data, insert it into table
with open("dwellings_data.csv") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for field in reader:
        conn.execute("INSERT INTO dwellings VALUES (?,?,?,?);", field)
print("Read CSV data into table")

# check there are 30 entries in table
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM dwellings;")
rows = cur.fetchall()
print(f"Rows in table: {rows[0][0]}")

# select only 2021 data, aggregate by containing Mesh Block
# check there are 30 entries in table
cur = conn.cursor()
cur.execute(
    """
    SELECT ContainingMB, AVG(NoPeople) 
    FROM dwellings 
    WHERE CensusYear = 2021
    GROUP BY ContainingMB
    """
)
rows = cur.fetchall()
print("Average number of people per dwelling per Mesh Block in 2021:")
for row in rows:
    print(row)

conn.close()
import os
os.unlink("test.db")
