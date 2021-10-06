"""
"""

from sorting_algorithms_number_of_operations import insertion_sort_comparisons, merge_sort_comparisons, selection_sort_comparisons, \
                                                    shell_sort_comparisons

import time
import random
import copy


def experiment_1_comparisons(size: int, num_of_exp = 5, sorting_algs = \
                {merge_sort_comparisons: [],
                 shell_sort_comparisons: [],
                 insertion_sort_comparisons: [],
                 selection_sort_comparisons: [],
                 }):
    """
    """

    sorting_algs = copy.deepcopy(sorting_algs)

    for j in range(num_of_exp):
        generated_list = []
        for i in range(size):
            generated_list.append(random.randint(0, size))

        

        for sorting_alg in sorting_algs:
            # print(sorting_alg)
            generated_list_copy = copy.deepcopy(generated_list)

            comp = sorting_alg(generated_list_copy)

            sorting_algs[sorting_alg].append(comp)
            # print(sorting_algs)

    for sorting_alg in sorting_algs:
        sorting_algs[sorting_alg] = sum(sorting_algs[sorting_alg])/num_of_exp

    return sorting_algs


def experiment_2_comparisons(size: int, num_of_exp = 1, sorting_algs = \
                {merge_sort_comparisons: [],
                 shell_sort_comparisons: [],
                 insertion_sort_comparisons: [],
                 selection_sort_comparisons: [],
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
            comp = sorting_alg(generated_list_copy)


            sorting_algs[sorting_alg] = comp
            # print(sorting_algs)

    return sorting_algs
    
    
def experiment_3_comparisons(size: int, num_of_exp = 1, sorting_algs = \
                {merge_sort_comparisons: [],
                 shell_sort_comparisons: [],
                 insertion_sort_comparisons: [],
                 selection_sort_comparisons: [],
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
            comp = sorting_alg(generated_list_copy)

            sorting_algs[sorting_alg] = comp
            # print(sorting_algs)

    return sorting_algs


def experiment_4_comparisons(size: int, num_of_exp = 3, sorting_algs = \
                {merge_sort_comparisons: [],
                 shell_sort_comparisons: [],
                 insertion_sort_comparisons: [],
                 selection_sort_comparisons: [],
                 }):
    """
    """

    sorting_algs = copy.deepcopy(sorting_algs)

    generated_list = []
    for i in range(size):
            generated_list.append(random.choice([1, 2, 3]))

    for j in range(num_of_exp):
        random.shuffle(generated_list)
        
        for sorting_alg in sorting_algs:
            # print(sorting_alg)
            generated_list_copy = copy.deepcopy(generated_list)

            comp = sorting_alg(generated_list_copy)

            sorting_algs[sorting_alg].append(comp)
            # print(sorting_algs)

    for sorting_alg in sorting_algs:
        sorting_algs[sorting_alg] = sum(sorting_algs[sorting_alg])/num_of_exp

    return sorting_algs    


if __name__ == "__main__":
    print(experiment_1_comparisons(2**7))
    print(experiment_2_comparisons(2**7))
    print(experiment_3_comparisons(2**7))
    print(experiment_4_comparisons(2**7))
