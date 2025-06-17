import sqlite3
drop_table="""
DROP TABLE Roster
"""
create_table="""
CREATE TABLE Roster(
Name TEXT,
Species TEXT,
Age INT
);
"""
insert_values="""
INSERT INTO Roster VALUES
('Benjamin Sisko','Human',40),
('Jadzia Dax','Trill',300),
('Kira Nerys','Bajoran',29)
;"""
update_values="""
UPDATE Roster SET Name='Ezri Dax' WHERE Name='Jadzia Dax'
"""
display_table="""
Select Name,Age FROM Roster WHERE Species='Bajoran'
"""
with sqlite3.connect('new_database.db') as connection:
    cursor=connection.cursor()
    try:
        cursor.execute(drop_table)
    except:
        pass
    cursor.execute(create_table)
    cursor.execute(insert_values)
    cursor.execute(update_values)
    cursor.execute(display_table)



with sqlite3.connect('new_database.db') as conn:
    cursor=conn.cursor()
    query="SELECT * FROM Roster"
    results=cursor.execute(query)
    rows=results.fetchall()
print(rows);



