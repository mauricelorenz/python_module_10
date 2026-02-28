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


def airball() -> int:
    return 10


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args: Any) -> int:
        return base_spell(*args) * multiplier
    return amplified


def test_condition(target: str) -> bool:
    if target == "Dragon":
        return True
    return False


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_func(*args: Any) -> Any:
        if condition(*args):
            return spell(*args)
        return "Spell fizzled"
    return conditional_func


def spell_sequence(spells: list[Callable]) -> Callable:
    def get_sequence(*args: Any) -> list[str]:
        return [item(*args) for item in spells]
    return get_sequence


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {", ".join(combined("Dragon"))}")
    print("\nTesting power amplifier...")
    mega_airball = power_amplifier(airball, 3)
    print(f"Original: {airball()}, Amplified: {mega_airball()}")
    print("\nTesting conditional caster...")
    conditional_func = conditional_caster(test_condition, fireball)
    print(f"Condition True: {conditional_func("Dragon")}")
    print(f"Condition False: {conditional_func("Witch")}")
    print("\nTesting spell sequence...")
    spells_func = spell_sequence([fireball, heal])
    print(spells_func("Dragon"))


if __name__ == "__main__":
    main()
