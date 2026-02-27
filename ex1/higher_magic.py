#!/usr/bin/env python3

from typing import Callable, Any


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args: Any) -> tuple:
        return (spell1(*args), spell2(*args))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    pass


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    pass


def spell_sequence(spells: list[Callable]) -> Callable:
    pass


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {", ".join(combined("Dragon"))}")


if __name__ == "__main__":
    main()
