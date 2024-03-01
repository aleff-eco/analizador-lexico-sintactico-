import ply.yacc as yacc
from ana_lex import tokens

# Gramatica 
def p_sentencia(p):
    '''
    sentencia : variables
                | ciclo_for
                | funcion
                | condicion_c
    '''
    p[0] = True

def p_variables(p):
    '''variables : Declaracion_variable Variable Igual Valor Punto_Y_coma'''
    p[0] = True

def p_ciclo_for(p):
    '''ciclo_for : CicloF Variable IN Variable Dos_puntos Parentesis_apertura Contenido Parentesis_final
                    | CicloF Variable IN Valor Dos_puntos Parentesis_apertura Contenido Parentesis_final'''
    p[0] = True

def p_funcion(p):
    '''funcion : Definicion_funcion Variable Parentesis_apertura Variable Parentesis_final Dos_puntos
                  | Definicion_funcion Variable Parentesis_apertura Parentesis_final Dos_puntos'''
    p[0] = True

def p_condicional(p):
    '''condicion_c : Condicional Parentesis_apertura Variable OPERADORES Variable Parentesis_final Dos_puntos
                     | Condicional Parentesis_apertura Variable OPERADORES Valor Parentesis_final Dos_puntos'''
    p[0] = True


def p_error(p):
    print("Error de sintaxis")
    p[0] = False

# Construcción del parser
parser = yacc.yacc()

# Función para verificar la sintaxis
def verificar(texto):
    try:
        resultado = parser.parse(texto)
        # print("Resultado:", resultado)
        return resultado
    except Exception as e:
        # print("Error:", e)
        return False
