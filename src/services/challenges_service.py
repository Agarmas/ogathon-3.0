from itertools import permutations


def virus_propagation(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def count_end89(n: int) -> int:
    sq = [i * i for i in range(10)]
    ends = {}

    def get_sequence_end(x: int) -> int:
        if x in ends:
            return ends[x]
        original = x
        while x != 1 and x != 89:
            x = sum(sq[int(d)] for d in str(x))
        ends[original] = x
        return x

    count = 0
    for i in range(1, n + 1):
        if get_sequence_end(i) == 89:
            count += 1

    return count


def recycling(matrix: list[list[int]]) -> int:
    total_items = [sum(row) for row in matrix]

    min_moves = float('inf')

    for perm in permutations(range(3)):
        moves = 0
        for i in range(3):
            moves += total_items[i] - matrix[i][perm [i]]
        min_moves = min(min_moves, moves)

    return min_moves
