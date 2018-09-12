import random


def calculate_main_diagonal(m):
    result = 0
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if i == j:
                result += col
    return result


def show_matrix(m):
    for row in m:
        print(row)


def generate_matrix(n, m):
    return [[random.randint(1, 10) for _m in range(m)] for _n in range(n)]


def main():
    s = int(input('Introduzca el tamaño de la matriz (NxN): '))
    matrix = generate_matrix(s, s)
    main_diagonal = calculate_main_diagonal(matrix)
    show_matrix(matrix)
    print('La suma es: ' + str(main_diagonal))


if __name__ == '__main__':
    main()
