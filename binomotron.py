from random import choice
import mysql.connector


# Connector pour la version mariadb sous Ubuntu 22.04
#import mariadb

# mydb = mariadb.connect(
#   host="localhost",
#   user="user",
#   password="1234",
#   database="alternants",
# )

#Connector pour accéder à la base de données alternants
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="1234",
  database="alternants"
)

mycursor = mydb.cursor()

#On récupère la liste des noms et prénoms de table students
mycursor.execute("SELECT * FROM students")
myresult = mycursor.fetchall()

#Fonction qui tire deux fois un élément au hasard d'une liste et le supprime et rends la liste sans les éléments choisient et un tuple des 2 éléments chosie
def take_two(listdb) :
    b1=choice(listdb)
    listdb.remove(b1)
    b2=choice(listdb)
    listdb.remove(b2)
    return listdb, (b1, b2)

#Fonction qui créer la liste randoom de binômes et si la liste initiale est impair ajoute un trinôme à la fin  
def liste_random(listdb):
    rep=[]
    while(len(listdb)>3) :
        listdb, tup=take_two(listdb)
        rep.append(tup)
    if len(listdb)==3 :
        rep.append((listdb[0], listdb[1], listdb[2]))
    
    return rep

#fonction pour afficher la liste des groupes
def afficher_groupe(liste):
    for a in liste :
        if len(a)==3:
            print (f'{a[0][0]} {a[0][1]}, {a[1][0]} {a[1][1]} et {a[2][0]} {a[2][1]}')
        else : 
            print (f'{a[0][0]} {a[0][1]} et {a[1][0]} {a[1][1]}')
        
liste = liste_random(myresult)
afficher_groupe(liste)
