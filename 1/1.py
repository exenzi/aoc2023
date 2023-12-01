from pathlib import Path
import re
from typing import Any


testing = False


def do(arg: str) -> Any:
    r = 0
    for l in arg.splitlines():
        digits = re.findall(r"\d", l)
        r += int(digits[0] + digits[-1])
    return r


test_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
expects = 142


def test():
    result = do(test_input)
    assert result == expects, f"Test result: {result}. Expected: {expects}"
    print(f"Test result: {result}. Expected: {expects}")


if not testing:
    print(do(Path("./input.txt").read_text()))
else:
    test()
