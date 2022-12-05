from typing import List
from pathlib import Path


INPUT_PATH = Path('inputs/day-02.txt')

TEST_RAW = '''A Y
B X
C Z'''

RPS_MAPPING = {
    'A': 0,     # rock
    'B': 1,     # paper
    'C': 2,     # scissors
    'X': 0,     # rock / lose
    'Y': 1,     # paper / draw
    'Z': 2,     # scissors / win
}


def parse_raw(raw: str) -> List[List[str]]:
    '''Returns the splitted games of RPS with each player's choice'''
    return [game.split() for game in raw.split('\n')]


def round_score(choices: List[str]) -> int:
    '''
    Returns the total score of the round.

    It is the sum of the score for the shape you selected:
        1 for Rock, 2 for Paper, 3 for Scissors (+1 to RPS mapping ID)
    and the score for the outcome of the round:
        0 if you lost, 3 if the round was a draw, 6 if you won
    '''
    outcome_score = [
        [3, 6, 0],
        [0, 3, 6],
        [6, 0, 3]
    ]
    competitor, you = [RPS_MAPPING[choice] for choice in choices]
    return you + 1 + outcome_score[competitor][you]


def update_strategy(choices: List[str]) -> List[str]:
    '''
    Returns updated choice according to win strategy.
    
    X means you need to lose
    Y means you need to end the round in a draw
    Z means you need to win
    '''
    outcome_choice = [
        ['Z', 'X', 'Y'],
        ['X', 'Y', 'Z'],
        ['Y', 'Z', 'X']
    ]
    competitor, you = [RPS_MAPPING[choice] for choice in choices]
    return [choices[0], outcome_choice[competitor][you]]


assert parse_raw(TEST_RAW) == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
assert round_score(parse_raw(TEST_RAW)[0]) == 8
assert round_score(parse_raw(TEST_RAW)[1]) == 1
assert round_score(parse_raw(TEST_RAW)[2]) == 6
assert round_score(update_strategy(parse_raw(TEST_RAW)[0])) == 4
assert round_score(update_strategy(parse_raw(TEST_RAW)[1])) == 1
assert round_score(update_strategy(parse_raw(TEST_RAW)[2])) == 7


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        raw = f.read()
    games = parse_raw(raw)
    games_scores = sum([round_score(game) for game in games])
    games_scores_updated_strategy = sum([round_score(update_strategy(game)) for game in games])

    print(f'Part 1: {games_scores}')
    print(f'Part 2: {games_scores_updated_strategy}')
