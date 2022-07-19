import os
PATH_FILE = os.path.dirname(__file__)

def read():
    numbers = []
    with open(f"{PATH_FILE}/archivos/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
def write():
    names = ["Facundo", "Miguel", "Cesar"]
    with open("{PATH_FILE}/archivos/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
def run():
    pass


if __name__ == '__main__':
    run() 