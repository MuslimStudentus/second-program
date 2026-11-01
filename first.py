LENGTH = {"м": 1, "км": 1000, "см": 0.01, "миля": 1609.34}
MASS = {"кг": 1, "г": 0.001, "т": 1000, "фунт": 0.453592}


def convert_table(value, src, dst, table):
    return value * table[src] / table[dst]


def convert_temp(value, src, dst):
    celsius = value if src == "C" else (value - 32) * 5 / 9
    return celsius if dst == "C" else celsius * 9 / 5 + 32


def read_number():
    while True:
        text = input("Число: ").replace(",", ".")
        try:
            return float(text)
        except ValueError:
            print("Введите число")


def read_unit(units, label):
    while True:
        name = input(f"{label} ({', '.join(units)}): ")
        if name in units:
            return name
        print("Такой единицы нет")


def main():
    print("Категории: 1 - длина, 2 - масса, 3 - температура")
    kind = input("Выберите: ")
    tables = {"1": LENGTH, "2": MASS, "3": ["C", "F"]}
    if kind not in tables:
        print("Неверная категория")
        return
    units = tables[kind]
    value = read_number()
    src = read_unit(units, "Из")
    dst = read_unit(units, "В")
    if kind == "3":
        result = convert_temp(value, src, dst)
    else:
        result = convert_table(value, src, dst, units)
    print(f"{value} {src} = {result:.4g} {dst}")


if __name__ == "__main__":
    main()