#!/usr/bin/env python3

from typing import Callable
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    operation_map = {"add": add, "multiply": mul, "max": max, "min": min}
    if operation not in operation_map:
        raise ValueError("Operation not supported")
    return reduce(operation_map[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    pass


def memoized_fibonacci(n: int) -> int:
    pass


def spell_dispatcher() -> Callable:
    pass


def main() -> None:
    print("\nTesting spell reducer...")
    spell_powers = [11, 16, 28, 31, 46, 48]
    operations = ["add", "multiply", "max", "min"]
    print(f"Sum: {spell_reducer(spell_powers, operations[0])}")
    print(f"Product: {spell_reducer(spell_powers, operations[1])}")
    print(f"Max: {spell_reducer(spell_powers, operations[2])}")
    print(f"Min: {spell_reducer(spell_powers, operations[3])}")
    fibonacci_tests = [16, 8, 15]


if __name__ == "__main__":
    main()
