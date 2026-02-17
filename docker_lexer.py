import re
from pathlib import Path

# 1. DEFINICIÓN DE TOKENS PARA DOCKERFILE (PASO 1)
tokens = [
    ('FROM', r'\bFROM\b'),
    ('RUN', r'\bRUN\b'),
    ('COPY', r'\bCOPY\b'),
    ('CMD', r'\bCMD\b'),
    ('WORKDIR', r'\bWORKDIR\b'),
    ('ENV', r'\bENV\b'),
    ('ARG', r'\bARG\b'),
    ('EXPOSE', r'\bEXPOSE\b'),
    
    ('PATH', r'^[./]|[./][a-zA-Z0-9._/-]+'),
    
    ('STRING', r'"[^"]*"|\'[^\']*\'|\[.*\]'),
    
    ('NUMBER', r'\d+'),
    
    ('IMAGE_NAME', r'[a-zA-Z][a-zA-Z0-9._/-]*(:[a-zA-Z0-9._-]*)?'),
    ('IDENT', r'[a-zA-Z_][a-zA-Z0-9_-]*'),  
    
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
    ('COMMENT', r'#.*'),
    ('MISMATCH', r'.'),
]


def lexer(input_text):
    """Función principal del analizador léxico (PASO 2)"""
    # Construir regex global
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)
    
    line_num = 1
    line_start = 0
    
    for mo in re.finditer(token_regex, input_text, re.MULTILINE):
        kind = mo.lastgroup
        value = mo.group(kind)
        
        if kind == 'NEWLINE':
            line_start = mo.end()
            line_num += 1
        elif kind == 'SKIP' or kind == 'COMMENT':
            continue  
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} inesperado en línea {line_num}')
        else:
            column = mo.start() - line_start
            yield kind, value, line_num, column

def cargar_archivo(nombre_archivo):
    """Lee el archivo Dockerfile"""
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"❌ Error: El archivo '{nombre_archivo}' no existe")
        return None
    except Exception as e:
        print(f"❌ Error al leer archivo: {e}")
        return None

# 3. PRUEBA PRINCIPAL
if __name__ == "__main__":
    nombre_archivo = "Dockerfile"
    
    input_text = cargar_archivo(nombre_archivo)
    if input_text is None:
        print("💡 Crea un archivo 'Dockerfile' en la misma carpeta")
    else:
        print("🚀 Analizando Dockerfile...")
        print("=" * 50)
        try:
            for token in lexer(input_text):
                print(f"({token[0]}, '{token[1]}', línea {token[2]}, col {token[3]})")
            print("\n✅ Análisis léxico COMPLETADO sin errores")
        except RuntimeError as e:
            print(f"\n❌ ERROR LÉXICO: {e}")
