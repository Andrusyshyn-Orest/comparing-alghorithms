"""
"""

from sorting_algorithms import merge_sort, selection_sort, \
                                insertion_sort, shell_sort

import time
import random
import copy


def experiment_1(size: int, num_of_exp = 5, sorting_algs = \
                {merge_sort: [],
                 shell_sort: [],
                 insertion_sort: [],
                 selection_sort: [],
                 }):
    """
    """

    sorting_algs = copy.deepcopy(sorting_algs)

    time_list = []
    for j in range(num_of_exp):
        generated_list = []
        for i in range(size):
            generated_list.append(random.randint(0, size))

        

        for sorting_alg in sorting_algs:
            # print(sorting_alg)
            generated_list_copy = copy.deepcopy(generated_list)

            start = time.time()
            sorting_alg(generated_list_copy)
            finish = time.time()

            sorting_algs[sorting_alg].append(finish - start)
            # print(sorting_algs)

    for sorting_alg in sorting_algs:
        sorting_algs[sorting_alg] = sum(sorting_algs[sorting_alg])/num_of_exp

    return sorting_algs


def experiment_2(size: int, num_of_expr = 1, sorting_algs = \
                {merge_sort: [],
                 shell_sort: [],
                 insertion_sort: [],
                 selection_sort: [],
                 }):
    """
    """
    sorting_algs = copy.deepcopy(sorting_algs)
    
    generated_list = []
    for i in range(size):
        generated_list.append(i)

    for sorting_alg in sorting_algs:
            # print(sorting_alg)

            generated_list_copy = copy.deepcopy(generated_list)
            start = time.time()
            sorting_alg(generated_list_copy)
            finish = time.time()

            sorting_algs[sorting_alg] = finish - start
            # print(sorting_algs)

    return sorting_algs
    
    
def experiment_3(size: int, num_of_expr = 1, sorting_algs = \
                {merge_sort: [],
                 shell_sort: [],
                 insertion_sort: [],
                 selection_sort: [],
                 }):
    """
    """
    sorting_algs = copy.deepcopy(sorting_algs)
    
    generated_list = []
    for i in range(size):
        generated_list.append(size - i)

    for sorting_alg in sorting_algs:
            # print(sorting_alg)

            generated_list_copy = copy.deepcopy(generated_list)
            start = time.time()
            sorting_alg(generated_list_copy)
            finish = time.time()

            sorting_algs[sorting_alg] = finish - start
            # print(sorting_algs)

    return sorting_algs


def experiment_4(size: int, num_of_exp = 3, sorting_algs = \
                {merge_sort: [],
                 shell_sort: [],
                 insertion_sort: [],
                 selection_sort: [],
                 }):
    """
    """

    sorting_algs = copy.deepcopy(sorting_algs)

    time_list = []
    generated_list = []
    for i in range(size):
            generated_list.append(random.choice([1, 2, 3]))

    for j in range(num_of_exp):
        random.shuffle(generated_list)
        
        for sorting_alg in sorting_algs:
            # print(sorting_alg)
            generated_list_copy = copy.deepcopy(generated_list)

            start = time.time()
            sorting_alg(generated_list_copy)
            finish = time.time()

            sorting_algs[sorting_alg].append(finish - start)
            # print(sorting_algs)

    for sorting_alg in sorting_algs:
        sorting_algs[sorting_alg] = sum(sorting_algs[sorting_alg])/num_of_exp

    return sorting_algs    


if __name__ == "__main__":
    print(experiment_1(2**7))
    print(experiment_2(2**7))
    print(experiment_3(2**7))
    print(experiment_4(2**7))
