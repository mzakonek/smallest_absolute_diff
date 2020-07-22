from validators import check_if_valid


def find_smallest_absolute_diff(A: list, B: list) -> int:
    """
    This function returns the smallest absolute diff, found between the pair of two numbers from A and B list.

    :param A: list of integers, given in the ascending order
    :param B: list of integers, given in the descending order
    :return: the smallest absoulte diff that was found
    """

    # check parameters if valid
    check_if_valid(A, is_ascending=True)
    check_if_valid(B, is_ascending=False)

    # reverse the list which is now in the descending order
    B = B[::-1]

    minimum = float("inf")
    len_a = len(A)
    len_b = len(B)
    i = j = 0

    while i < len_a and j < len_b:
        diff = A[i] - B[j]
        minimum = min(minimum, abs(diff))

        if diff < 0:
            i += 1
        elif diff > 0:
            j += 1
        else:
            break
    A = B = 0
    return minimum

