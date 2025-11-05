import re

def reconocer_cadenas(C):
    """
    Implementa el reconocimiento de cadenas para notación científica, 
    direcciones IP, y correos electrónicos usando Expresiones Regulares.
    """
    resultados = {}
    
    # 1. Patrón para Notación Científica
    # Formato: [+/-]D[.D+]e[+/-]D+
    # Ejemplo: -1.23e+10, 5e-2, 10.0e5
    regex_cientifica = r'^[+-]?\d+(\.\d+)?[eE][+-]?\d+$'
    
    # 2. Patrón para Dirección IP (IPv4)
    # Formato: D.D.D.D, donde cada D es un número de 0 a 255
    # La regex se centra en la estructura (cuatro grupos de 1-3 dígitos separados por puntos), 
    # la validación estricta de 0-255 es más compleja y a menudo se realiza con lógica de código, 
    # pero para reconocimiento de patrón básico, esta es común:
    regex_ip = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    # 3. Patrón para Correo Electrónico
    # Formato: local-part@domain.tld
    # Una versión robusta que cumple la mayoría de los estándares:
    # (El componente local-part es el más complejo)
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # --- Verificación ---
    
    # 1. Notación Científica
    if re.fullmatch(regex_cientifica, C):
        resultados['notacion_cientifica'] = True
    else:
        resultados['notacion_cientifica'] = False

    # 2. Dirección IP (IPv4)
    # Se añade una comprobación lógica adicional para la validez de 0-255, 
    # ya que la regex sola acepta 999.999.999.999.
    es_ip_valida = False
    if re.fullmatch(regex_ip, C):
        partes = C.split('.')
        if all(0 <= int(p) <= 255 for p in partes):
            es_ip_valida = True
            
    resultados['ip'] = es_ip_valida

    # 3. Correo Electrónico
    if re.fullmatch(regex_email, C):
        resultados['correo_electronico'] = True
    else:
        resultados['correo_electronico'] = False
        
    return resultados

# --- Ejemplos de uso ---
cadenas_a_probar = [
    "1.23e-10",              # Científica Válida
    "192.168.1.1",           # IP Válida
    "usuario.ejemplo@uneg.edu.ve", # Email Válido
    "-5E+2",                 # Científica Válida
    "300.1.1.1",             # IP Inválida (300 > 255)
    "a@b.c",                 # Email Inválido (.c es muy corto)
    "un texto cualquiera",   # Ninguno
]

print("-" * 50)
print(f"{'Cadena':<30} | {'Científica':^10} | {'IP':^4} | {'Email':^5}")
print("-" * 50)

for c in cadenas_a_probar:
    r = reconocer_cadenas(c)
    cientifica = "✅" if r['notacion_cientifica'] else "❌"
    ip = "✅" if r['ip'] else "❌"
    email = "✅" if r['correo_electronico'] else "❌"
    print(f"{c:<30} | {cientifica:^10} | {ip:^4} | {email:^5}")

print("-" * 50)