from dataclasses import dataclass
from typing import Dict, List


INPUT_PATH = Path('inputs/day-03.txt')

TEST_RAW = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


@dataclass
class Rucksack:
    first_compartment: List[str]
    second_compartment: List[str]

    @staticmethod
    def parse(items: str) -> 'Rucksack':
        num_items = len(items)
        first_compartment = [i for i in items[:num_items // 2]]
        second_compartment = [i for i in items[num_items // 2:]]
        return Rucksack(first_compartment, second_compartment)


def parse_rucksacks(raw: str) -> List[Rucksack]:
    return [Rucksack.parse(items) for items in raw.split('\n')]


def find_sum_of_error_priorities(rucksacks: List[Rucksack]) -> int:
    result = 0
    for rucksack in rucksacks:
        errors = (set(rucksack.first_compartment) & set(rucksack.second_compartment))
        priorities = {
            error: ord(error) - 96 if error.islower() else ord(error) - 38
            for error in errors
        }
        result += sum(priorities.values())
    return result


def find_sum_of_groups_badges(rucksacks: List[str]) -> int:
    result = 0
    groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
    for group in groups:
        badge = list(set(group[0]).intersection(*[set(line) for line in group[1:]]))[0]
        priority = ord(badge) - 96 if badge.islower() else ord(badge) - 38
        result += priority
    return result


assert find_sum_of_error_priorities(parse_rucksacks(TEST_RAW)) == 157
assert find_sum_of_groups_badges(TEST_RAW.split('\n')) == 70


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        raw = f.read()
    rucksacks = parse_rucksacks(raw)
    rucksacks_lines = raw.split('\n')
    
    print(f'Part 1: {find_sum_of_error_priorities(rucksacks)}')
    print(f'Part 2: {find_sum_of_groups_badges(rucksacks_lines)}')
