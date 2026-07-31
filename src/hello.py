"""A simple hello-world program."""

import sys


def greeting(name: str = "world") -> str:
    """Return a friendly greeting for ``name``."""
    return f"Hello, {name}!"


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greeting(name))


if __name__ == "__main__":
    main()
