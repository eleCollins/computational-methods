from enteros import enteros
from flotantes import flotantes
from operadores import operator_dfas  # Updated import
from variables import variables
from parentesis import parentesis_izq, parentesis_der
from enum import Enum

class Tokens(str, Enum):
    ENTERO = 'Entero'
    FLOTANTE = 'Flotante'
    VARIABLE = 'Variable'
    PARENTESIS_IZQ = 'Paréntesis que abre'
    PARENTESIS_DER = 'Paréntesis que cierra'
    IGUAL = 'Asignación'
    MAS = 'Suma'
    MENOS = 'Resta'
    MULTIPLICACION = 'Multiplicación'
    DIVISION = 'División'
    POTENCIA = 'Potencia'
    OTRO = 'Otro'

def lexerAritmetico(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        tokens: list[dict[str, Tokens]] = []
        current_token: str = ""

        for char in contenido:
            if char in "()":  # Check for parentheses first
                if current_token:  # Process the current token before handling the parenthesis
                    if enteros.accepts(current_token):
                        tokens.append({current_token: Tokens.ENTERO})
                    elif flotantes.accepts(current_token):
                        tokens.append({current_token: Tokens.FLOTANTE})
                    elif variables.accepts(current_token):
                        tokens.append({current_token: Tokens.VARIABLE})
                    elif operator_dfas['='].accepts(current_token):
                        tokens.append({current_token: Tokens.IGUAL})
                    elif operator_dfas['+'].accepts(current_token):
                        tokens.append({current_token: Tokens.MAS})
                    elif operator_dfas['-'].accepts(current_token):
                        tokens.append({current_token: Tokens.MENOS})
                    elif operator_dfas['*'].accepts(current_token):
                        tokens.append({current_token: Tokens.MULTIPLICACION})
                    elif operator_dfas['/'].accepts(current_token):
                        tokens.append({current_token: Tokens.DIVISION})
                    elif operator_dfas['^'].accepts(current_token):
                        tokens.append({current_token: Tokens.POTENCIA})
                    current_token = ""

                # Tokenize the parenthesis
                if parentesis_izq.accepts(char):
                    tokens.append({char: Tokens.PARENTESIS_IZQ})
                elif parentesis_der.accepts(char):
                    tokens.append({char: Tokens.PARENTESIS_DER})
            elif char.isalnum() or char in ".+-eE=*/^":  # Continue building the current token
                current_token += char
            else:  # Handle other characters
                if current_token:
                    if enteros.accepts(current_token):
                        tokens.append({current_token: Tokens.ENTERO})
                    elif flotantes.accepts(current_token):
                        tokens.append({current_token: Tokens.FLOTANTE})
                    elif variables.accepts(current_token):
                        tokens.append({current_token: Tokens.VARIABLE})
                    elif operator_dfas['='].accepts(current_token):
                        tokens.append({current_token: Tokens.IGUAL})
                    elif operator_dfas['+'].accepts(current_token):
                        tokens.append({current_token: Tokens.MAS})
                    elif operator_dfas['-'].accepts(current_token):
                        tokens.append({current_token: Tokens.MENOS})
                    elif operator_dfas['*'].accepts(current_token):
                        tokens.append({current_token: Tokens.MULTIPLICACION})
                    elif operator_dfas['/'].accepts(current_token):
                        tokens.append({current_token: Tokens.DIVISION})
                    elif operator_dfas['^'].accepts(current_token):
                        tokens.append({current_token: Tokens.POTENCIA})
                    current_token = ""

                # Check if the character matches any operator DFA
                for operator, dfa in operator_dfas.items():
                    if dfa.accepts(char):
                        tokens.append({char: Tokens(operator)})
                        break

        # Process any remaining token
        if current_token:
            if enteros.accepts(current_token):
                tokens.append({current_token: Tokens.ENTERO})
            elif flotantes.accepts(current_token):
                tokens.append({current_token: Tokens.FLOTANTE})
            elif variables.accepts(current_token):
                tokens.append({current_token: Tokens.VARIABLE})
            elif operator_dfas['='].accepts(current_token):
                tokens.append({current_token: Tokens.IGUAL})
            elif operator_dfas['+'].accepts(current_token):
                tokens.append({current_token: Tokens.MAS})
            elif operator_dfas['-'].accepts(current_token):
                tokens.append({current_token: Tokens.MENOS})
            elif operator_dfas['*'].accepts(current_token):
                tokens.append({current_token: Tokens.MULTIPLICACION})
            elif operator_dfas['/'].accepts(current_token):
                tokens.append({current_token: Tokens.DIVISION})
            elif operator_dfas['^'].accepts(current_token):
                tokens.append({current_token: Tokens.POTENCIA})

        print("TOKEN\t\tTIPO")
        for token in tokens:
            for key, value in token.items():
                print(f"{key}\t\t{value.value}")

lexerAritmetico('tarea3/prueba.txt')