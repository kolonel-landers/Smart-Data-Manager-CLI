students = []


#ajouter des étudiants
students.append(("Landry",10, 40, 55, 200))

#afficher avec boucle
for s in students:
   print("name":s[0])
   print("notes": s[3])


#liste imbriquée
students = [["Landry", [15, 25, 28]], ["Mylene", [5, 10 , 70]]]

#Calcul de moyenne
for s in students:
   average = sum(s[1])/len(s[1])
   print(s[0], average)
