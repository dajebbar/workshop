import itertools


def header_line(header, line):
    zipped_line = itertools.zip_longest(header, line, fillvalue=None)
    dico = {k[0]:k[-1] for k in zipped_line}
    return dico


with open('../../datafiles/sales_record.csv', 'r') as f:
    first_line = f.readline()
    header = first_line.replace("\n", "").split(",")
    for i, line in enumerate(f):
        # Here we loop over the first 10 lines in order to not to make the output too big
        line = line.replace("\n", "").split(",")
        d = header_line(header, line)
        print(d)
        if i > 10:
            break