from traceback import print_tb


def run():
# Codigo regular:
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

# Código con dict comprehensions:

    # my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}

    # print(my_dict)

# Reto
#Crear un dictionary comprehension, un diccionario cuyas llaves sean los 100 primeros números naturales con sus raíces cuadradas como valores

#Solución 1:
    my_dict = {i: round(i**0.5,2) for i in range(1,1001)}
    print(my_dict)

#Solución 2:
    # from math import sqrt
    # my_dict = {i:round(math.sqrt(i), 2) for i in range (1, 1001)}
    # print(my_dict)

if __name__ == '__main__':
    run()