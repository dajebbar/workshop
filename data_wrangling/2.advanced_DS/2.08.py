import os


os.environ['MY_KEY'] = 'MY_VAL'
my_key = os.getenv('MY_KEY')
print(my_key)
print(os.getenv('MY_KEY_NOT_SET'))