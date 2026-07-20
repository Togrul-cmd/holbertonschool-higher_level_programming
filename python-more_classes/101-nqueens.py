#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    column = [0] * N
    diag_size = 2 * N - 1
    diag_1 = [0] * diag_size
    diag_2 = [0] * diag_size
    solns = []

    def solve(y=0):
        if y == N:
            print(solns)
            return

        for i in range(N):
            if column[i] or diag_1[i + y] or diag_2[i - y + N - 1]:
                continue
            column[i] = diag_1[i + y] = diag_2[i - y + N - 1] = 1
            solns.append([y, i])
            solve(y + 1)
            solns.pop()
            column[i] = diag_1[i + y] = diag_2[i - y + N - 1] = 0
    solve()


if __name__ == "__main__":
    main()
