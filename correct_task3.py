def average_valid_measurements(values):
    if not values:
        return 0
    
    total = 0
    valid_count = 0
    
    for v in values:
        if v is not None:
            try:
                num_value = float(v)
                total += num_value
                valid_count += 1
            except (ValueError, TypeError):
                continue
    
    return total / valid_count if valid_count > 0 else 0