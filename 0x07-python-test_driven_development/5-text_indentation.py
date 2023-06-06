#!/usr/bin/python3
"""Write imported module here"""


def text_indentation(text):
    """Function that adds two new lines when it finds these characters in a string: ., :, and ?

    Args:
        text: the string to print

    Raises:
        TypeError: if the text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join([line.strip(" ") for line in text.split(char)])
    print(text, end="")


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/5-text_indentation.txt")
