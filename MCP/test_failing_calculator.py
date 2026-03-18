# python
import pytest
from MCP.failing_calculator import average_ratios

def test_average_ratios_skips_zero():
    # (100/10 + 100/5) / 2 == (10 + 20) / 2 == 15.0
    assert average_ratios([10, 5, 0]) == pytest.approx(15.0)

def test_average_ratios_all_zeros_raises():
    with pytest.raises(ValueError):
        average_ratios([0, 0])