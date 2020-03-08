import re


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""

    text = re.sub("\n", " ", text)
    sentences = re.findall(
        r"""[A-Z]       # A sentences starts with [A-Z]
        [A-Za-z]*\b     # the subsequent letters should complete the first word
        \w*\b           # a second word must follow (ending with word end "\b")
        .+?[.?!]        # the sentence contains at least one more word ".+"
        \s(?![a-z])     # ends (non-greedy = ?) with a punctuation which is followed by a space (to exclude abbreviations) and a capital letter (not lower case)
        """,
        text,
        re.DOTALL | re.VERBOSE,
    )

    return [sentence.strip() for sentence in sentences]
