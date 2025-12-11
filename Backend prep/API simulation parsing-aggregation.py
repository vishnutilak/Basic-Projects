from collections import defaultdict

def process_orders(data_list: list[dict]) -> dict:
    """
    Filters incomplete orders, groups by region, and calculates the total amount 
    for each region using efficient Python techniques.
    """
    
    # 1. Filter and sum amounts, grouped by region
    # Using a defaultdict to simplify the accumulation step
    regional_totals = defaultdict(float)
    
    # Use a generator expression for efficiency (lazy processing)
    complete_orders = (
        order for order in data_list 
        if order.get('status') == 'complete'
    )
    
    for order in complete_orders:
        region = order.get('region')
        amount = order.get('amount', 0)
        
        if region:
            regional_totals[region] += amount
            
    # Convert defaultdict back to a regular dict for a cleaner API return
    return dict(regional_totals)
