# Реализовать алгоритм пирамидальной сортировки (сортировка кучей)

def heapify(integer_list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and integer_list[i] < integer_list[left]:
        largest = left

    if right < n and integer_list[largest] < integer_list[right]:
        largest = right

    if largest != i:
        integer_list[i], integer_list[largest] = integer_list[largest], integer_list[i]
        heapify(integer_list, n, largest)


def heapsort(int_list):
    n = len(int_list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(int_list, n, i)

    for i in range(n - 1, 0, -1):
        int_list[i], int_list[0] = int_list[0], int_list[i]
        heapify(int_list, i, 0)

    return int_list


arr = [100, 2, 83, 14, 1144, 36, 777, -65, 56, 89]
sorted_arr = heapsort(arr)
print(sorted_arr)
