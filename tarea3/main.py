from enteros import enteros
from flotantes import flotantes
from operadores import operadores
from enum import Enum

class Tokens(str, Enum):
  ENTERO = 'Entero'
  FLOTANTE = 'Flotante'
  OPERADOR = 'Operador'
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
          current_token = ""

        if not char.isspace():
          tokens.append({ char: Tokens.OTRO })


    if current_token:
      if enteros.accepts(current_token):
          tokens.append({current_token: Tokens.ENTERO})
      elif flotantes.accepts(current_token):
          tokens.append({current_token: Tokens.FLOTANTE})
      elif operadores.accepts(current_token):
          tokens.append({current_token: Tokens.OPERADOR})
      else:
          tokens.append({current_token: Tokens.OTRO})

    print("TOKEN\t\tTIPO")
    for token in tokens:
      for key, value in token.items():
        print(f"{key}\t\t{value.value}")

lexerAritmetico('tarea3/prueba.txt')