elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]
elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"
interogari_nume = ["Ana", "Mara", "Elena", "stop"]
absente = [1, 0, 2, 3, 0]
#Fiecare elev are o notă pe aceeași poziție.

# Partea A - Afisare si Prelucrare
#A1 Listeaza elevii cu notele lor
for elev, nota in zip(elevi, note):
    print(f"{elev} a luat nota {nota}")

#A2 Nota maxima si minima
nota_min = 10
nota_max = 0

for i in note:
    if i < nota_min :
        nota_min = i
    if i > nota_max:
        nota_max = i

for elev,nota in zip(elevi, note):
    if nota == nota_min:
        elev_min = elev
    if nota == nota_max:
        elev_max = elev

print(f"{elev_max} a obtinut cea mai mare nota: {nota_max}")
print(f"{elev_min} a obtinut cea mai mica nota: {nota_min}")

#A3 Media clasei
print(f"Media clasei {sum(note)/len(note):.2f}")

#A4 Promovati
print(f"Elevii care au luat nota mai mare sau egal cu 5 sunt:")
for i in range(len(elevi)):
    if note[i] >= 5 :
        print(elevi[i], end=", ")
print("\n")


#Partea B – Actualizari
#B5 +1 punct fiecarei note (max 10)
for i in range(len(note)):
    if note[i] < 10 :
        note[i] = note[i] + 1

#B6 Adauga elevul predefinit
elevi.append(elev_nou)
note.append(nota_elev_nou)

#B7 Sterge elevul predefinit
if elev_de_sters in elevi:
    pozitie = elevi.index(elev_de_sters)
    elevi.pop(pozitie)
    note.pop(pozitie)
else:
    print(f"{elev_de_sters} nu exista in lista")

#B8 Afișeaza din nou lista
print("Rezultate dupa actualizare:")
for i in range(len(elevi)):
    print(f"{elevi[i]} a luat nota {note[i]}")

# Partea C – Căutări si statistici
#C9 Cautari de nume cu while
i = 0
while i < len(interogari_nume):
    nume = interogari_nume[i]
    if nume == "stop":
        break
    if nume in elevi:
        poz = elevi.index(nume)
        print(f"{nume} are nota {note[poz]}.")
    else:
        print(f"{nume} nu exista in lista.")
    i = i + 1


#C10 Numar promovați / respinsi
nr_promovati = nr_respinsi = 0
for i in range(len(elevi)):
    if note[i] >= 5 :
        nr_promovati = nr_promovati + 1
    else:
        nr_respinsi = nr_respinsi + 1

print(f"{nr_promovati} persoane au promovat si {nr_respinsi} persoane au nota sub cinci.")

#C11 Media promovatilor
note_promovate = []
for n in note:
    if n >= 5:
        note_promovate.append(n)
if len(note_promovate) > 0:
    media_promovate = sum(note_promovate) / len(note_promovate)
    print(f"Media promovatilor : {media_promovate} ")
else:
    print("Nu a promovat nimeni.")


