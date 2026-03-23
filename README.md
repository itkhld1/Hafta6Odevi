# mystery_module

A small utility module to compute the real roots of a quadratic equation ax^2 + bx + c = 0.

## Overview

The module exposes a single function:

- `fn_x(a, b, c)`

Behavior:
- If the discriminant (b^2 − 4ac) is negative, the function returns `None` (no real roots).
- If the discriminant is zero or positive, the function returns a 2-tuple `(root1, root2)` of floats:
  - root1 = (-b + sqrt(discriminant)) / (2a)
  - root2 = (-b - sqrt(discriminant)) / (2a)
- If `a == 0` the function divides by `2*a` and will raise `ZeroDivisionError`. The module does not handle linear equations.

This README documents usage, examples, edge cases, testing suggestions, and recommended improvements.

## Installation

Copy `mystery_module.py` into your project (for example, `MCP/mystery_module.py`) or ensure the package that contains it is importable on your `PYTHONPATH`. The function depends only on the Python standard library.

## API

fn_x(a: float, b: float, c: float) -> Optional[Tuple[float, float]]

- Parameters:
  - `a`, `b`, `c`: coefficients of the quadratic equation (expected numeric types).
- Returns:
  - `(x1, x2)` — tuple of floats when discriminant >= 0.
  - `None` — when discriminant < 0 (no real roots).
- Raises:
  - `ZeroDivisionError` if `a == 0`.
  - `TypeError` if non-numeric types are passed and arithmetic fails.

## Handling a linear case (a == 0) before calling fn_x:

a, b, c = 0, 2, -4
if a == 0:
    if b == 0:
        raise ValueError("Degenerate equation: a == 0 and b == 0")
    x = -c / b
    print("Linear root:", x)
else:
    print("Quadratic roots:", fn_x(a, b, c))
    

## Usage

Basic usage (import from the package path used in this repository):

```python
# python
from MCP.mystery_module import fn_x

# Distinct real roots
roots = fn_x(1, -3, 2)   # returns (2.0, 1.0)

# Repeated real root (discriminant == 0)
roots = fn_x(1, 2, 1)    # returns (-1.0, -1.0)

# No real roots
roots = fn_x(1, 0, 1)    # returns None

