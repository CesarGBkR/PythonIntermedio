def divisors(num):
    divisors = []
    try:
        if num < 0 or num == 0:
            raise ValueError("No se pueden ingresar números negativos ni cero")
        for i in range(1, num + 1 ):
            if num %i == 0:
                divisors.append(i)
        return divisors
        
    except ValueError as ve:
        return ve

def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Fin del programa")
    except ValueError as ve:
        print("Debes ingresar un número")
if __name__ =='__main__':
    run()