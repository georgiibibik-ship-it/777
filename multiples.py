


def check(n: int, a: int, b: int, c: int) -> bool:
    in_range = False
    multiple = False
    if n >= a and n <= b:
        in_range = True
    if c != 0 and n % c == 0:
        multiple = True
    return in_range and multiple


def find_multiples(a: int, b: int, c: int) -> list[int]:
    if c == 0:
        raise ValueError("Делитель c не может быть равен нулю")
    if a > b:
        raise ValueError("Начало диапазона a не должно превышать b")
    return [n for n in range(a, b + 1) if check(n, a, b, c)]


def main() -> int:
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        result = find_multiples(a, b, c)
    except ValueError as error:
        print(f"Ошибка: {error}")
        return 1
    print(" ".join(map(str, result)) if result else "Подходящих чисел нет")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
