#!/usr/bin/python3

def solve(N, V):
    solution = []  # Fill this array

    for partial_len in range(0, N):
        max_start: int = N - partial_len
        minimum: int = -1

        for start in range(max_start):
            new_min: int = (min(V[start:(start + partial_len + 1)]))
            if minimum < 0 or minimum < new_min:
                minimum = new_min

        solution.append(minimum)

    return solution


if __name__ == "__main__":
    N = int(input().strip())
    V = list(map(int, input().strip().split(" ")))
    print(" ".join(map(str, solve(N, V))))
