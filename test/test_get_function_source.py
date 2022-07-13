"""Test getting function source sode."""
from typing import Callable

from src.python_source import get_function_source


def test_get_ordinary_function():
    """Test function source code extraction."""
    def func(a: int = 100) -> int:
        if a > 100:
            result = 0
        else:
            result = 1
        return result

    reference_code = (
        "def func(a: int = 100) -> int:\n"
        "    if a > 100:\n"
        "        result = 0\n"
        "    else:\n"
        "        result = 1\n"
        "    return result\n"
    )

    code = get_function_source(func)
    assert code == reference_code


def test_get_function_code_no_decorators():
    """Test function source code extraction."""
    def decorator(arg: Callable) -> Callable:
        print(arg.__name__)
        return arg

    @decorator
    def func(a: int = 100) -> int:
        if a > 100:
            result = 0
        else:
            result = 1
        return result

    reference_code = (
        "def func(a: int = 100) -> int:\n"
        "    if a > 100:\n"
        "        result = 0\n"
        "    else:\n"
        "        result = 1\n"
        "    return result\n"
    )

    code = get_function_source(func, drop_decorators=True)
    assert code == reference_code
