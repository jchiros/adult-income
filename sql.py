"""
Group 1 | BSCS 3-4

Carpenteros, Jasper
Gerochi, Jhaslyn
Guanlao, Claire
Nebrida, Carryl
Sandoval, Anne
Sullos, Kristine
"""

import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """CREATE TABLE IF NOT EXISTS "adult_income_dataset" (
	"id"	INTEGER NOT NULL,
	"age"	INTEGER,
	"workclass"	TEXT,
	"education"	TEXT,
	"occupation"	TEXT,
	"race"	TEXT,
	"gender"	TEXT,
	"hours_per_week"	INTEGER,
	"native_country"	TEXT,
	"income"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
        )"""
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, age, workclass, education, occupation, race, gender, hours_per_week, native_country, income):
        self.cur.execute("INSERT INTO adult_income_dataset(age, workclass, education, occupation, race, gender, hours_per_week, native_country, income) VALUES (?,?,?,?,?,?,?,?,?)",
                         (age, workclass, education, occupation, race, gender, hours_per_week, native_country, income))
        self.con.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM adult_income_dataset")
        rows = self.cur.fetchall()
        return rows

    def remove(self, id):
        self.cur.execute("DELETE FROM adult_income_dataset WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, age, workclass, education, occupation, race, gender, hours_per_week, native_country, income):
        self.cur.execute("UPDATE adult_income_dataset SET age=?, workclass=?, education=?, occupation=?, race=?, gender=?, hours_per_week=?, native_country=?, income=? WHERE id=?",
                         (age, workclass, education, occupation, race, gender, hours_per_week, native_country, income, id))
        self.con.commit()

##    def search(self, age, workclass, education, occupation, race, gender, hours_per_week, native_country, income):
##        self.cur.execute("SELECT * FROM employees WHERE age=?, workclass=?, education=?, occupation=?, race=?, gender=?, hours-per-week=?, native-country=?, income=?",
##                         (age, workclass, education, occupation, race, gender, hours_per_week, native_country, income))
##        rows = self.cur.fetchall()
##        self.con.commit()
##        return rows

if __name__ == "__main__":
   db = Database("adult_income.db")
   for row in db.fetch():
       print(row)
