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


if __name__ == '__main__':
    run()
    