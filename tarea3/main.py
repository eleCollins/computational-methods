from enteros import enteros
from enum import Enum

class Tokens(str, Enum):
  ENTERO = 'Entero'
  FLOTANTE = 'Flotante'

def lexerAritmetico(archivo):
  with open(archivo, 'r') as f:
    contenido = f.read()

    tokens: dict[str, Tokens] = []
    strings = contenido.split()
    for string in strings:
      if (enteros.accepts(string)):
        tokens.append({ string: Tokens.ENTERO })
      else if ():
        tokens.append({ string: Tokens.FLOTANTE })

    print(tokens)


lexerAritmetico('tarea3/prueba.txt')