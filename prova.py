def ordinamento_dizionari(lista, n):
    values: dict = {}

    for i in lista:
        key: str = i[0]
        value: float = float(i[1])

        if key in values:
            values[key] += value
        else:
            values[key] = value

    return sorted(values, key=lambda k: values[k], reverse=True)[0:n]


print(ordinamento_dizionari([["a", 1], ["b", 2], ["c", 3], ["a", 1]], 2))
