import itertools


def header_line(header, line):
    itertools.zip_longest(header, line, fillvalue=None)
