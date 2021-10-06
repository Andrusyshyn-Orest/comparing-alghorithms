"""

"""




def selection_sort_comparisons(arr: list):
    """

    """

    counter = 0
    length = len(arr)


    for i in range(length):
        min_ind = i

        for j in range(i+1, length):
            if arr[j] < arr[min_ind]:
                
                min_ind = j
            counter += 1

        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    return counter

def insertion_sort_comparisons(arr: list):
    """
    """

    length = len(arr)
    counter = 0

    for i in range(1, length):
 
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                counter += 1
                j -= 1
        counter += 1
        arr[j + 1] = key

    return counter


def merge_sort_comparisons(lst: list, counter = 0) -> list:
    """
    Returns sorted lst using merge sort.

    """

    length = len(lst)
    counter += 1
    if length < 2:
        return counter

    middle = length // 2
    lst1 = lst[:middle]
    lst2 = lst[middle:]

    counter += merge_sort_comparisons(lst1)
    counter  += merge_sort_comparisons(lst2)
    counter += merge_comparisons(lst1, lst2, lst)
    return counter


def merge_comparisons(lst1: list, lst2: list, lst3: list, counter = 0):
    """
    Merges sorted lists lst1 and lst2 in lst3.
    len(lst3) == len(lst1) + len(lst2). Returns
    nothing, just changes lst3.

    """

    in1 = in2 = in3 = 0
    len1, len2 = len(lst1), len(lst2)

    while (in1 < len1) and (in2 < len2):
        if lst1[in1] < lst2[in2]:
            lst3[in3] = lst1[in1]
            in1 += 1
        else:
            lst3[in3] = lst2[in2]
            in2 += 1
        counter += 1
        in3 += 1

    while in1 < len1:
        counter += 1
        lst3[in3] = lst1[in1]
        in3 += 1
        in1 += 1

    while in2 < len2:
        counter += 1
        lst3[in3] = lst2[in2]
        in3 += 1
        in2 += 1

    return counter

def shell_sort_comparisons(arr):
    """
    >>> arr = [1]
    >>> shell_sort(arr)
    [1]
    >>> arr = []
    >>> shell_sort(arr)
    []
    >>> arr = [1,1,1,1,1,1]
    >>> shell_sort(arr)
    [1, 1, 1, 1, 1, 1]
    >>> arr = [1, 2, 3]
    >>> shell_sort(arr)
    [1, 2, 3]
    >>> arr = [4,2,0,9,6,4]
    >>> shell_sort(arr)
    [0, 2, 4, 4, 6, 9]
    >>> arr = [3, 5, 1, 0, 4]
    >>> shell_sort(arr)
    [0, 1, 3, 4, 5]
    >>> arr = [3,0, 3, 4, 1]
    >>> shell_sort(arr)
    [0, 1, 3, 3, 4]
    """

    counter = 0
    n = len(arr)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                counter += 1
                arr[j] = arr[j - interval]
                j -= interval

            arr[j] = temp
            counter += 1
        interval //= 2

    return counter


if __name__ == "__main__":
    print(insertion_sort_comparisons([1,2,3,4,5,6]))
