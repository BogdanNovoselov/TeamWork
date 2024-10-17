import unittest
import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

def heapify(arr, n, i):

    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def radix_sort(arr):

    RADIX = 10
    placement = 1
    max_digit = max(arr)
    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr


class TestSortFunctions(unittest.TestCase):
    # Проверка на прваильность сортировки
    def test_quicksort(self):
        self.assertEqual(quicksort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(quicksort([5, 2, 9, 1, 7, 3]), [1, 2, 3, 5, 7, 9])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(selection_sort([5, 2, 9, 1, 7, 3]), [1, 2, 3, 5, 7, 9])

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([3, 6, 8, 10, 1, 2, 1]), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(bubble_sort([5, 2, 9, 1, 7, 3]), [1, 2, 3, 5, 7, 9])

    # Проверка на время сортировки
    def test_quicksort_time(self):
        for n in [100, 500, 1000, 5000, 10000]:
            arr = [random.randint(0, 1000) for _ in range(n)]
            start_time = time.time()
            quicksort(arr.copy())
            end_time = time.time()
            self.assertLess(end_time - start_time, 1) # время не должно превышать 10 секунд

    def test_selection_sort_time(self):
        for n in [100, 500, 1000, 5000, 10000]:
            arr = [random.randint(0, 1000) for _ in range(n)]
            start_time = time.time()
            selection_sort(arr.copy())
            end_time = time.time()
            self.assertLess(end_time - start_time, 1)  # время не должно превышать 10 секунд

    def test_bubble_sort_time(self):
        for n in [100, 500, 1000, 5000, 10000]:
            arr = [random.randint(0, 1000) for _ in range(n)]
            start_time = time.time()
            bubble_sort(arr.copy())
            end_time = time.time()
            self.assertLess(end_time - start_time, 1)  # время не должно превышать 16 секунд

    def test_merge_sort_time(self):
        for n in [100, 500, 1000, 5000, 10000]:
            arr = [random.randint(0, 1000) for _ in range(n)]
            start_time = time.time()
            merge_sort(arr.copy())
            end_time = time.time()
            self.assertLess(end_time - start_time, 1)  # время не должно превышать 1 секунду


    def test_heap_sort_time(self):
        for n in [100, 500, 1000, 5000, 10000]:
            arr = [random.randint(0, 1000) for _ in range(n)]
            start_time = time.time()
            heap_sort(arr.copy())
            end_time = time.time()
            self.assertLess(end_time - start_time, 1)  # время не должно превышать 1 секунду


    def test_radix_sort_time(self):
        for n in [100, 500, 1000, 5000, 10000]:
            arr = [random.randint(0, 1000) for _ in range(n)]
            start_time = time.time()
            radix_sort(arr.copy())
            end_time = time.time()
            self.assertLess(end_time - start_time, 1)  # время не должно превышать 1 секунду



if __name__ == '__main__':
    unittest.main()
