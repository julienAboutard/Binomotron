from random import shuffle


prenom = ["Julien","Nawel","Vincent","Djamila","Florian","Tom","Christelle","Wahid","Audrey","Dorine","Marwin","Alice","Hayel"]
nom = ["Aboutard","Ouarti","Boettcher","Chabane","Berthelot","Bockaj","Wittmann","Ameur","Costes","Paris","Launay","Lafon","Bendib"]

def liste_random(prenom, nom):
    liste = []
    rep=[]
    for i,j in zip(nom,prenom):
        liste.append((i,j))
    while(len(liste)>3) :
        shuffle(liste)
        rep.append((liste.pop(0), liste.pop(1)))
    return rep
liste = liste_random(prenom, nom)
print(liste)

# def extraction(liste):
#     a = liste[0]
#     return groupe
# print(liste)
# groupe = extraction(liste)
# print(groupe)