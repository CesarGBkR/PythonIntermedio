from dict_comprehensions import run


def run():
#Crea una lista a partir de los numeros dentro de una lista ya dada, donde solo ingreses aquellos numeros NO pares

    #Solución con List comprehensions
    # my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    # odd = [i for i in my_list if i %2 != 0]
    # print(odd)

    #Solución con filter
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]

    odd = list(filter(lambda x: x%2 != 0, my_list))
    print(odd)

#Crear una lista con los valores al cuadrado de una lista ya dada

    #Solución con List comprehensions
    # my_list2 =  [1,2,3,4,5]
    # ood =  [i * i for i in my_list2]
    # print(ood)

    #Solución con map
    my_list2 =  [1,2,3,4,5]
    square = list(map(lambda x: x**2, my_list2))
    print(square)

if __name__ == '__main__':
    run()
    