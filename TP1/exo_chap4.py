# Ex 4.10.1
semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

# 1)
print(f"Jour semaine : {semaine[:5]}")
print(f"Jour week-end : {semaine[5:]}")

# 2)
print(f"Jour semaine : {semaine[-7:-1]}")
print(f"Jour week-end : {semaine[-2:]}")

# 3)
print(semaine[-1])
print(semaine[6])

# 4)
print(semaine[::-1])

# Ex 4.10.2
hiver = ["Décembre", "Janvier", "Février"]
printemps = ["Mars", "Avril", "Mai"]
ete = ["Juin", "Juillet", "Aout"]
automne = ["Septembre", "Octobre", "Novenmbre"]

saisons = [hiver, printemps, ete, automne]

print(saisons[2])
print(saisons[1][0])
print(saisons[1:2])
print(saisons[:][1])

# Ex 4.10.3
print(list(range(9, 91, 9)))

# Ex 4.10.4
print(len(list(range(2, 10_001, 2))))