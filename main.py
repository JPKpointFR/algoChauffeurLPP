# Trouver la valeur la plus petite

nom_chauffeur = ["Patrick", "paul", "mark",
                 "jean", "pierre", "marie", "maxime"]
distance_chauffeur_km = [1.5, 2.2, 0.4, 0.9, 7.1, 1.1, 0.6]

noms_distances = [("Patrick", 1.5), ("paul", 2.2), ("mark", 0.4)]


# index_min
# V1
"""
index_min = 0
distance_min = distance_chauffeur_km[0]
for i in range(len(distance_chauffeur_km)):
    distance = distance_chauffeur_km[i]
    if distance < distance_min:
        distance_min = distance
        index_min = i


print(f'Distance minimale: {distance_min} km')
print(f'index de la distance minimale: {index_min}')
print(f"Nom du chauffeur {nom_chauffeur[index_min]}")
"""

# distance_chauffeur_km.sort()
# print(distance_chauffeur_km[0])
# print(distance_chauffeur_km)


"""# V2
nom_distance_min = noms_distances[0]

for noms_distances in noms_distances:
    if noms_distances[1] < nom_distance_min[1]:
        noms_distances_min = noms_distances

print("Distance minimale:",
      nom_distance_min[1], "nom du chauffeur", nom_distance_min[0])"""
