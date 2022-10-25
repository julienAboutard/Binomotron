from random import shuffle
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="1234",
  database="alternants"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()

# print(myresult)



def liste_random(listdb):
    # liste = []
    rep=[]
    # for i in listdb:
    #     liste.append(i)
    while(len(listdb)>3) :
        shuffle(listdb)
        rep.append((listdb.pop(0), listdb.pop(1)))
    if len(listdb)==3 :
        rep.append((listdb[0], listdb[1], listdb[2]))
    return rep
liste = liste_random(myresult)
for x in liste :
    print(x)

# def extraction(liste):
#     a = liste[0]
#     return groupe
# print(liste)
# groupe = extraction(liste)
# print(groupe)