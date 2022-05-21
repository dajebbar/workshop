dict_1 = {
    "key1": 1, 
    "key2": ["list_element1", 34],
    "key3": "value3",
    "key4": {"subkey1": "v1"},
    "key5": 4.5
}

print(dict_1)

del dict_1["key2"]
print(dict_1)

del dict_1["key3"]
del dict_1["key4"]
print(dict_1)