import matplotlib.pyplot as plt
plt.style.use('ggplot')


people = ['Ann','Brandon','Chen','David','Emily',
        'Farook','Gagan','Hamish','Imran','Joseph',
        'Katherine','Lily']
age = [21,12,32,45,37,18,28,52,5,40,48,15]
weight = [55,35,77,68,70,60,72,69,18,65,82,48]
height = [160,135,170,165,173,168,175,159,105,171,155,158]

# age versus weight

plt.scatter(x=age, y=weight)
plt.title('Age vs weight')
plt.xlabel('Age')
plt.ylabel('Weight')

plt.show()