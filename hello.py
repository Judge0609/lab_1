def calculate_grundy(n, k, board):
    # Ініціалізація масиву гранді-чисел
    grundy = [0] * (n + 1)

    # Обчислення гранді-чисел
    for i in range(1, n + 1):
        mex = set()
        for j in range(max(0, i - k), i):
            mex.add(grundy[j])
        grundy[i] = calculate_mex(mex)

    # Визначення гранді-числа для початкової позиції
    result = 0
    for i in range(n):
        if board[i] == 'O':
            result ^= grundy[i + 1]

    return result

# Обчислення мінімального непозитивного цілого числа
def calculate_mex(s):
    mex = 0
    while mex in s:
        mex += 1
    return mex

# Зчитуємо вхідні дані
n, k = map(int, input().split())
board = input()

# Визначення результату за методом Шпрага-Гранді
result = calculate_grundy(n, k, board)
if result != 0:
    print(1)
else:
    print(2)
