"""
"""

from sorting_algorithms import merge_sort, selection_sort, \
                                insertion_sort, shell_sort
from sorting_algorithms_number_of_operations import insertion_sort_comparisons, merge_sort_comparisons, selection_sort_comparisons, \
                                                    shell_sort_comparisons
from time_comparison import experiment_1, experiment_2, experiment_3, experiment_4
from number_of_operations_comparison import experiment_1_comparisons, experiment_2_comparisons, experiment_3_comparisons, experiment_4_comparisons
import matplotlib.pyplot as plt
import copy


def build_graphic(sorting_algs, experiment):
    """
    """

    sorting_algs_copy = copy.deepcopy(sorting_algs)

    sorting_algs_table = {}
    for sorting_alg in sorting_algs:
        sorting_algs_table[sorting_alg] = [[], []]

    for power in range(7, 16, 2):
        size = 2 ** power
        sorting_algs_copy = copy.deepcopy(sorting_algs)
        sorting_algs_results = experiment(size, sorting_algs=sorting_algs_copy)

        for sorting_alg in sorting_algs_results:
            sorting_algs_table[sorting_alg][0].append(power)
            sorting_algs_table[sorting_alg][1].append(sorting_algs_results[sorting_alg])

    for sorting_alg in sorting_algs_table:
        x1 = sorting_algs_table[sorting_alg][0]
        y1 = sorting_algs_table[sorting_alg][1]

        plt.plot(x1, y1, label = f"{sorting_alg}")
        

    plt.yscale('log')

    plt.xlabel('x - axis')

    plt.ylabel('y - axis')

    plt.title(f'{experiment}')
    

    plt.legend()
    

    plt.show()

    return sorting_algs_table

def main(sorting_algs = \
                {merge_sort: [],
                 shell_sort: [],
                 insertion_sort: [],
                 selection_sort: [],
                 },
                 sorting_algs_comparison = \
                {merge_sort_comparisons: [],
                 shell_sort_comparisons: [],
                 insertion_sort_comparisons: [],
                 selection_sort_comparisons: [],
                 }):
    """
    """

    sorting_algs_copy = copy.deepcopy(sorting_algs)
    sorting_algs_comparison = copy.deepcopy(sorting_algs_comparison)

    build_graphic(sorting_algs_copy, experiment_1)
    build_graphic(sorting_algs_comparison, experiment_1_comparisons)

    build_graphic(sorting_algs_copy, experiment_2)
    build_graphic(sorting_algs_comparison, experiment_2_comparisons)

    build_graphic(sorting_algs_copy, experiment_3)
    build_graphic(sorting_algs_comparison, experiment_3_comparisons)

    build_graphic(sorting_algs_copy, experiment_4)
    build_graphic(sorting_algs_comparison, experiment_4_comparisons)


if __name__ == "__main__":
    main()
