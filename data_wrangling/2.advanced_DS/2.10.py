with open('../datafiles/AA.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        for word in line:
            print(word, end='')