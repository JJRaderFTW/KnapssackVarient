# COP4533 - Knapsack Variant project
# 11/29/23
# Collaborators: Javier Lopez, Sean Cheema, Rickard Sorkin

def opt(
        total_items: int,
        desired_weight: int,
        final_num_items: int,
        weights: list[int],
        values: list[int]
):
    """
    Knapsack Variant

    :param total_items: number of items in the list (i)
    :param desired_weight: desired weight (w)
    :param final_num_items: number of desired items (k)
    :param weights: list of weights
    :param values: list of values
                the 3-Dimensional matrix produced by this function.
    """
    # 3D matrix (i, w, k)
    mat = [[[0 for _ in range(final_num_items+1)] for _ in range(desired_weight+1)] for _ in range(total_items+1)]

    # fill the 3D matrix with every possible combination of i, w, k
    for i in range(1, total_items+1):
        for w in range(1, desired_weight+1):
            for k in range(1, final_num_items+1):
                # number of items is less than desired number of items
                if i < k:
                    mat[i][w][k] = float('-inf')
                # desired weight has not been fulfilled and we can no longer take items
                elif w > 0 and k == 0:
                    mat[i][w][k] = float('-inf')
                # desired weight has been fulfilled but we have not taken the desired number of items
                elif w == 0 and k > 0:
                    mat[i][w][k] = float('-inf')
                # desired weight and desired number of items have both been fulfilled
                elif w == 0 and k == 0:
                    mat[i][w][k] = 0
                # current item's weight is greater than desired weight so look at the previous item
                elif weights[i-1] > desired_weight:
                    mat[i][w][k] = mat[i-1][w][k]
                # take max of taking the current item vs not taking the item
                else:
                    mat[i][w][k] = max(mat[i-1][w][k], mat[i-1][w-weights[i-1]][k-1] + values[i-1])

    # return max value and matrix
    return mat[-1][-1][-1], mat


def traceback(
        mat: list[list[list[int]]]
):
    """
    Traceback function for knapsack variant

    :param mat: knapsack matrix
    :return: set of items taken
    """
    pass


if __name__ == '__main__':
    total_items = 5
    desired_weight = 10
    final_num_weights = 3
    weights = [3, 4, 2, 6, 5]
    values = [8, 10, 4, 12, 6]

    max, mat = opt(total_items, desired_weight, final_num_weights, weights, values)

    items_taken = traceback(mat)

    print(
        f'Maximum value: {max}\n' \
        f'Using items: {items_taken}'
    )
    


