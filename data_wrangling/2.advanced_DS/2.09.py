fd = open('../datafiles/data_temporary_files.txt', 'r')
for line in fd.readlines():
    for word in line:
        print(word, end='')
fd.close()

with open('../datafiles/AA.txt', 'rb') as f:
    for line in f.readline():
        print(line, end='')

