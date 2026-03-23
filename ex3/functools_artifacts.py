#!/usr/bin/env python3

from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    operation_map = {"add": add, "multiply": mul, "max": max, "min": min}
    if operation not in operation_map:
        raise ValueError("Operation not supported")
    return reduce(operation_map[operation], spells)


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Hit {target} with {power} power {element}"


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {"fire_enchant": partial(base_enchantment, 50, "Fire"),
            "ice_enchant": partial(base_enchantment, 50, "Ice"),
            "lightning_enchant": partial(base_enchantment, 50, "Lightning")}


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def dispatch_func(arg: Any) -> str:
        return "Invalid argument type"

    @dispatch_func.register(int)
    def int_dispatch(arg: int) -> str:
        return f"Making {arg} damage"

    @dispatch_func.register(str)
    def str_dispatch(arg: str) -> str:
        return f"Enchanting item with {arg}"

    @dispatch_func.register(list)
    def list_dispatch(arg: list) -> str:
        result_list = []
        for spell in arg:
            result_list.append(f"Cast spell: {spell}")
        return ", ".join(result_list)
    return dispatch_func


def main() -> None:
    print("\nTesting spell reducer...")
    spell_powers = [11, 16, 28, 31, 46, 48]
    operations = ["add", "multiply", "max", "min"]
    print(f"Sum: {spell_reducer(spell_powers, operations[0])}")
    print(f"Product: {spell_reducer(spell_powers, operations[1])}")
    print(f"Max: {spell_reducer(spell_powers, operations[2])}")
    print(f"Min: {spell_reducer(spell_powers, operations[3])}")
    print("\nTesting partial enchanter...")
    enchantments = partial_enchanter(base_enchantment)
    for enchantment in enchantments:
        print(enchantments[enchantment]("Dragon"))
    print("\nTesting memoized fibonacci...")
    fibonacci_tests = [16, 8, 15]
    for nbr in fibonacci_tests:
        print(f"Fib({nbr}): {memoized_fibonacci(nbr)}")
    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(f"int: {spell(50)}")
    print(f"str: {spell('Fire')}")
    print(f"list: {spell(['Fire', 'Water', 'Air'])}")
    print(f"dict: {spell({'fail': 1})}")


if __name__ == "__main__":
    main()
