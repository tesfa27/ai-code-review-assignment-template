def calculate_average_order_value(orders):
    if not orders:
        return 0
    
    total = 0
    valid_count = 0
    
    for order in orders:
        if not isinstance(order, dict):
            continue
        
        status = order.get("status", "").lower()
        if status != "cancelled":
            amount = order.get("amount", 0)
            if isinstance(amount, (int, float)) and amount >= 0:
                total += amount
                valid_count += 1
    
    return total / valid_count if valid_count > 0 else 0