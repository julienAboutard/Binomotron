import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="1234",
  database="alternants"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS students (nom VARCHAR(100),  prénom VARCHAR(100), CONSTRAINT ID PRIMARY KEY (nom, prénom))")

sql = "INSERT INTO students (nom, prénom) VALUES (%s, %s)"
val = [
  ("Aboutard", "Julien"),
  ("Ameur", "Wahid"),
  ("Bendid","Hayel"),
  ("Berthelot", "Florient"),
  ("Bockaj", "Tomislav"),
  ("Boettcher","Vincent"),
  ("Chabane", "Djamila"),
  ("Costes", "Audrey"),
  ("Lafon", "Alice"),
  ("Launay", "Marwin"),
  ("Ouarti", "Nawel"),
  ("Paris", "Dorine"),
  ("Wittman", "Christelle"),
  ]
mycursor.executemany(sql, val)

mydb.commit()