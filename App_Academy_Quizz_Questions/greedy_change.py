def greedy_change(value, coins):
    if value > 0 and len(coins) == 0 : return None 
    if value == 0 : return []
    new_val = value - max(coins)
    return [max(coins)] + greedy_change(new_val, list(filter(lambda c: c <= new_val, coins)))

greedy_change(25, [7, 3, 4]) 
# [7, 7, 7, 4]
