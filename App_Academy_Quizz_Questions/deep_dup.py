# Using recursion and the is_a? method,
# write an Array#deep_dup method that will perform a "deep" duplication of the interior arrays.

def deep_dup(arr):
    return list(map(lambda el: deep_dup(el) if isinstance(el, list) else el, arr))


robot_parts = [["nuts", "bolts", [], "washers"],["capacitors", "resistors", "inductors"]]
deep_dup(robot_parts) == robot_parts