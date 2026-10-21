"""A tiny greeting for a first open-source trial."""

from datetime import date


def main() -> None:
    today = date.today().isoformat()
    print(f"Hello from codex-oss-trial! Today is {today}.")


if __name__ == "__main__":
    main()
