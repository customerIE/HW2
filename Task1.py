import fractions


# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.
def convert_number(num: int, mode: str) -> str:
    result = ''
    convert: int = 16
    while num >= 1:
        res = num % convert
        if convert == 16:
            if res == 10:
                res = 'a'
            if res == 11:
                res = 'b'
            if res == 12:
                res = 'c'
            if res == 13:
                res = 'd'
            if res == 14:
                res = 'e'
            if res == 15:
                res = 'f'
        result += str(res)
        num = num // convert
    return result[::-1]

print(convert_number(423, mode="hex"), f"assert: {hex(21)}")
