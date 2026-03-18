from pathlib import Path
from typing import Iterable, List

DEFAULT_MARKUP_RATE = 1.15
DEFAULT_LOG_PATH = Path("log.txt")


def apply_markup(value: float, rate: float = DEFAULT_MARKUP_RATE) -> float:
    """Return value after applying a markup rate."""
    return value * rate


def format_total(value: float) -> str:
    """Return a formatted string for a numeric total."""
    return f"Total: {value:.2f}"


def append_log(values: Iterable[float], log_path: Path = DEFAULT_LOG_PATH) -> None:
    """Append the list of values to the given log file (one entry per call)."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(str(list(values)) + "\n")


def process_data(
    data: Iterable[float],
    rate: float = DEFAULT_MARKUP_RATE,
    log_path: Path = DEFAULT_LOG_PATH,
    print_output: bool = True,
) -> List[float]:
    """
    Process numeric input by applying a markup rate, optionally print formatted results,
    append the numeric results to a log file, and return the numeric results.

    - data: iterable of numeric values
    - rate: markup multiplier (default 1.15)
    - log_path: file path to append logs
    - print_output: when True, prints formatted totals
    """
    results: List[float] = []
    for d in data:
        # Let Python raise TypeError for non-numeric inputs; callers can validate earlier.
        val = apply_markup(float(d), rate)
        formatted = format_total(val)
        if print_output:
            print(formatted)
        results.append(val)

    append_log(results, Path(log_path))
    return results
