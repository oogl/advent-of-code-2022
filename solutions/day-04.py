from typing import List, Tuple


INPUT_PATH = Path('inputs/day-04.txt')

TEST_RAW = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''


Pair = List[List[int]]


def parse_raw(raw: str) -> List[Pair]:
    result = []
    for pair in raw.split('\n'):
        pair_sections = []
        for sections in pair.split(','):
            nums = sections.split('-')
            pair_sections.append([int(nums[0]), int(nums[1])])
        result.append(pair_sections)
    return result


def is_fully_included(pair: Pair) -> bool:
    if ((pair[0][0] >= pair[1][0]) & (pair[0][1] <= pair[1][1])):
        return True
    elif ((pair[1][0] >= pair[0][0]) & (pair[1][1] <= pair[0][1])):
        return True
    return False


def has_overlap(pair: Pair) -> bool:
    if (pair[0][1] < pair[1][0]):
        return False
    elif (pair[0][0] > pair[1][1]):
        return False
    return True


assert [is_fully_included(pair) for pair in parse_raw(TEST_RAW)] == [0, 0, 0, 1, 1, 0]
assert [has_overlap(pair) for pair in parse_raw(TEST_RAW)] == [0, 0, 1, 1, 1, 1]


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        raw = f.read()

    pairs = parse_raw(raw)
    print(f'Part 1: {sum(is_fully_included(pair) for pair in pairs)}')
    print(f'Part 2: {sum(has_overlap(pair) for pair in pairs)}')
