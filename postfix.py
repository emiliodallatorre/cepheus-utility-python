#!/usr/bin/python3

def solve(N, V):
    solution: int = 0

    working_queue: list = V
    stack: list = []

    for element in working_queue:
        if element == "-":
            new_value = stack[-2] - stack[-1]
            stack.pop()
            stack.pop()
            stack.append(new_value)
        else:
            if element == "+":
                new_value = stack[-2] + stack[-1]
                stack.pop()
                stack.pop()
                stack.append(new_value)
            else:
                if element == "*":
                    new_value = stack[-2] * stack[-1]
                    stack.pop()
                    stack.pop()
                    stack.append(new_value)
                else:
                    stack.append(int(element))

    solution = stack[0]
    return solution


if __name__ == "__main__":
    N = int(input())
    V = input().strip().split(" ")
    assert (len(V) == N)
    print(solve(N, V))
