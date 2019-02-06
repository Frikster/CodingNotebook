# Not added to Anki...
def greedy_change(value, coins):
    if value == 0 : return []
    if len(coins) == 0 : return None 
    coins = [c for c in coins if c <= value]
    value -= max(coins)
    return [max(coins)] + greedy_change(value, coins)
    # return [max(coins)] + greedy_change(new_val, list(filter(lambda c: c <= new_val, coins)))

print(greedy_change(25, [7, 3, 4]) )
# [7, 7, 7, 4]
print(greedy_change(25, [50, 7, 3, 4]) )
print(greedy_change(26, [50, 7, 3, 4]) )

