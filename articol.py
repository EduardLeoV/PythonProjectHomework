text = ("Apelul venit prin 112 ne-a anuntat "
        "despre faptul ca un barbat de 62 ani aflat la cules ciuperci a suferit un "
        "traumatism la membrul inferior si nu se mai poate deplasa, fiind intr-o zona "
        "din care poate fi extras doar cu echipamente speciale.")

part1 = text[:len(text)//2].upper()
if part1[0] == " ":
    part1[0] = ""
if part1[:-1] == " ":
    part1[:-1] = ""


part2 = text[-1:len(text)//2-1:-1]
for c in ",.?!" :
    part2 = part2.replace(c, "")

part2=part2[0].upper() + part2[1:]

print(part1+part2)
