from enteros import enteros
from flotantes import flotantes
from operadores import operator_dfas  # Updated import
from variables import variables
from parentesis import parentesis_izq, parentesis_der
from comentarios import comentarios
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
    COMENTARIO = 'Comentario'
    OTRO = 'Otro'

def lexerAritmetico(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()
        tokens = []
        i = 0
        
        # Mapping from operator characters to Tokens enum values
        operator_to_token = {
            '=': Tokens.IGUAL,
            '+': Tokens.MAS,
            '-': Tokens.MENOS,
            '*': Tokens.MULTIPLICACION,
            '/': Tokens.DIVISION,
            '^': Tokens.POTENCIA
        }
        
        while i < len(contenido):
            # Skip whitespace
            if contenido[i].isspace():
                i += 1
                continue
                
            # Check for comments
            if i < len(contenido) - 1 and contenido[i:i+2] == '//':
                # Extract comment until end of line
                comment_end = contenido.find('\n', i)
                if comment_end == -1:  # If no newline found, comment goes to the end of file
                    comment_end = len(contenido)
                
                comment = contenido[i:comment_end]
                tokens.append({comment: Tokens.COMENTARIO})
                i = comment_end + 1 if comment_end < len(contenido) else len(contenido)
                continue
            
            # Check for parentheses
            if contenido[i] == '(':
                tokens.append({contenido[i]: Tokens.PARENTESIS_IZQ})
                i += 1
                continue
            elif contenido[i] == ')':
                tokens.append({contenido[i]: Tokens.PARENTESIS_DER})
                i += 1
                continue
                
            # Check for numbers and variables
            if contenido[i].isalnum() or contenido[i] in '.+-':
                # Start building a token (number, variable, float)
                current_token = contenido[i]
                i += 1
                # Continue collecting characters for the token
                while i < len(contenido) and (contenido[i].isalnum() or contenido[i] == '.' or 
                                             (contenido[i] in '+-' and i > 0 and contenido[i-1].lower() == 'e')):
                    current_token += contenido[i]
                    i += 1
                
                # Classify the token
                if enteros.accepts(current_token):
                    tokens.append({current_token: Tokens.ENTERO})
                elif flotantes.accepts(current_token):
                    tokens.append({current_token: Tokens.FLOTANTE})
                elif variables.accepts(current_token):
                    tokens.append({current_token: Tokens.VARIABLE})
                else:
                    tokens.append({current_token: Tokens.OTRO})
            
            # Check for operators
            if contenido[i] in operator_to_token:
                tokens.append({contenido[i]: operator_to_token[contenido[i]]})
                i += 1
                continue
            else:
                # Skip any unrecognized characters
                i += 1
        
        print("TOKEN\t\tTIPO")
        print("------------------------")
        for token in tokens:
            for key, value in token.items():
                print(f"{key}\t\t{value.value}")

lexerAritmetico('tarea3/prueba.txt')