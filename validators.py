import multiprocessing

# marginal value of length that checked list will need to have, to multiprocess validations
min_len_to_multiprocess = 10000000


def is_sorted(list_, if_ascending, returned_values_manager=None):
    """
    It checks if list is properly sorted
    :param returned_values_manager: given if running in multiprocessing
    """
    if if_ascending:
        is_sorted = all(x <= y for x, y in zip(list_, list_[1:]))
    else:
        is_sorted = all(x >= y for x, y in zip(list_, list_[1:]))

    if returned_values_manager:
        returned_values_manager.append(is_sorted)
    else:
        return is_sorted


def integers_only(list_, returned_values_manager=None):
    """
    It checks if list contains only integers.
    :param returned_values_manager: given if running in multiprocessing
    """

    is_valid = all(isinstance(x, int) for x in list_)

    if returned_values_manager:
        returned_values_manager.append(is_valid)
    else:
        return is_valid


def check_if_valid(list_to_check: list, is_ascending: bool) -> None:
    """
    Asserts that checks if input is valid.
    If length of list is longer than value set in
    """

    # check if list has proper type
    assert isinstance(list_to_check, list) is True

    # if list is very long, multiprocess time consuming validations, where it is at least O(n)
    if len(list_to_check) > min_len_to_multiprocess:
        # use manager to create list that will hold return statements by multiprocessed functions
        manager = multiprocessing.Manager()
        validators_returned = manager.list()

        jobs = []

        worker_checkints = multiprocessing.Process(
            name='ints_only', target=integers_only, args=(list_to_check, validators_returned)
        )

        worker_issorted = multiprocessing.Process(
            name='is_sorted', target=is_sorted, args=(list_to_check, is_ascending, validators_returned)
        )

        jobs.extend([worker_checkints, worker_issorted])
        for proc in jobs:
            proc.start()
        for proc in jobs:
            proc.join()

        # check if all assertions returned True, if not then it means, that at least one AssertionError was thrown
        if not all(validators_returned):
            exit()
    else:
        # check if list has integers only
        assert integers_only(list_to_check) is True

        # check if list is sorted properly
        assert is_sorted(list_to_check, is_ascending) is True

