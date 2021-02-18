def euclide(a, b):
    r = a % b

    # Siamo arrivati a fine corsa.
    if r == 0:
        return r

    # Controlliamo se il prossimo è la fine della corsa e ci fermiamo.
    next_recursion: int = euclide(b, r)
    if next_recursion == 0:
        return r

    # Andiamo avanti.
    else:
        return euclide(b, r)


print(euclide(120, 119))
