def insertion_sort(arr):
    """
    Ordenação por Inserção (Insertion Sort).
    Retorna uma tupla: (lista_ordenada, numero_de_comparacoes)
    """
    arr = list(arr)
    comparacoes = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = key
    return arr, comparacoes

def merge_sort(arr):
    """
    Ordenação por Intercalação (Merge Sort).
    Retorna uma tupla: (lista_ordenada, numero_de_comparacoes)
    """
    arr = list(arr)
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_sorted, left_comp = merge_sort(arr[:mid])
    right_sorted, right_comp = merge_sort(arr[mid:])

    i = 0
    j = 0
    merged = []
    merge_comp = 0

    while i < len(left_sorted) and j < len(right_sorted):
        merge_comp += 1
        if left_sorted[i] <= right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1

    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    total_comp = left_comp + right_comp + merge_comp
    return merged, total_comp
