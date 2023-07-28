def heapify(arr, n, i):
    """
    Функция для преобразования поддерева с корнем в индексе i в пирамиду (max heap).
    Параметры:
        arr (list): Список элементов, который нужно отсортировать.
        n (int): Размер пирамиды (количество элементов в поддереве).
        i (int): Индекс корня поддерева.
    """
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    # Если левый потомок больше корня
    if left_child < n and arr[i] < arr[left_child]:
        largest = left_child

    # Если правый потомок больше корня
    if right_child < n and arr[largest] < arr[right_child]:
        largest = right_child

    # Если корень не является наибольшим, меняем местами с наибольшим потомком
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Функция для сортировки списка с использованием пирамидальной сортировки.
    Параметры:
        arr (list): Список элементов, который нужно отсортировать.
    """
    n = len(arr)

    # Построение max heap
    # Начинаем с последнего узла, у которого есть потомки
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлечение элементов из max heap один за другим
    for i in range(n - 1, 0, -1):
        # Перемещаем текущий корень в конец
        arr[0], arr[i] = arr[i], arr[0]  # Меняем местами
        # Вызываем heapify для уменьшения размера пирамиды
        heapify(arr, i, 0)


# Пример использования:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Отсортированный массив:")
print(arr)
