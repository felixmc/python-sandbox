import math

# arr must be sorted
def binarySearch (arr, needle):
  print('searching for', needle, 'in [', ' '.join(map(str,arr)), ']')

  left = 0
  right = len(arr) - 1

  found = -1
  its = 0

  while (found == -1 and left <= right):
    its += 1
    mid = math.floor((left + right) / 2)
    midValue = arr[mid]

    print('iteration', its, '>> L:', left, '| R:', right, '| M', mid, '| arr[M]:', midValue)

    if (needle == midValue):
      found = mid
    elif (needle > midValue):
     left = mid + 1
    else:
     right = mid - 1

  print('found at [', found, '] after', its, 'iterations')

  return found



arr = [1, 2, 3, 4, 5, 6, 7]

binarySearch(arr, 5)
