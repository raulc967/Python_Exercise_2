def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    low = phrase.lower()
    no_space = low.replace(' ', '')
    reverse = no_space[::-1]
    if no_space == reverse:
        return True
    else:
        return False

print(is_palindrome("Robert"))