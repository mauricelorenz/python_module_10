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
    pass


def retry_spell(max_attempts: int) -> Callable:
    pass


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass


def main() -> None:
    print("\nTesting spell timer...")
    print(f"Result: {fireball()}")
    test_powers = [13, 12, 27, 6]
    spell_names = ['tsunami', 'freeze', 'heal', 'blizzard']
    mage_names = ['Nova', 'Storm', 'Sage', 'Ember', 'Zara', 'Casey']
    invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']


if __name__ == "__main__":
    main()
