import math



def cos():
    return lambda x: math.cos(math.radians(x))

def sin():
    return lambda x: math.sin(math.radians(x))

sine = sin()
cosine = cos()

print(sine(30)**2 + cosine(30)**2)