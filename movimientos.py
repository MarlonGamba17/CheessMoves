def tablero_a_cadena(tablero):
    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena


def obtener_nombre_pieza(simbolo):
    """
    (str) -> str

    >>> obtener_nombre_pieza('p')
    'Peon blanco'
    >>> obtener_nombre_pieza('R')
    'Rey Negro'

    Retorna el nombre de la pieza del ajedrez dado su simbolo

    :param simbolo: la representacion de la pieza segun el enunciado
    :return: El nombre y color de la pieza
    """
    tipo = 'Negro'
    if simbolo.islower():
        tipo = 'blanco'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'Peon '+tipo
    elif retorno == 't':
        return 'Torre ' + tipo
    elif retorno == 'k':
        return 'Caballo ' + tipo
    elif retorno == 'a':
        return 'Alfil ' + tipo
    elif retorno == 'q':
        return 'Reina ' + tipo
    elif retorno == 'r':
        return 'Rey ' + tipo
    else:
        return 'No es una pieza'

def mover_torre(tablero, x_inicial, y_inicial, x_final, y_final):
    '''
    ([][],int,int,int,int)-> [][]: tablero resultante.
    :param tablero: [][]: matriz con la posicion de las fichas
    :param x_inicial: int: entero indocando posicion en x inicial
    :param y_inicial: int: entero indocando posicion en y inicial
    :param x_final: int: entero indocando posicion en x final
    :param y_final: int: entero indocando posicion en y final
    :return: [][] tablero resultante
    '''

    ficha =  tablero[x_inicial][y_inicial]

    x_diferencia =  x_final- x_inicial
    y_diferencia = y_final - y_inicial

    cont_filas = 0
    cont_columnas = 0
    for fila in range(x_inicial,x_final):
        if(x_inicial == x_final):
            break
        if fila != x_inicial and fila != x_final and tablero[fila][y_inicial] != ' ':
            return 'camino bloqueado'
        if fila == x_final:
            tablero[fila][y_inicial] = tablero[x_inicial,x_final]

    for columna in range(y_inicial,y_final):
        if(tablero[x_inicial][columna])!= ' ':
            return 'camino bloqueado'



    if (ficha != 't'):
        return 'no es una torre'
print(mover_torre(tablero, 1, 1, 2, 2))
