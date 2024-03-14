# Weekly Challenge 1

containers = {}
cache = {}
singulars = {}


def get_containers(unit: str, key: str, value: list) -> int:
    total = 0
    for container in value:
        count, color = container.split('.')
        if color == unit:
            total += int(count)
        elif color in singulars:
            continue
        elif color in cache:
            total += int(count) * cache[color]
        else:
            total += (int(count) * get_containers(unit, color, containers[color]))

    if total > 0:
        cache[key] = total

    return total


def read_rules(filename: str) -> None:
    with open(filename, 'r') as file:
        input_text = file.read()

    containers_input = input_text.split('\n')

    for container in containers_input:
        color, contains = container.split(':')
        contains = contains.split('|')

        if contains[0].isnumeric():
            singulars[color] = int(contains[0])
        else:
            containers[color] = contains


def main(unit: str, target: str, amount: int, rulebook: str) -> int:
    read_rules(rulebook)

    if target in cache:
        return -1 if target != unit else cache[target] * amount

    return amount * get_containers(unit, target, containers[target]) * (singulars[unit])


if __name__ == '__main__':
    print(main("cloudy-blue", "light-greenish-blue", 6, "input.txt"))
