def required_tables(reservations):
    events = []
    for r in reservations:
        events.append([r[0], 1])
        events.append([r[1], -1])

    events.sort(key=lambda x: (x[0], x[1]))

    current_tables = 0
    max_tables = 0
    for e in events:
        current_tables += e[1]
        max_tables = max(max_tables, current_tables)

    return max_tables


reservations = [[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]]
reservations2 = [
    [1, 3],
    [2, 4],
    [3, 5],
    [4, 6],
    [5, 7],
    [6, 8],
    [7, 9],
    [8, 10],
    [9, 11],
    [10, 12],
]

print(required_tables(reservations))
print(required_tables(reservations2))
