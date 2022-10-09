def parse_request(value):
    match value:
        case {'key': 1000, **rest}:
            return rest['id']
        case ('error', message) | ('error', message,
                                   *_):  # можем принять 2 типа шаблонов. Переменные тогда в шаблоне должны быть одноименны
            raise ValueError(message)
        case {'meta': val, **rest} if not rest:
            return val['id']
        case {'meta': {'code': _, 'error': error},
              'info': [{'allowed': allowed},
                       _]}:  # список проверяется строго в данном случае, но [{'allowed': allowed}, *_]} любок количество элементов
            return f"{error}, {allowed}"
        case (set() as x, _) if len(x) == 2: # set() as x == set(x)
            return max(x)
        case _:
            raise ValueError(f"Unknown value: {value}")


if __name__ == '__main__':
    first = {'key': 1000, 'id': 999}  # Если поменять 'key' на 1100 сработает wildcard
    second = ['error', 'Slow connection']
    third = {'meta': {'id': 9000}}
    fourth = {'meta': {'code': 200, 'error': 'no'}, 'info': [{'allowed': 'yes'}, 1111]}
    fifth = ({10, 11}, 5)
    print(parse_request(third))
