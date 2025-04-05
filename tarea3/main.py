from enteros import enteros
from flotantes import flotantes
from enum import Enum

class Tokens(str, Enum):
  ENTERO = 'Entero'
  FLOTANTE = 'Flotante'
  OTRO = 'Otro'

def lexerAritmetico(archivo):
  with open(archivo, 'r') as f:
    contenido = f.read()
    tokens: dict[str, Tokens] = []
    current_token: string = ""

    for char in contenido:
      if char.isalnum() or char in ".+-eE":  # Characters that can be part of a number
                current_token += char
      else:
        if current_token:
          if enteros.accepts(current_token):
            tokens.append({ current_token: Tokens.ENTERO })
          elif flotantes.accepts(current_token):
            tokens.append({ current_token: Tokens.FLOTANTE })
          current_token = ""

        if not char.isspace():
          tokens.append({ char: Tokens.OTRO })


    if current_token:
      if enteros.accepts(current_token):
          tokens.append({current_token: Tokens.ENTERO})
      elif flotantes.accepts(current_token):
          tokens.append({current_token: Tokens.FLOTANTE})
      else:
          tokens.append({current_token: Tokens.OTRO})


    print(tokens)

lexerAritmetico('tarea3/prueba.txt')