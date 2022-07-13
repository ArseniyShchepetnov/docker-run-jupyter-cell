"""Source code manipulation."""
import inspect
import textwrap
from typing import Callable

import itertools


def drop_function_decorators(code: str) -> str:
    """Returns function code without decorators."""
    lines = code.split("\n")
    lines_iter = itertools.dropwhile(lambda x: not x.startswith('def'), lines)
    code = "\n".join(lines_iter)
    return code


def get_function_source(func: Callable, drop_decorators: bool = True):
    """Get function source code."""
    code = inspect.getsource(func)
    code = textwrap.dedent(code)

    if drop_decorators:
        code = drop_function_decorators(code)

    return code
