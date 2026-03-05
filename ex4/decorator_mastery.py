#!/usr/bin/env python3

from typing import Callable, Any
from functools import wraps
from time import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time()
        result = func(*args, **kwargs)
        print(f"Spell completed in {time() - start_time:.6f} seconds")
        return result
    return wrapper


@spell_timer
def fireball() -> str:
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args[-1] >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(13)
def iceball(power: int) -> str:
    return "Iceball cast!"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for count in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... "
                          f"(attempt {count}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(5)
def good_spell() -> str:
    return "Good cast!"


@retry_spell(5)
def bad_spell() -> str:
    raise Exception


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")
    print("\nTesting power validator...")
    test_powers = [13, 12, 27, 6]
    for power in test_powers:
        print(f"Power {power}: {iceball(power)}")
    print("\nTesting retry spell...")
    print("Good spell:")
    print(good_spell())
    print("Bad spell:")
    print(bad_spell())
    print("\nTesting MageGuild...")
    spell_names = ['tsunami', 'freeze', 'heal', 'blizzard']
    mage_names = ['Nova', 'Storm', 'Sage', 'Ember', 'Zara', 'Casey']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
    print(MageGuild.validate_mage_name(mage_names[0]))
    print(MageGuild.validate_mage_name(invalid_names[0]))
    mage = MageGuild()
    print(mage.cast_spell(spell_names[0], 15))
    print(mage.cast_spell(spell_names[1], 9))


if __name__ == "__main__":
    main()
