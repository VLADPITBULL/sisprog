def get_quantity_for_product(product_type: int, material_type: int, count: int, width: float, length: float) -> int:
    # Пример: 5% потери
    waste_factor = 1.05
    raw_area_per_unit = width * length
    total_area = raw_area_per_unit * count * waste_factor
    return int(round(total_area))
