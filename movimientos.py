tablero = [
['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
[' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
]

def tablero_a_cadena(tablero):
    """
    (list of str) -> str
    recibimos un tablero o diccionario y devolvemos una cadena
    :param tablero: el tablero con la posicionde cada ficha
    :return: dict el tablero con la nueva posicion de las fichas
    """

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

def mover_peon(tablero,x_inicial,y_inicial,x_final,y_final):
    '''
    ([][],int,int,int,int)-> [][]: tablero resultante del movimiento de un peon.
    :param tablero: [][]: matriz con la posicion de las fichas
    :param x_inicial: int: entero indocando posicion en x inicial
    :param y_inicial: int: entero indocando posicion en y inicial
    :param x_final: int: entero indocando posicion en x final
    :param y_final: int: entero indocando posicion en y final
    :return: [][] tablero resultante
    '''

    ficha = tablero[x_inicial][y_inicial]
    peon = 'pP'
    if (ficha not in peon):
        raise TypeError('no es un peon')

    ultima_posicion = tablero[x_final][y_final]
    have_to_eat = False
    team = ficha.islower()
    team2 = False
    if (ultima_posicion != ' '):
        team2 = ultima_posicion.islower()
        if (team == team2):
            raise TypeError('camino bloqueado')
    if(x_final>x_inicial and team):
        x_diferencia = x_final - x_inicial
    elif(x_final<x_inicial and team2):
        x_diferencia = x_inicial-x_final
    else:
        return 'movimiento invalido'

    maxmov = 0
    if x_inicial == 1 or x_inicial == 6:
        maxmov = 2
    else:
        maxmov = 1

    if x_diferencia>2 or x_diferencia>maxmov:
        return 'movimiento_invalido'


    try:
        for fila in range(x_inicial, x_final):
            if (x_inicial == x_final):
                break
            if fila==x_inicial:
                continue
            elif fila != x_inicial and tablero[fila][y_inicial] != ' ' and x_diferencia!=2:
                have_to_eat = True
                tablero[fila][y_inicial] = ficha
                break
            elif fila != x_inicial and tablero[fila][y_inicial] == ' ' and x_diferencia == 2:
                return 'movimiento invalido'




        for columna in range(y_inicial, y_final):
            if (y_inicial == y_final):
                break
            elif columna != y_inicial and columna != y_final and tablero[x_inicial][columna] != ' ':
                return 'camino bloqueado'

        tablero[x_final][y_final] = ficha
        tablero[x_inicial][y_inicial] = ' '

        tablero = tablero_a_cadena(tablero)
    except:
        TypeError('la posicion esta fuera del tablero')

    return tablero;


def mover_torre(tablero, x_inicial, y_inicial, x_final, y_final):
    '''
    ([][],int,int,int,int)-> [][]: tablero resultante del movimiento de una torre.
    :param tablero: [][]: matriz con la posicion de las fichas
    :param x_inicial: int: entero indocando posicion en x inicial
    :param y_inicial: int: entero indocando posicion en y inicial
    :param x_final: int: entero indocando posicion en x final
    :param y_final: int: entero indocando posicion en y final
    :return: [][] tablero resultante
    '''

    ficha =  tablero[x_inicial][y_inicial]
    torre = 'tT'
    if (ficha not in torre):
        return 'no es una torre'

    ultima_posicion = tablero[x_final][y_final]
    team = ficha.islower()
    team2= False
    if (ultima_posicion != ' '):
        team2 = ultima_posicion.islower()
        if(team==team2):
            return 'camino bloqueado'

    if x_inicial!=x_final and y_inicial!=y_final:
       return 'movimiento invalido'
    try:
        for fila in range(x_inicial,x_final):
            if(x_inicial == x_final):
                break
            elif fila != x_inicial and fila != x_final and tablero[fila][y_inicial] != ' ':
                return 'camino bloqueado'

        for columna in range(y_inicial,y_final):
            if (y_inicial == y_final):
                break
            elif columna != y_inicial and columna != y_final and tablero[x_inicial][columna] != ' ':
                return 'camino bloqueado'
    except:
        TypeError('la posicion no existe en el tablero')


    tablero[x_final][y_final] = ficha
    tablero[x_inicial][y_inicial] = ' '

    tablero = tablero_a_cadena(tablero)

    return tablero;


def mover_caballo(tablero, x_inicial, y_inicial, x_final, y_final):
    if (0 < x_final <= 7) and (0 < y_final <= 7):
        esCaballo = True
        esCaballo = tablero[x_inicial][y_inicial] in 'kK'
        restaEnX = -(x_inicial - x_final)
        restaEnY = -(y_inicial - y_final)
        posicionInicial = tablero[x_inicial][y_inicial].islower()
        posicionFinal = tablero[x_final][y_final].islower()
        resultadoMovimiento = tablero

        if (esCaballo):
            if (restaEnX == 2 and restaEnY == 1) or (restaEnX == 1 and restaEnY == 2):
                if (posicionInicial == posicionFinal):
                    print('Ficha amiga.')
                else:
                    resultadoMovimiento[x_final][y_final] = resultadoMovimiento[x_inicial][y_inicial]
                    resultadoMovimiento[x_inicial][y_inicial] = ' '
                    print(tablero_a_cadena(resultadoMovimiento))
            else:
                print('Movimiento invalido.')
        else:
            print('No es un caballo.')
    else:
        print('Posición final no valida.')


def mover_rey(tablero,x_inicial,x_final,y_inicial, y_final):
    """
    Funcion que define el movimiento del rey
    :param tablero:
    :param x_inicial:
    :param x_final:
    :param y_inicial:
    :param y_final:
    :return:
    """

    pass

    esRey = None
    auxiliar_x = x_final

    #Validar si es rey
    if (x_inicial == x_final or y_inicial == y_final):
        esRey = tablero[x_inicial][y_inicial] in 'Rr'

        #Validar si el movimiento en x es mayor a una casilla
        if auxiliar_x != x_final + 1:

            #Valida si la posicion en y es vacia
            if esRey:
                for x in range(x_inicial + 1, x_final):
                    if (tablero[x][y_final] != ''):
                        for y in range (y_inicial, y_final):
                            print([x_inicial],[y])
                    else:
                        raise ValueError("El camino esta bloqueado")
            else:
                print('No es un rey')
        else:
            raise ValueError("El movimiento no es válido")

    else:
        raise ValueError('No es un rey')


    #Validamos si en el movimiento final hay un aliado o enemigo
    if esRey == 't':
        if tablero[x_final][y_final] == 't':
            raise ValueError('No puedo matar aliados')

        if esRey:
            for x in range(x_inicial + 1, x_final):
                if (tablero[x][y_final] == ''):
                    for y in range (y_inicial, y_final):
                        print([x_inicial],[y])
                else:
                    raise ValueError("El camino esta bloqueado")

                    break

        else:
            esRey == tablero[x_final][y_final]

    else:
        if tablero[x_final][y_final] == 'T':
            raise ValueError('No puedo matar aliados')
        else:
            esRey == tablero[x_final][y_final]


def mover_alfil(tablero, x_inicial, y_inicial, x_final, y_final):
    """
    (list of list, int, int, int, int) -> list of list
    :param tablero: list of list que representa el tablero
    :param x_inicial: int que representa la posicion inicial en X
    :param y_inicial: int que representa la posicion inicial en Y
    :param x_final: int que representa la posicion final en X
    :param y_final: int que representa la posicion final en Y
    :return: list of list que representa un tablero final
    """
    if (0 < x_final <= 7) and (0 < y_final <= 7):
        esAlfil = tablero[x_inicial][y_inicial] in 'aA'
        deltaX = abs(x_final - x_inicial)
        deltaY = abs(y_final - y_inicial)
        ficha = tablero[x_inicial][y_inicial]
        colorFicha = tablero[x_inicial][y_inicial].islower()

        if (esAlfil):
                if (deltaX == deltaY):
                    if (x_inicial != x_final and y_inicial != y_final):
                        mov_y = y_inicial + 1
                        for mov_x in range(x_inicial + 1, x_final + 1):
                            if (tablero[mov_x][mov_y] == ' '):
                                tablero[mov_x][mov_y] = ficha
                                tablero[x_inicial][y_inicial] = ' '
                                mov_y = mov_y + 1
                                continue
                            else:
                                if (colorFicha != tablero[mov_x][mov_y].islower()):
                                    tablero[mov_x][mov_y] = ficha
                                    tablero[x_inicial][y_inicial] = ' '
                                    break
                                else:
                                    print('Camino bloqueado por ficha aliada.')
                                    break
                    else:
                        print('No se ha movido el alfil')
                else:
                    print('Movimiento invalido. El alfil se debe mover en diagonal')
        else:
            print('La ficha no es un alfil.')
    else:
        print('Posición final fuera del tablero.')