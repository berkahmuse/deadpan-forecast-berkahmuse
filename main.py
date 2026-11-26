#!/usr/bin/env python3
"""Deadpan forecast for Updraft City.

A single-line weather forecast for a city that does not exist, written
in the flat, confident tone of a TV meteorologist reading off the map.
The line is a fixed string: the program is fully deterministic, takes no
input, touches no network, and always writes the exact same bytes.

Updraft City is a place where the rain falls upward, so everyday life
has adapted around it: umbrellas are carried upside down, and the
street sweepers do their work in the sky.
"""

from pathlib import Path

FORECAST = (
    "Updraft City: rain falls upward at 14 miles an hour tonight, so "
    "residents carry their umbrellas upside down and street sweepers "
    "work the sky."
)

OUTPUT_PATH = Path("/output/entry.txt")


def build_forecast() -> str:
    """Return the forecast line, trimmed to one line under the cap."""
    line = " ".join(FORECAST.split())
    if not 1 <= len(line) <= 160:
        raise ValueError(f"forecast is {len(line)} chars, must be 1-160")
    return line


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(build_forecast() + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
