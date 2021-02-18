def s(v, p, n):
    u: list = [0 for x in range(n)]

    for i in range(n):
        u[p[i]] = v[i]

    return u


def f(n):
    v = [0, 1, 2, 3, 4, 5, 6]
    p = [2, 3, 4, 5, 6, 1, 0]

    for i in range(n):
        v = s(v, p, 7)

    return v


results: list = []
last_result: list = f(0)
last_int: int = 0

while True:
    last_int += 1

    last_result = f(last_int)

    if last_result in results:
        print("AAAA", last_result, last_int)
        break

    results.append(last_result)

    print(last_int, last_result)
