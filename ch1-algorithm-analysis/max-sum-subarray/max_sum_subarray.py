from typing import Iterable


def max_sum_subarray_slow(a: Iterable[int]) -> int:
    """
    max_sum_subarray_slow  is a naive implementation of the Max Sum Subarray
    Problem, running in O(n^3) time by enumerating all n^2 possible
    subarrays and summing the m elements of each of those subarrays
    """
    # the base case subarray is empty with sum 0
    max = 0
    for start_index in range(len(a)):
        # we will enumerate all subarrays that start at index 0,
        # then all subarrays that start at index 1, etc...
        for end_index in range(start_index, len(a)):
            # when start index is 0, we make subarrays a[0..0] up to a[0..len(a) - 1]
            # when start index is 1, we make subarrays a[1..1] up to a[1..len(a) - 1]
            # and so on. There is no need to "look back" from a start index of 1
            # to cover the subarray a[1..0] because a[0..1] was already covered on the
            # previous outer loop iteration and order of elements does not matter
            sub_array_sum = sum(a[start_index : end_index + 1])
            # sum all elements a[start index...end index]
            if sub_array_sum > max:
                max = sub_array_sum
    return max