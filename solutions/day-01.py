from pathlib import Path
from typing import List


def parse_raw(raw: str) -> List[List[int]]:
    '''Converts raw string into the list of elf's calories'''
    return [[int(calories) for calories in elf.split('\n')] for elf in raw.split('\n\n')]


def calories_per_elf(elfs_calories: List[List[int]]) -> List[int]:
    '''Returns the list of sums of calories per elf'''
    return [sum(calories) for calories in elfs_calories]


INPUT_PATH = Path('inputs/day-01.txt')


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        raw = f.read()
    
    max_calories_per_elf = max(calories_per_elf(parse_raw(raw)))
    calories_of_top_three_elfs = sum(sorted(calories_per_elf(parse_raw(raw)), reverse=True)[:3])

    print(f'Part 1: {max_calories_per_elf}')
    print(f'Part 2: {calories_of_top_three_elfs}')
