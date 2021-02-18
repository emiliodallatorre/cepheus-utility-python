# [fine] è la lunghezza della lista per comodità.
def ricerca_binaria(oggetto: list, obiettivo, inizio: int, fine: int):
    mid: int = (fine + inizio) // 2

    # L'elemento non è nella lista.
    if fine == inizio:
        return None

    # L'elemento è all'indice [mid].
    if oggetto[mid] == obiettivo:
        return mid

    # L'elemento è a destra o a sinistra di [mid].
    if obiettivo < oggetto[mid]:
        return ricerca_binaria(oggetto, obiettivo, inizio, mid)
    elif obiettivo > oggetto[mid]:
        # [mid + 1] è sempre <= fine.
        return ricerca_binaria(oggetto, obiettivo, mid + 1, fine)


def ricerca_binaria_non_ricorsiva(oggetto: list, obiettivo):
    inizio: int = 0
    fine: int = len(oggetto)

    while True:
        mid: int = (fine + inizio) // 2

        # L'elemento non è nella lista.
        if fine == inizio:
            return None

        # L'elemento è all'indice [mid].
        if oggetto[mid] == obiettivo:
            return mid

        # L'elemento è a destra o a sinistra di [mid].
        if obiettivo < oggetto[mid]:
            fine = mid
        elif obiettivo > oggetto[mid]:
            # [mid + 1] è sempre <= fine.
            inizio = mid + 1


# Risolve il problema della torre di Hanoi
def hanoi(source: list, aux, dest, n):
    if n == 0:
        return

    hanoi(source, dest, aux, n - 1)
    disk = source.pop()
    print("Sposto %s." % (disk))
    dest.append(disk)
    hanoi(aux, source, dest, n - 1)


h = [4, 3, 2, 1]
d = []

hanoi(h, [], d, len(h))
