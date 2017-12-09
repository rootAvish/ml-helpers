#!/usr/bin/env python3


def contains_all_packages(haystacks, *args):
    """Returns a tuple containing list of index of all haystacks
    that contains all elements in *args, and one not containing them.

    :param haystacks: A list of lists where each list is a haystack
    :param *args: The packages that should/shouldn't occur together
    """
    packages_to_find = set(list(args))
    return ([haystack for haystack in haystacks
             if not packages_to_find.issubset(set(haystack))],
            [haystack for haystack in haystacks
             if packages_to_find.issubset(set(haystack))])
