#!/usr/bin/env python3

from typing import Callable, Any


def mage_counter() -> Callable:
    counter = 0

    def increment_counter() -> int:
        nonlocal counter
        counter += 1
        return counter
    return increment_counter


def spell_accumulator(initial_power: int) -> Callable:
    def increment_power(additional_power: int) -> int:
        nonlocal initial_power
        initial_power += additional_power
        return initial_power
    return increment_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant_item(item: str) -> str:
        return f"{enchantment_type} {item}"
    return enchant_item


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(store_key: str, store_value: Any) -> None:
        vault[store_key] = store_value

    def recall(store_key: str) -> Any:
        try:
            return vault[store_key]
        except KeyError:
            return "Memory not found"
    return {"store": store, "recall": recall}


def main() -> None:
    """Run the main program."""
    print("\nTesting mage counter...")
    increment_counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {increment_counter()}")
    print("\nTesting spell accumulator...")
    initial_powers = [55, 29, 48]
    power_additions = [7, 12, 20, 10, 17]
    increment_power = spell_accumulator(initial_powers[0])
    print(f"Initial power: {initial_powers[0]}")
    for power in power_additions:
        print(f"+{power} = {increment_power(power)}")
    print("\nTesting enchantment factory...")
    enchantment_types = ["Flaming", "Radiant", "Earthen"]
    flaming_factory = enchantment_factory(enchantment_types[0])
    radiant_factory = enchantment_factory(enchantment_types[1])
    items_to_enchant = ["Ring", "Shield", "Amulet", "Wand"]
    print(flaming_factory(items_to_enchant[0]))
    print(radiant_factory(items_to_enchant[1]))
    print("\nTesting memory vault...")
    my_vault = memory_vault()
    my_vault["store"]("test", "Save this!")
    print(f"Happy path: {my_vault['recall']('test')}")
    print(f"Unhappy path: {my_vault['recall']('fail')}")


if __name__ == "__main__":
    main()
