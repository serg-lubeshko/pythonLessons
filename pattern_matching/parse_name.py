# Распаковка в case


def parse_name(value: str | tuple | dict | list):
    """
    1. Распаковка list, tuple они равнозначны (присваение surname, name, second_name)
    ожидается последовательность (кроме строки и байтов), но не set или dict
    2. case surname, name, second_name можно записать case (surname, name, second_name)
    3. case str() это проверка типа !!! и затем выполняется только if len(value.split()) == 3!!!
    4. !!! При проверке слова ljря неважно сколько ключ-значений, проверяется  последовательность, указанная в case
    5. Переменные surname, name, second_name доступны не только в local scope, но и вне. Пример 2


    """
    match value:
        case surname, name, second_name:
            return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"
        case {'surname': surname, "name": name, "second_name": second_name} if len(value) == 3:  # if len(value) ==3:
            return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"
        case str() if len(value.split()) == 3:
            surname, name, second_name = value.split()
            return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"
        case _:
            return "Error"

#example_2

def parse_name2(value: str | tuple | dict | list):
    match value:
        case surname, name, second_name:
            pass
        case {'surname': surname, "name": name, "second_name": second_name} if len(value) == 3:  # if len(value) ==3:
            pass
        case str() if len(value.split()) == 3:
            surname, name, second_name = value.split()
            pass
        case _:
            return "Error"
    return f"Фамилия: {surname}, Имя: {name}, Отчество: {second_name}"


if __name__ == '__main__':
    assert parse_name2(("Иванов", "Иван", "Иванович")) == "Фамилия: Иванов, Имя: Иван, Отчество: Иванович"
    assert parse_name(["Иванов", "Иван", "Иванович"]) == "Фамилия: Иванов, Имя: Иван, Отчество: Иванович"
    assert parse_name({'surname': "Иванов",
                       'name': "Иван",
                       'second_name': "Иванович",
                       }) == "Фамилия: Иванов, Имя: Иван, Отчество: Иванович"
    assert parse_name("Иванов Иван Иванович") == "Фамилия: Иванов, Имя: Иван, Отчество: Иванович"
    assert parse_name(["Иванов", "Иванович"]) == "Error"
    assert parse_name(("Иванов", "Иван", "Иванович", "Иванович")) == "Error"
    assert parse_name({'a': "Иванов",
                       'b': "Иван",
                       'c': "Иванович",
                       }) == "Error"
    assert parse_name("Иванов Иван Иванович 1222") == "Error"
    assert parse_name({'surname': "Иванов",
                       'second_name': "Иванович",
                       'name': "Иван",
                       'salary': 50000,
                       }) == "Error"
