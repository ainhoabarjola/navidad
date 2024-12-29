def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else '.' for num in fila))
    print()

def es_valido(tablero, fila, columna, num): #Verifica si es válido colocar 'num' en la posición (fila, columna).
    # Verificar la fila
    if num in tablero[fila]:
        return False
    
    # Verificar la columna
    if num in (tablero[i][columna] for i in range(9)):
        return False
    
    # Verificar el subcuadrante 3x3
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == num:
                return False

    return True

def resolver_sudoku(tablero): #Resuelve el Sudoku utilizando el algoritmo de backtracking.
    # Encontrar una celda vacía
    for fila in range(9):
        for columna in range(9):
            if tablero[fila][columna] == 0:
                # Intentar números del 1 al 9
                for num in range(1, 10):
                    if es_valido(tablero, fila, columna, num):
                        tablero[fila][columna] = num
                        if resolver_sudoku(tablero):
                            return True
                        # Retroceso
                        tablero[fila][columna] = 0
                return False  # Si no se encuentra solución, regresar False
    return True  # Sudoku resuelto

# Tablero de Sudoku de ejemplo (0 representa celdas vacías)
tablero_inicial = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Tablero Inicial:")
imprimir_tablero(tablero_inicial)

if resolver_sudoku(tablero_inicial):
    print("Sudoku Resuelto:")
    imprimir_tablero(tablero_inicial)
else:
    print("No se pudo resolver el Sudoku.")
