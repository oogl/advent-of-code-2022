from collections import defaultdict
from pathlib import Path


INPUT_PATH = Path('inputs/day-06.txt')


def get_start_of(input_type: str, input: str) -> int:
    ''''''
    if input_type == 'packet':
        length = 4
    elif input_type == 'message':
        length = 14
    else:
        raise ValueError(f'There is no such `input_type`: {input_type}')

    assert len(input) >= length + 1, f'there is no {input_type} due to the length of the input'

    if len(set(input[:length])) == length:
        return length + 1

    chars_counter = defaultdict(int)
    for char in input[:length]:
        chars_counter[char] += 1

    for i, cur_char in enumerate(input[length:]):
        chars_counter[input[i]] -= 1
        chars_counter[cur_char] += 1
        if set(chars_counter.values()) <= {0, 1}:
            return i + length + 1


assert get_start_of('packet', 'bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
assert get_start_of('packet', 'nppdvjthqldpwncqszvftbrmjlhg') == 6
assert get_start_of('packet', 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
assert get_start_of('packet', 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
assert get_start_of('message', 'mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19
assert get_start_of('message', 'bvwbjplbgvbhsrlpgdmjqwftvncz') == 23
assert get_start_of('message', 'nppdvjthqldpwncqszvftbrmjlhg') == 23
assert get_start_of('message', 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 29
assert get_start_of('message', 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26


if __name__ == '__main__':
    with open(INPUT_PATH) as f:
        signal = f.read()
    
    print(f'Part 1: {get_start_of("packet", signal)}')
    print(f'Part 2: {get_start_of("message", signal)}')
