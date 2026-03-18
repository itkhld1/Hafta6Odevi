from typing import Iterable

def average_ratios(numbers: Iterable[float]) -> float:
    """Compute the average of 100/n for each non-zero n in numbers.

    Zeros are skipped. Raises ValueError if there are no non-zero numbers.
    """
    ratios = [100.0 / n for n in numbers if n != 0]
    if not ratios:
        raise ValueError("No non-zero numbers to compute average")
    return sum(ratios) / len(ratios)

if __name__ == "__main__":
    # example usage / quick manual check
    print(average_ratios([10, 5, 0]))
