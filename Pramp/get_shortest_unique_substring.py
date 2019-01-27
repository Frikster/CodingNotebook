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
  counter_hash = {}  # keeps track of how many of each character is in the current window
  for char in arr:
    counter_hash[char] = 0

  front = 0
  back = 0
  unique_counter = 0  # keeps track of how many unique elements in window that are in arr

  # keep track of a candidate window. Store it and keep searching. If better one found, replace this one.
  stored_front = float('inf')
  stored_back = float('-inf')

  while front < len(str):
    print(str[back:front])
    if str[front] in counter_hash:
      if counter_hash[str[front]] == 0:
        unique_counter += 1
      counter_hash[str[front]] += 1
    front += 1

    while unique_counter >= len(arr):
      if stored_front - stored_back > front - back:
        stored_front = front
        stored_back = back

      if str[back] in counter_hash:
        # move back forward therefore remove char at back of window
        counter_hash[str[back]] -= 1
        if counter_hash[str[back]] == 0:
          unique_counter -= 1

      back += 1

  if stored_front == float('inf') or stored_back == float('-inf'):
    return ""
  return str[stored_back:stored_front]


print(get_shortest_unique_substring(['A', 'B', 'C'], "ADBCQWERTY"))
get_shortest_unique_substring(["A", "B", "C"], "ADOBECODEBANCDDD")
