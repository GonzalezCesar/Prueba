import re

def validar_fen(cadena):
    """
    Valida si una cadena está en notación Forsyth–Edwards (FEN).
    Devuelve True si es válida, False si no lo es.
    """
    # Expresión regular basada en el formato FEN estándar
    patron = re.compile(
        r"^"
        r"([prnbqkPRNBQK1-8]{1,8}/){7}"  # 8 filas del tablero (7 con '/')
        r"[prnbqkPRNBQK1-8]{1,8}"        # última fila sin '/'
        r"\s"                            # espacio
        r"[wb]"                           # turno: 'w' o 'b'
        r"\s"
        r"(-|[KQkq]{1,4})"                # enroques posibles
        r"\s"
        r"(-|[a-h][36])"                  # captura al paso
        r"\s"
        r"\d+"                            # medio movimiento
        r"\s"
        r"\d+"                            # número de movimiento
        r"$"
    )

    return bool(patron.match(cadena.strip()))

# --- Ejemplo de uso ---
if __name__ == "__main__":
    ejemplos = [
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",  # válida
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1",    # válida
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b KQ - 10 20", # válida
        "rnbqkbnr/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",   # inválida (solo 7 filas)
        "hola mundo"                                                # inválida
    ]

    for e in ejemplos:
        print(f"'{e}' → {'VÁLIDA' if validar_fen(e) else 'INVÁLIDA'}")
