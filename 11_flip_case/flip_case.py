def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    answer = []
    if to_swap.isupper() == True:
        low = to_swap.lower()
        for letter in phrase:
            if letter == low:
                answer.append(letter.upper())
            elif to_swap == letter:
                answer.append(letter.lower())
            else:
                answer.append(letter)
        return ''.join(answer)
    elif to_swap.islower() == True:
        up = to_swap.upper()
        for letter in phrase:
            if letter == up:
                answer.append(letter.lower())
            elif to_swap == letter:
                answer.append(letter.upper())
            else:
                answer.append(letter)
        return ''.join(answer)

print(flip_case('Aaaahhh', 'h')) 