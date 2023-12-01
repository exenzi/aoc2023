from pathlib import Path
import re
from typing import Any

testing = True

def do(arg: str) -> Any:
    r = 0
    for l in arg.splitlines():
        
    return r


test_input = """"""
expects = 0

def test():
    result = do(test_input)
    assert result == expects, f"Test result: {result}. Expected: {expects}"
    print(f"Test result: {result}. Expected: {expects}")


if not testing:
    print(do(Path('./input.txt').read_text()))
else:
    test()
