'''Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"
Constraints:

[time limit] 5000ms

[input] array.character arr

1 ≤ arr.length ≤ 30
[input] string str

1 ≤ str.length ≤ 500
[output] string'''

def get_shortest_unique_substring(arr, str):
    counter_hash = {}
    for char in arr:
        counter_hash[char] = 0

    front = 0
    back = 0
    counter = 0

    stored_front = float('inf')
    stored_back = float('-inf')

    while front < len(str):
        print(str[front])
        print(counter_hash.get(str[front], -1) >= 0)

        if counter_hash.get(str[front], -1) >= 0:
            print(counter_hash[char])
            if counter_hash[char] == 0:
                counter += 1
            counter_hash[char] += 1
        front += 1

        while counter >= len(arr):
            if stored_front - stored_back > front - back:
                stored_front = front
                stored_back = back

            if counter_hash.get(str[back], -1) >= 0:
                counter_hash[str[back]] -= 1
                if counter_hash[str[back]] == 0:
                    counter -= 1

            back += 1

    if stored_front == float('inf') or stored_back == float('-inf'):
        return ""
    return str[stored_back:stored_front + 1]


get_shortest_unique_substring(["A", "B", "C"], "ADOBECODEBANCDDD")