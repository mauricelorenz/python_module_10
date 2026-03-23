#!/usr/bin/env python3

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {"max_power": max(mages, key=lambda mage: mage["power"])["power"],
            "min_power": min(mages, key=lambda mage: mage["power"])["power"],
            "avg_power": round(sum([mage["power"] for mage in mages])
                               / len(mages), 2)}


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [{"name": "Earth Shield", "power": 107, "type": "focus"},
                 {"name": "Ice Wand", "power": 92, "type": "focus"},
                 {"name": "Crystal Orb", "power": 117, "type": "weapon"},
                 {"name": "Earth Shield", "power": 111, "type": "relic"}]
    mages = [{"name": "River", "power": 57, "element": "light"},
             {"name": "Riley", "power": 75, "element": "earth"},
             {"name": "Casey", "power": 90, "element": "ice"},
             {"name": "Sage", "power": 64, "element": "shadow"},
             {"name": "Casey", "power": 67, "element": "earth"}]
    spells = ["fireball", "tornado", "heal", "meteor"]
    artifacts_sorted = artifact_sorter(artifacts)
    print(f"{artifacts_sorted[0]['name']} ({artifacts_sorted[0]['power']} "
          f"power) comes before {artifacts_sorted[1]['name']} "
          f"({artifacts_sorted[1]['power']} power)")
    mages_filtered = power_filter(mages, 67)
    print("\nTesting power filter...")
    print("Mages with power greater or equal to 67:")
    for mage in mages_filtered:
        print(f"- {mage['name']} ({mage['power']} power)")
    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    for spell in transformed_spells:
        print(spell, end=" ")
    print()
    print("\nTesting mage_stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
