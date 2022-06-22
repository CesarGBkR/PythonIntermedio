def run():

#Código regular:
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)
    #         print(squares)

# Código usando Comprehensions:
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(squares)

# Reto
#Crear un list comprehension, una lista de todos lo múltiplos de 4 que A SU VEZ  son múltiplos de 6 y de 9

    listaReto = [ i for i in range(1, 10000) if i % 36 == 0] # Reducimos ANDs encontrando el mínimo común múltiplo de los multiplos requeridios
    print(listaReto)


if __name__ ==  "__main__":
    run()