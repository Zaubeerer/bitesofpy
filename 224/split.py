import re


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""

    text = re.sub("\n", " ", text)
    sentences = re.findall(
        r"""[A-Z][A-Za-z]*\b\w*\b.+?[.?!] (?![a-z])""", text, re.DOTALL
    )

    return [sentence.strip() for sentence in sentences]
