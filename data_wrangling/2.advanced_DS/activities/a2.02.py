import itertools


def header_line(header, line):
    itertools.zip_longest(header, line, fillvalue=None)


with open('../../datafiles/sales_record.csv', 'r') as f:
    header = ''
    for line in f.readlines()[0][:-1]:
        header += line
        # for word in line:
        #     header.append(word)
    
    print(header.split(','))