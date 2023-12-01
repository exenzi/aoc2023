from pathlib import Path
import re
from typing import Any

testing = False

m = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def num(a: str) -> str:
    if a.isdigit():
        return str(a)
    return str(m[a])


def do(arg: str) -> Any:
    r = 0
    for l in arg.splitlines():
        digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", l)
        r += int(num(digits[0]) + num(digits[-1]))
    return r


test_input = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
expects = 281


def test():
    result = do(test_input)
    assert result == expects, f"Test result: {result}. Expected: {expects}"
    print(f"Test result: {result}. Expected: {expects}")


if not testing:
    print(do(Path("./input.txt").read_text()))
else:
    test()
