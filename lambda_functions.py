def run():
# Codigo regular:
    # def palindrome(nombre):
    #     if nombre == nombre[::-1]:
    #         print(True)

    # palindrome('ana')

# Código lambda (Funciones anónimas)
    palindrome = lambda string: string == string[::-1]
    print(palindrome("ana"))


if __name__ == "__main__":
    run()