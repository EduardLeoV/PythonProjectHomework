#1
def suma_cifrelor(n: int):
    suma = 0
    cifre = n
    while n > 0:
        cifra = n % 10
        suma += cifra
        n = n // 10
    return str(f"Suma cifrelor {cifre} este {suma}")

#2
def cmmdc(a: int, b: int):
    divizor=0

    for i in range(1,min(a,b)+1):
        if a % i == 0 and b % i == 0 and i > divizor:
            divizor = i

    if a == b == 0:
        return str("0 nu are divizor")

    if  divizor == 0:
        return str("0 nu are divizor")

    return str(f"Cel mai mare divizor comun al lui {a} și {b} este {divizor}")

#3
def cmmmc(a: int, b: int):
    nr_mare = max(a, b)
    while True:
        if nr_mare % a == 0 and nr_mare % b == 0:
            return str(f"Cel mai mic multiplu comun a lui {a} si {b} este {nr_mare}")
        else:
            nr_mare += max(a, b)

#4
def numar_divizori(n: int):
    nr_divizor = 0
    i = n
    if n <= 0 :
        return str("Error")
    while i > 0:
        if n % i == 0:
            nr_divizor += 1
        i -= 1
    return str(f"Numărul de divizori ai lui {n} este {nr_divizor}.")

#5
def lista_prime_pana_la(n: int):
    lista_prime = []
    nr = n
    if n <= 0:
        return str("Nu e numar natural")
    while nr > 0:

        i = 1
        divizor = 0

        while not (i > nr):
            if nr % i == 0:
                divizor += 1
            i += 1
        if divizor == 2:
            lista_prime.append(nr)
        nr -= 1

    return str(f"Numere prime până la {n}: {lista_prime}")

#6
def filtreaza_pare(lista: list[int]):
    lista_pare = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pare.append(lista[i])
    return str(f"Numere pare: {lista_pare}")

#7
def produs_scalar(v1: list[float], v2: list[float]) :
    lungime = min(len(v1),len(v2)) -1
    produs = 0
    while lungime >= 0:
        produs += v1[lungime] * v2[lungime]
        lungime -= 1
    return str(f"Produsul scalar este {produs}.")

#8
def medie_ponderata(valori:list[float], ponderi:list[float]):
    if not (len(valori) == len(ponderi)):
        return str("Numerele listerol nu e egal")
    suma_ponderi = 0
    for i in range(0, len(ponderi)):
        suma_ponderi += ponderi[i]
    medie = 0
    for i in range(0, len(ponderi)):
        medie += (ponderi[i] * valori[i]) / suma_ponderi

    return str(f"Media ponderate este {medie}")

#9
def rotire_dreapta(lista: list[int], k: int) -> list[int]:
    if len(lista) == 0:
        return str("Lista este goala.")
    k = k % len(lista)
    return str(f"Lista rotita cu {k} pozitii este: {lista[-k:] + lista[:-k]}")

#10
def interclaseaza(l1: list[int], l2: list[int]) :
    i,j=0,0
    lista=[]
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            lista.append(l1[i])
            i += 1
        else:
            lista.append(l2[j])
            j += 1

        while i < len(l1):
            lista.append(l1[i])
            i += 1

        while j < len(l2):
            lista.append(l2[j])
            j += 1
    return print(f"Lista interclasate este:{lista}")

#11
def elimina_duplicate(lista: list[int]) -> str:
    i = 0
    while i < len(lista):
        j = i + 1
        while j < len(lista):
            if lista[i] == lista[j]:
                lista.pop(j)
            else:
                j += 1
        i += 1
    str(f"Fara duplicate : {lista}")

#12
def frecventa_litere(text: str) -> str:
    frecventa = []
    lista = set(text)
    for car in lista:
        if car != ' ':
            frecventa.append(f"{car} :{text.count(car)}")

    return str(frecventa)

#13
def cel_mai_frecvent_cuvant(text: str) -> str:
    cuvinte = text.split()
    if not cuvinte:
        return "Nu exista cuvinte!"

    frecvente = {}
    for c in cuvinte:
        frecvente[c] = frecvente.get(c, 0) + 1

    max_cuvant = None
    max_aparitii = 0

    for c in frecvente:
        if frecvente[c] > max_aparitii:
            max_cuvant = c
            max_aparitii = frecvente[c]

    return f"Cuvantul cel mai frecvent este '{max_cuvant}' cu {max_aparitii} aparitii."

#14
def este_isograma(text: str) -> str:
    t = text.replace(" ", "").lower()

    if len(t) == len(set(t)):
        return f"'{text}' este isogramă."
    else:
        return f"'{text}' NU este isogramă."

#15
def numere_distincte(lista: list[int]) -> str:
    if not lista:
        return "Lista este goala."

    if len(lista) == len(set(lista)):
        return "Toate numerele din lista sunt distincte."
    else:
        return "Lista contine elemente care se repeta."

#16
def timp_in_format(secunde: int) -> str:
    if secunde < 0:
        return "Eroare: numarul de secunde nu trebuie sa fie negativ."

    ore = secunde // 3600
    minute = (secunde % 3600) // 60
    sec = secunde % 60

    return str(f"{secunde} secunde inseamna {ore:02d}:{minute:02d}:{sec:02d}.")

#17
def parola_valida(parola: str) -> str:
    if len(parola) < 8:
        return "Parola este invalida: trebuie sa aiba cel putin 8 caractere."

    are_litera = any('a' <= ch.lower() <= 'z' for ch in parola)

    are_cifra = any('0' <= ch <= '9' for ch in parola)

    if not are_litera:
        return "Parola este invalida: trebuie sa contina cel putin o litera."

    if not are_cifra:
        return "Parola este invalida: trebuie să contina cel putin o cifra."

    return "Parola este valida."

#18
def in_binar(n: int) -> str:
    if n < 0:
        return "Eroare: numarul trebuie sa fie pozitiv."

    if n == 0:
        return "Reprezentarea în baza 2 a lui 0 este 0."

    binar = ""
    numar = n
    while numar > 0:
        binar = str(numar % 2) + binar
        numar = numar // 2

    return f"Reprezentarea în baza 2 a lui {n} este {binar}."

#19
def numar_unic(lista: list[int]) -> str:
    if not lista:
        return "Eroare: lista este goala."

    frecvente = {}
    for num in lista:
        if num in frecvente:
            frecvente[num] += 1
        else:
            frecvente[num] = 1

    numar_unic = None
    for num, count in frecvente.items():
        if count == 1:
            if numar_unic is not None:
                return "Eroare: lista nu respecta regula (un singur numar apare o singura data)."
            numar_unic = num

    if numar_unic is None:
        return "Eroare: lista nu respecta regula (un singur numar apare o singura data)."

    return f"Numarul unic este {numar_unic}."

#20
def sunt_anagrame(a: str, b: str) -> str:
    a1 = a.replace(" ", "").lower()
    b1 = b.replace(" ", "").lower()

    if len(a1) != len(b1):
        return f"'{a}' si '{b}' nu sunt anagrame."

    frecvente_a = {}
    for ch in a1:
        if ch in frecvente_a:
            frecvente_a[ch] += 1
        else:
            frecvente_a[ch] = 1

    for ch in b1:
        if ch not in frecvente_a:
            return f"'{a}' si '{b}' nu sunt anagrame."
        frecvente_a[ch] -= 1
        if frecvente_a[ch] < 0:
            return f"'{a}' si '{b}' nu sunt anagrame."

    return f"'{a}' si '{b}' sunt anagrame."
