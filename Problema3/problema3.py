import re

def reconocer_cadenas(C):
    """
    Implementa el reconocimiento de cadenas para notación científica, 
    direcciones IP, y correos electrónicos usando Expresiones Regulares.
    """
    resultados = {}
    
    regex_cientifica = r'^[+-]?\d+(\.\d+)?[eE][+-]?\d+$'
    
    regex_ip = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    regex_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.fullmatch(regex_cientifica, C):
        resultados['notacion_cientifica'] = True
    else:
        resultados['notacion_cientifica'] = False

    es_ip_valida = False
    if re.fullmatch(regex_ip, C):
        partes = C.split('.')
        if all(0 <= int(p) <= 255 for p in partes):
            es_ip_valida = True
            
    resultados['ip'] = es_ip_valida

    if re.fullmatch(regex_email, C):
        resultados['correo_electronico'] = True
    else:
        resultados['correo_electronico'] = False
        
    return resultados

cadenas_a_probar = [
    "1.23e-10",             
    "192.168.1.1",          
    "usuario.ejemplo@uneg.edu.ve",
    "-5E+2",                 
    "300.1.1.1",            
    "a@b.c",                
    "un texto cualquiera",  
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