def shifted_arr_search(shiftArr, num):
  return rotated_search(shiftArr, num, 0, len(shiftArr))


def rotated_search(arr, target, left, right):
  if right <= left:
    return -1

  mid = left + ((right - left) // 2)

  if arr[mid] == target:
    return mid
  
  if arr[mid] < arr[left]:
    if arr[mid] < target and arr[left] > target:
      return rotated_search(arr, target, mid+1, right)
    else:
      return rotated_search(arr, target, left, mid)
  elif arr[mid] > target and arr[left] <= target:
      return rotated_search(arr, target, left, mid)
  else:
      return rotated_search(arr, target, mid+1, right)


print(shifted_arr_search([0, 1,2,3,4,5], 1))
