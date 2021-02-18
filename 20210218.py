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


lista: list = [0, 2, 4, 6, 9]
print(ricerca_binaria_non_ricorsiva(lista, 2))
