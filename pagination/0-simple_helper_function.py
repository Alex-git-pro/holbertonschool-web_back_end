#!/usr/bin/env python3
"""
Write a function named index_range that takes
two integer arguments page and page_size.
"""


def index_range(page, page_size):
    """The function should return a tuple of size two containing
    a start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.

    Args:
        page : Page Number (1-undexed)
        page_size : Number of items per page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
