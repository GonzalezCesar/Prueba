import re

def validar_fila_fen(row_str: str) -> bool:
    """Valida que una sola fila de FEN sume 8."""
    count = 0
    for char in row_str:
        if char.isdigit():
            count += int(char)
        elif char.isalpha():
            count += 1
        else:
            return False 
    return count == 8

def validar_fen(fen_str: str) -> bool:
    """
    Valida una cadena FEN completa, tanto sintáctica como semánticamente
    (en términos de conteo de filas).
    """
    fen_regex = re.compile(
        r"^\s*([rnbqkpRNBQKP1-8]{1,8}\/){7}[rnbqkpRNBQKP1-8]{1,8}\s"  
        r"[wb]\s"                                                    
        r"(K?Q?k?q?|-)\s"                                            
        r"(-|[a-h][36])\s"                                           
        r"\d+\s"                                                     
        r"\d+\s*$"                                                   
    )
    
    if not fen_regex.match(fen_str):
        print(f"Error: La estructura FEN general es inválida.")
        return False
    
    try:
        campos = fen_str.strip().split()
        filas_str = campos[0]
        filas = filas_str.split('/')
        
        if len(filas) != 8:
            print("Error: El campo de piezas no tiene 8 filas.")
            return False
            
        for i, fila in enumerate(filas):
            if not validar_fila_fen(fila):
                print(f"Error: La fila {i+1} ('{fila}') no suma 8 escaques.")
                return False
                
    except Exception as e:
        print(f"Error inesperado durante la validación de filas: {e}")
        return False
        
    return True

fen_inicio = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
fen_invalida_fila = "rnbqkbnr/pppppppp/8/8/4/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1" 
fen_invalida_estructura = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w ZZZ - 0 1" 

print(f"'{fen_inicio}': {validar_fen(fen_inicio)}")
print(f"'{fen_invalida_fila}': {validar_fen(fen_invalida_fila)}")
print(f"'{fen_invalida_estructura}': {validar_fen(fen_invalida_estructura)}")