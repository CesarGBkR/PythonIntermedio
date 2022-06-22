def run():
    my_list = [1, "Hello", True, 4.5]
    my_dic = {"firstName": "Cesar", "lastName": "Garduñó" }

    superList = [
        {"firstName": "Cesar", "lastName": "Garduñó" },
        {"firstName": "Miguel", "lastName": "Antonio" },
        {"firstName": "Pepe", "lastName": "Rodelo" },
        {"firstName": "Susana", "lastName": "Rodelo" },
        {"firstName": "Jose", "lastName": "Garcia" },
    ]

    superDict = {
        "natualNums": [1,2,3,4,5],
        "integerNums": [-1,-2,0,1,2],
        "floatinglNums": [1.1,4.5,6.43]
    }


    for key, value in superDict.items():
        print(key, "-", value)

    for value in superList:
        for key, value in value.items():
            print(f'{key} - {value}')
if __name__ == '__main__':
    run()