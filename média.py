notas = [5.5, 8.0, 9.0, 7.5]
media = 7.0
Total_notas = 0
for nota in notas:
  total_notas += nota
if total_notas/len(notas) >= media:
  print("Aprovado")
else:
  print("Reprovado")

nota1 = 5.5
nota2 = 8.0
nota3 = 9.0
nota4 = 7.5

media = 7.0

total_notas = nota1 + nota2 + nota3 + nota4

if total_notas/4 >= media:
  print("Aprovado")
else:
  print("Reprovado")
