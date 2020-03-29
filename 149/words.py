def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    sorted_words = []

    words_starting_with_digits = []

    for word in words:
        if not word[0].isdigit():
            sorted_words.append(word)
        else:
            words_starting_with_digits.append(word)
    
    sorted_words = sorted(sorted_words, key=str.lower)

    for word in sorted(words_starting_with_digits):
        sorted_words.append(word)
    
    return sorted_words
