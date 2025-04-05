from enteros import enteros
from flotantes import flotantes
from operadores import operadores
from variables import variables
from enum import Enum

class Tokens(str, Enum):
  ENTERO = 'Entero'
  FLOTANTE = 'Flotante'
  OPERADOR = 'Operador'
  VARIABLE = 'Variable'
  OTRO = 'Otro'

def lexerAritmetico(archivo):
  with open(archivo, 'r') as f:
    contenido = f.read()
    tokens: dict[str, Tokens] = []
    current_token: string = ""

    for char in contenido:
      if char.isalnum() or char in ".+-eE=*/^":
        current_token += char
      else:
        if current_token:
          if enteros.accepts(current_token):
            tokens.append({ current_token: Tokens.ENTERO })
          elif flotantes.accepts(current_token):
            tokens.append({ current_token: Tokens.FLOTANTE })
          elif operadores.accepts(current_token):
            tokens.append({current_token: Tokens.OPERADOR })
          elif variables.accepts(current_token):
            tokens.append({current_token: Tokens.VARIABLE })
          current_token = ""

    if current_token:
      if enteros.accepts(current_token):
        tokens.append({current_token: Tokens.ENTERO})
      elif flotantes.accepts(current_token):
        tokens.append({current_token: Tokens.FLOTANTE})
      elif operadores.accepts(current_token):
        tokens.append({current_token: Tokens.OPERADOR})
      elif variables.accepts(current_token):
        tokens.append({current_token: Tokens.VARIABLE })

    print("TOKEN\t\tTIPO")
    for token in tokens:
      for key, value in token.items():
        print(f"{key}\t\t{value.value}")

lexerAritmetico('tarea3/prueba.txt')