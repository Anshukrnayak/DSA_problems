def merge_two_arr(left, right):
   """Merges two sorted arrays into a single sorted array.

    Args:
        left (list): First sorted array.
        right (list): Second sorted array.

    Returns:
        list: A sorted array containing all elements from left and right.
    """
   arr = []
   i = j = 0
   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         arr.append(left[i])
         i += 1
      else:
         arr.append(right[j])
         j += 1

   arr.extend(left[i:])
   arr.extend(right[j:])
   return arr


def merge_sort(arr):
   """Sorts an array using the Merge Sort algorithm.

    Args:
        arr (list): Array to be sorted.

    Returns:
        list: A sorted copy of the input array.
    """
   if len(arr) <= 1:
      return arr

   mid = len(arr) // 2
   left = merge_sort(arr[:mid])
   right = merge_sort(arr[mid:])

   return merge_two_arr(left, right)


def main():
   """Demonstrates Merge Sort on a sample array."""
   arr = [4, 2, 1, 3, 8]
   print(merge_sort(arr))


if __name__ == '__main__':
   main()