import sys
import re

keywords = {
    "auto": "automatico",
    "break": "romper",
    "case": "caso",
    "char": "caracter",
    "const": "constante",
    "continue": "continuar",
    "default": "defecto",
    "do": "hacer",
    "double": "doble",
    "else": "si no",
    "enum": "enumeracion",
    "extern": "externo",
    "float": "flotante",
    "for": "para",
    "goto": "ir a",
    "if": "si",
    "int": "entero",
    "long": "largo",
    "register": "registro",
    "return": "retornar",
    "short": "corto",
    "signed": "con signo",
    "sizeof": "tamano de",
    "static": "estatico",
    "struct": "estructura",
    "switch": "cambiar",
    "typedef": "definir tipo",
    "union": "union",
    "unsigned": "sin signo",
    "void": "vacio",
    "volatile": "volatil",
    "while": "mientras",
}

def main():
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} problema4.c", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error al leer el archivo: {file_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Contenido del archivo:\n{content}")
    print("\nPalabras reservadas encontradas y sus traducciones:")

    words = re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*', content)
    found_keywords = set()

    for word in words:
        if word in keywords and word not in found_keywords:
            print(f"{word} -> {keywords[word]}")
            found_keywords.add(word)

if __name__ == "__main__":
    main()