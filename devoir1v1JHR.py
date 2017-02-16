#coding: utf-8

#tous les médecins avant l'an 2000 feront partie de la liste 1
l1 = list(range(30000,100000,1))
#tous les médecins de 2000 à ajd font partie de la liste 2
l2 = list(range(00000,18000,1))

l3 = l1+l2 
print(l3)

# Ici, malheureusement, ça ne fonctionne pas pour les années 2000 à 2009.
# Les premiers numéros de permis de l'an 2000, par exemple, sont affichés comme étant 1, 2 ou 3, par exemple, au lieu de 00001, 00002 ou 00003.