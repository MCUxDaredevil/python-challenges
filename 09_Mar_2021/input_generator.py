import random

ROWS = 4  # Should always be 4
COLUMNS = 10  # Can be any number, should be bigger to increase the chance of generating all formations at least once.


def generate_input() -> list[list[int]]:
    data = []
    for x in range(ROWS):
        if x == 0:
            row = random.choices([0, 1], k=COLUMNS)
        elif x == 1:
            row = [random.choice([0, 1]) if data[0][_] == 1 else 0 for _ in range(COLUMNS)]
        elif x == 2:
            row = [random.choice([0, 1]) if data[0][_] == 1 else 1 for _ in range(COLUMNS)]
        elif x == 3:
            row = [random.choice([0, 1]) if data[2][_] == 1 else 0 for _ in range(COLUMNS)]

            data.insert(2, row)
            continue

        data.append(row)

    return data
