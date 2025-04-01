import pytest
from materials_subsystem.calculation import get_quantity_for_product

def test_get_quantity_for_product():
    result = get_quantity_for_product(
        product_type=1,
        material_type=2,
        count=10,
        width=2.0,
        length=3.0
    )
    assert result == 63  # 10 * 2 * 3 * 1.05 = 63
