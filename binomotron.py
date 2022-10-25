from random import choices, shuffle,choice
import mariadb

mydb = mariadb.connect(
  host="localhost",
  user="user",
  password="1234",
  database="alternants",
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()

def liste_random(listdb):
    rep=[]
    while(len(listdb)>3) :
        b1=choice(listdb)
        listdb.remove(b1)
        b2=choice(listdb)
        listdb.remove(b2)
        rep.append((b1,b2))
    if len(listdb)==3 :
        rep.append((listdb[0], listdb[1], listdb[2]))
    return rep
liste = liste_random(myresult)
# for x in liste :
#     print(x)



def afficher_groupe(liste):
    for a in liste :
        if len(a)==3:
            print (a[0], ",", a[1], 'et', a[2])
        else : 
            print (a[0], "et", a[1])
        
afficher_groupe(liste)
