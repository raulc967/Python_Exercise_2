def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    answer = []
    count = 0
    for item in lst:
        if count % 2 == 0:
            answer.append(item)
        count = count + 1
    return answer

print(remove_every_other([1, 2, 3, 4, 5]))