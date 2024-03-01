import ply.lex as lex

tokens = (
    'Declaracion_variable',
    'Condicional',
    'CicloF',
    'IN',
    'Definicion_funcion',
    'Punto_Y_coma',
    'Mayor_que',
    'Menor_que',
    'Menor_o_igual',
    'Mayor_o_igual',
    'Dos_puntos',
    'Igual',
    'Valor',
    'Igual_igual',
    'Numero',
    'Contenido',
    'Parentesis_apertura',
    'Parentesis_final',
    'Variable',  
    'Espacios', 
    'ERROR',  
    'OPERADORES',
    'NUMBER'
)

t_Punto_Y_coma = r';'
t_Dos_puntos = r':'
t_Igual = r'='
t_Igual_igual = r'=='
t_Mayor_que = r'>'
t_Menor_que = r'<'
t_Mayor_o_igual = r'>='
t_Menor_o_igual = r'<='
t_Parentesis_apertura = r'\('
t_Parentesis_final = r'\)'
t_OPERADORES = r'==|>=|<=|>|<'
t_NUMBER = r"\d+"

lexema = []

def t_Declaracion_variable(t):
    r'\bVAR\b'
    return t

def t_Condicional(t):
    r'\bIF\b'
    return t

def t_Definicion_funcion(t):
    r'\bDEF\b'
    return t

def t_CicloF(t):
    r'\bFOR\b'
    return t

def t_IN(t):
    r'IN\b'
    return t

def t_Valor(t):
    r'(-?\d+\.\d+)|(\d+)|("[^"]+")'
    return t

def t_Numero(t):
    r'\b\d+\b'  
    return t

def t_Contenido(t):
    r'\bC\b'
    return t

def t_Variable(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    keywords = {'IN', 'range', 'print'}
    if t.value.upper() in keywords:
        t.type = t.value.upper() 
    return t

def t_Espacios(t):
    r'\s+'
    pass


def analisis(data):
    global lexema

    analizador = lex.lex()
    analizador.input(data)
    
    lexema.clear()
    has_invalid_token = False

    while True:
        token = analizador.token()
        if not token:
            break
        if token.type == 'ERROR':
            has_invalid_token = True
        estado = "{:16} {:16} {:4}".format(str(token.type), str(token.value), str(token.lexpos))

        lexema.append(estado)
    
    return not has_invalid_token, lexema
       

def t_error(t):
    global lexema
    estado = "ERROR {:16} {:4}".format(str(t.value), str(t.lexpos))
    lexema.append(estado)
    t.lexer.skip(1)