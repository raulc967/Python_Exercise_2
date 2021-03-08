def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    length = len(a[2]) + len(b[2])
    a_set = set(a[2])
    b_set = set(b[2])
    answer = a_set.union(b_set)
    if len(answer) == length:
        return False
    return True

elmo = ('Elmo', 5, ['hugging', 'being nice'])
gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])
print(friend_date(elmo, gandalf))