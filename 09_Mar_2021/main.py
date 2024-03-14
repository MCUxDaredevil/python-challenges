from input_generator import generate_input


def main(data: list[list[int]]) -> None:
    length = len(data[0])
    formations = []

    for i in range(length):
        if data[0][i] == 0:
            formations.append("G")
        elif data[3][i] == 0:
            formations.append("C")
        elif data[1][i] == 0 or data[2][i] == 0:
            formations.append("B")
        else:
            formations.append("P")

    print(" ".join(formations))


if __name__ == '__main__':
    main(generate_input())
