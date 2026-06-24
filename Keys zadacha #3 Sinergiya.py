def sum_negative_between_max_min(arr):
    if len(arr) < 2:
        return 0  # если меньше двух элементов, между ними ничего нет

    # Индексы первого вхождения максимума и минимума
    idx_max = arr.index(max(arr))
    idx_min = arr.index(min(arr))

    # Определяем границы подмассива между ними (не включая сами элементы)
    left = min(idx_max, idx_min) + 1
    right = max(idx_max, idx_min) - 1

    # Если границы пересеклись, то между ними нет элементов
    if left > right:
        return 0

    # Суммируем отрицательные элементы в этом промежутке
    total = 0
    for i in range(left, right + 1):
        if arr[i] < 0:
            total += arr[i]
    return total

# Пример использования
if __name__ == "__main__":
    A = [3, -5, 2, -1, 8, -7, 0, -4]
    # максимум 8 на индексе 4, минимум -7 на индексе 5 -> между ними индекс 4 
    # на самом деле между ними ничего нет, т.к. индексы соседние -> сумма 0
    # но пример можно изменить
    print(sum_negative_between_max_min(A))  # 0

    B = [10, -2, -5, 3, -8, 1]
    # max=10 (index0), min=-8 (index4) -> между индексы 1,2,3 -> значения -2,-5,3 -> отрицательные -2,-5 сумма -7
    print(sum_negative_between_max_min(B))  # -7
