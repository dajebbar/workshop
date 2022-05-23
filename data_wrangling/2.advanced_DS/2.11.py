data_dict = {
    'Morocco': 'Rabat',
    'Italy': 'Rome',
    'Spain': 'Madrid',
}

with open('../datafiles/data_temporary_files.txt', 'a') as f:
    for country, capital in data_dict.items():
        f.write(f'The capital of {country} is {capital}\n')


with open('../datafiles/data_temporary_files.txt', 'r') as f:
    for line in f.readlines():
        for word in line:
            print(word, end='')