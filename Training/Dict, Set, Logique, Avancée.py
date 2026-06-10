students = [
    {"name": "Landry", "notes":[10, 15, 18]}, 
]

#ajouter un étudiant
students.append({"name":"Kevin","notes":[10, 8, 12]})

#recherche boucle avancée
def find_student(name):
    for s in students:
        if s["name"] == name:
            return s
        

#ensemble (éviter doublons)
names = set()

if name not in names:
    names.add(name)


#supprimer un étudiant
for s in students:
    if s["Name"] == name:
        students.removes(s)
        break
