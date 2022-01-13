# Author CCG 1/13/22

last_initials = ["B", "D", "H", "E", "G", "G", "H", "R", "M", "L", "I", "I", "N", "N", "O", "P", "P", "X", "T", "S", "S", "P"]

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin", "Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
initial_numb = 0

for row_numb, row in enumerate(rows):
    for name_numb, name in enumerate(row):
        full_name = rows[row_numb][name_numb]
        full_name += (" " + last_initials[initial_numb] + ".")
        rows[row_numb][name_numb] = full_name
        initial_numb +=1

print(rows)
